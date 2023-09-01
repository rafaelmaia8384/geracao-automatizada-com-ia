# Exploração aprofundada de bibliotecas Python padrão: NumPy, pandas e matplotlib. Compreendendo a importância dessas bibliotecas e suas aplicações práticas em Ciências da Computação, incluindo manipulação de dados, análise estatística e visualização de dados.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criando um array em numpy
array = np.array([1,2,3,4,5])
print('Array em Numpy:', array)

# Crianning um dataframe em pandas
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)
print('Dataframe em Pandas:\n', df)

#plotagem de um gráfico simples em matplotlib
plt.plot(array)
plt.ylabel('some numbers')
plt.show()