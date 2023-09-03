# Implementação de algoritmos de classificação de aprendizado de máquina usando a biblioteca scikit-learn em Python.

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Carrega o dataset do iris
iris = datasets.load_iris()

# Split do dataset em treino e teste
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=42)

# Cria a instância do classificador SVM
clf = svm.SVC(kernel='linear', C=1)

# Treina o modelo
clf.fit(X_train, y_train)

# Faz previsões no conjunto de teste
predictions = clf.predict(X_test)

# Avalia a precisão das previsões
print("Accuracy:", metrics.accuracy_score(y_test, predictions))