import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import StandardScaler
# ========================================================================================
# TREINO COM MODELO SVC - UMA LINHA RETA
# ========================================================================================


url = "https://gist.githubusercontent.com/guilhermesilveira/12291c548acaf544596795709020e3db/raw/325bdef098bd9cbc2189215b7e32e22f437f29f3/projetos.csv"

dados = pd.read_csv(url)

dados["finalizados"] = dados["nao_finalizado"].map({1: 0, 0: 1})

dados = dados.query("horas_esperadas > 0")

semente = 9248
x = dados[["horas_esperadas", "preco"]]
y = dados["finalizados"]
raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x,y, random_state = semente) 
# modelo = SVC(gamma="auto")

scaler = StandardScaler()
scaler.fit(raw_treino_x)

treino_x = scaler.transform(raw_treino_x)
teste_x = scaler.transform(raw_teste_x)

modelo = SVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)
acuracia = accuracy_score(teste_y, previsoes) * 100

print(f"A acurácia é de {acuracia:.2f}%\n")    
print("Distribuição das classes no treino:")
print(treino_y.value_counts())
print("\nDistribuição das classes no teste:")
print(teste_y.value_counts())

data_col1 = teste_x[:,0]
data_col2 = teste_x[:,1]


x_min = data_col1.min()
x_max = data_col1.max()
y_min = data_col2.min()
y_max = data_col2.max()

# print(f"x_min:{x_min}")
# print(f"x_max:{x_max}")
# print(f"y_min:{y_min}")
# print(f"y_max:{y_max}")

pixels = 100

eixo_x = np.arange(x_min, x_max, (x_max - x_min) / pixels)
eixo_y = np.arange(y_min, y_max, (y_max - y_min) / pixels)
xx, yy = np.meshgrid(eixo_x, eixo_y)

pontos = np.c_[xx.ravel(), yy.ravel()]

z = modelo.predict(pontos)
z = z.reshape(xx.shape)

plt.contourf(xx,yy,z)
plt.scatter(data_col1, data_col2, c=teste_y, alpha=0.8, s=3)
plt.show()

print(z)