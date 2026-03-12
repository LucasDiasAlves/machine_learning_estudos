from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# ----------------------------------------------------
# gato ou sarue

# features[1- sim | 0-não]:
# pelo curto?
# varias cores?
# escala?
# come ovo?
# mia?
# finge de morto?
# garras retrateis?
# domestico?
# ------------------------------------------------

gato1 = [1,1,1,0,1,0,1,1]
gato2 = [0,1,1,0,1,0,1,1]
gato3 = [1,0,0,0,1,0,0,0]
gato4 = [0,0,1,0,0,0,1,1]

sarue1 = [1,0,1,1,0,1,0,0]
sarue2 = [1,0,1,1,0,1,0,1]
sarue3 = [0,0,1,0,0,1,0,0]
sarue4 = [1,0,1,1,0,1,0,1]

dados = [gato1, gato2, gato3, gato4, sarue1, sarue2, sarue3, sarue4]
definicao = [1,1,1,1,0,0,0,0] #é gato ou não? 1-sim | 0-não

modelo = LinearSVC()
modelo.fit(dados, definicao)

animal_misterioso = [0,0,1,0,1,0,0,0]
previsoes = modelo.predict([animal_misterioso])

if previsoes == 1:
    print("O animal o qual me forneceu informações é um FELINO")
else:
    print("O animal o qual me forneceu informações é um SARUÉ")

