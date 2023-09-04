# Aplicando Python no desenvolvimento de algoritmos de aprendizado de máquina para análise de dados.

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Carrega o dataset
iris = datasets.load_iris()

# Divide o dataset em treino e teste
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=42)

# Inicializa o classificador
clf = svm.SVC(kernel='linear', C=1)

# Treina o classificador com os dados de treino
clf.fit(x_train, y_train)

# Faz as previsões com os dados de teste
predictions = clf.predict(x_test)

# Avalia a acurácia do algoritmo
print('Acurácia:', metrics.accuracy_score(y_test, predictions))