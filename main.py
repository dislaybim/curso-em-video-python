import pandas as pd
import numpy as np

# Criando um DataFrame com dados aleatórios usando o numpy
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Idade': np.random.randint(18, 30, size=5),  # Idades aleatórias entre 18 e 29
        'Pontuação': np.random.randint(0, 100, size=5)}  # Pontuações aleatórias entre 0 e 99

df = pd.DataFrame(data)

# Exibindo o DataFrame
print("DataFrame:")
print(df)

# Salvando o DataFrame em um arquivo Excel
excel_file = 'dados_excel.xlsx'
df.to_excel(excel_file, sheet_name='Dados', index=False)

print(f"\nOs dados foram salvos em '{excel_file}'.")
