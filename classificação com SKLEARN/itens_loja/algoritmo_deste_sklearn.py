from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score

semente = 9248

url = "https://gist.githubusercontent.com/guilhermesilveira/b9dd8e4b62b9e22ebcb9c8e89c271de4/raw/c69ec4b708fba03c445397b6a361db4345c83d7a/tracking.csv"
dados = pd.read_csv(url)

y = dados["comprou"]
x = dados[["inicial", "palestras", "contato", "patrocinio"]]

treino_x, teste_x, treino_y, teste_y = train_test_split(x,y, random_state = semente) 


modelo = LinearSVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print(f"A acuracia é de {acuracia:.2f}%")
print(treino_x.value_counts())
print(treino_y.value_counts())
print(teste_x.value_counts())