import pandas as pd
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier

# --------------------------------------------------------------------------------------------
# -------------------------------------- TRATANDO OS DADOS------------------------------------
url = "https://gist.githubusercontent.com/guilhermesilveira/dd7ba8142321c2c8aaa0ddd6c8862fcc/raw/e694a9b43bae4d52b6c990a5654a193c3f870750/precos.csv"

dados = pd.read_csv(url)
dados["km_por_ano"] = dados["milhas_por_ano"] * 1.60934
dados["idade"] = datetime.today().year - dados["ano_do_modelo"]
dados.drop(["milhas_por_ano","ano_do_modelo"], axis=1 , inplace=True)
# ------------------------------------------------------------------------------------------------------




semente = 5719

x = dados[['preco','idade','km_por_ano']]
y = dados['vendido']

raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x,y, random_state = semente) 

scaler = StandardScaler()
scaler.fit(raw_treino_x)

# treino_x = scaler.transform(raw_treino_x)
# teste_x = scaler.transform(raw_teste_x)

classificador = DummyClassifier()
classificador.fit(raw_treino_x, treino_y)
previsoes = classificador.predict(raw_teste_x)

# modelo = SVC(gamma='auto')
# modelo.fit(treino_x,treino_y)
# previsoes = modelo.predict(teste_x)
acuracia = accuracy_score(teste_y, previsoes) * 100

print(f"A acurácia é de {acuracia:.2f}%\n")    
print("Distribuição das classes no treino:")
print(treino_y.value_counts())
print("\nDistribuição das classes no teste:")
print(teste_y.value_counts())


sns.relplot(x="km_por_ano", y="preco", data=dados, hue="vendido", col="vendido")
plt.show()

print(dados.columns)