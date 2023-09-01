# Projeto para gerar código em python automaticamente com IA


## O que esse projeto faz
O arquivo main.py é responsável por fazer chamadas à API da openai e utilizar o modelo chatgpt-4 para criar códigos em python dado um determinado assunto. O assunto também é gerado via IA e é relacionado com as matérias vistas pelos estudantes de Ciência da Computação.

## Pré requisitos
Para rodar esse projeto, crie um arquivo .env na raíz do repositório e defina a variável de ambiente. Obtenha a chave no site do openai (openai.com).
```
OPENAI_API_KEY=SECRETKEY123
```

## Como rodar
```
pip install -r requirements.txt
python main.py
```

## Resultado
O projeto irá gerar arquivos com a terminação .py dentro da pasta examples. Se você desejar permitir que o app faça o push dos novos commits automaticamente, você deve configurar o acesso via ssh ao seu repositório (gerar chaves ssh e definir nas configurações do github)