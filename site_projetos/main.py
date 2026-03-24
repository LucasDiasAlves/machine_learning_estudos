import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score

url = "https://gist.githubusercontent.com/guilhermesilveira/12291c548acaf544596795709020e3db/raw/325bdef098bd9cbc2189215b7e32e22f437f29f3/projetos.csv"

dados = pd.read_csv(url)

dados["finalizados"] = dados["nao_finalizado"].map({1: 0, 0: 1})

dados = dados.query("horas_esperadas > 0")

# sns.relplot(x="horas_esperadas", y="preco", data=dados, hue="finalizados", col="finalizados")
# plt.show()

def treino(x, y):
    semente = 9248

    treino_x, teste_x, treino_y, teste_y = train_test_split(x,y, random_state = semente) 

    modelo = LinearSVC()
    modelo.fit(treino_x,treino_y)
    previsoes = modelo.predict(teste_x)

    acuracia = accuracy_score(teste_y, previsoes) * 100
    print(f"A acurácia é de {acuracia:.2f}%\n")    
    print("Distribuição das classes no treino:")
    print(treino_y.value_counts())
    print("\nDistribuição das classes no teste:")
    print(teste_y.value_counts())

treino(dados[["horas_esperadas", "preco"]], dados["finalizados"])

# print(dados.head())