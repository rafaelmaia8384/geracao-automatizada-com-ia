# Análise de Dados com Python: Uso do Pandas para Manipulação de Dados

import pandas as pd

# Criação de um DataFrame simples

volunteers_dict = {
    'names': ['John Doe', 'Jane Doe', 'Mary Johnson', 'James Smith', 'Patricia Williams'],
    'email': ['john.doe@email.com', 'jane.doe@email.com', 'mary.johnson@email.com', 'james.smith@email.com', 'patricia.williams@email.com'],
    'age': [25, 28, 35, 19, 40],
    'hours_volunteered': [100, 80, 250, 60, 150]
}

volunteers_df = pd.DataFrame(volunteers_dict)

print("volunteers dataframe:", volunteers_df)


# Manipulação de Dados

# 1. Seleção de Coluna

email_column = volunteers_df['email']
print("\nemail column:", email_column)

# 2. Filtro de dados

above_30 = volunteers_df[volunteers_df['age'] > 30]
print("\nVolunteers older than 30:", above_30)