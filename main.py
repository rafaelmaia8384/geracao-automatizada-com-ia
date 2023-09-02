import os
import re
import json
import openai
import time
import random
from dotenv import load_dotenv
import git


load_dotenv(".env")

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_subject():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            functions=[
                {
                    "name": "generate_subject",
                    "description": "Geração de um assunto sobre programação em python.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "subject": {
                                "type": "string",
                                "description": "Resumo, com no máximo 300 caracteres, do assunto.",
                            },
                        },
                        "required": [
                            "subject",
                        ],
                    },
                }
            ],
            messages=[
                {
                    "role": "system",
                    "content": "Você é uma IA que ajuda a gerar assuntos específicos sobre a área de programação em python.",
                },
                {
                    "role": "user",
                    "content": "Um tópico ou assunto sobre programação em python que pode ser ensinado para estudantes do curso de graducação em Ciências da Computação.",
                },
            ],
            function_call={"name": "generate_subject"},
        )
        result = json.loads(
            response.choices[0]["message"]["function_call"]["arguments"]
        )
        return result["subject"]
    except Exception as e:
        print(e)
        return None


def get_code_from_subject(subject):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            functions=[
                {
                    "name": "generate_code_from_subject",
                    "description": "Geração simples de código em python.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "Código em python utilizado para exemplificar o assunto fornecido.",
                            },
                        },
                        "required": [
                            "code",
                        ],
                    },
                }
            ],
            messages=[
                {
                    "role": "system",
                    "content": "Você é uma IA que ajuda a gerar código específico sobre um tópico em python.",
                },
                {
                    "role": "user",
                    "content": f"Gere um código em python exemplificando o assunto a seguir:\n\n{subject}",
                },
            ],
            function_call={"name": "generate_code_from_subject"},
        )
        result = json.loads(
            response.choices[0]["message"]["function_call"]["arguments"]
        )
        return result["code"]
    except Exception as e:
        print(e)
        return None


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = s[:50]
    return s


def save_code_to_file(subject, code):
    slug_from_subject = slugify(subject)
    file_name = f"{slug_from_subject}.py"
    if os.path.exists(file_name):
        return
    with open(f"./examples/{file_name}", "w") as f:
        f.write(f"# {subject}\n\n")
        f.write(code)
    print(f"File {file_name} created successfully!")


def commit_and_push(repo, commit_message):
    repo.git.add("--all")
    repo.git.commit("-m", commit_message)
    repo.git.push()


def job():
    subject = get_subject()
    if subject:
        code = get_code_from_subject(subject)
        if code:
            save_code_to_file(subject, code)
            project_dir = os.getcwd()
            repo = git.Repo(project_dir)
            commit_and_push(repo, subject)
            print("Successfully committed and pushed to GitHub!")
            return
    print("Something went wrong!")


wait_time_seconds = 3600 * 8


if __name__ == "__main__":
    wait_hours = wait_time_seconds / 3600
    while True:
        print(f"Next job in {wait_hours} hours...")
        time.sleep(wait_time_seconds)
        random_number = random.randint(0, 100)
        if random_number < 40:
            print("Job running...")
            job()
        else:
            print("Not now!")
