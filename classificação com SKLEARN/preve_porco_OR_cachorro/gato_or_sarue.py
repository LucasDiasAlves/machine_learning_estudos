from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

perguntas = ['Ele tem pelo curto?',
             'Ele tem varias cores?',
             'Ele comum mente escala?',
             'Ele tambem come ovo?',
             'Por acaso mia?',
             'Ele se finge de morto?',
             'Ele tem garras retrateis?',
             'Ele tem sido domesticado?',]
resultado = []
print("--------------- Irei adivinhar se seu animal é um GATO ou um SARUÉ ------------\n")
print("------------------------- Coloque 1 para SIM e 0 para NÃO ---------------------\n")

for i in perguntas:
    respota = int(input(i))
    resultado.append(respota)

# animal_misterioso = [0,0,1,0,1,0,0,0]
previsoes = modelo.predict([resultado])

if previsoes == 1:
    print("O animal o qual me forneceu informações é um FELINO 🐈‍⬛🐈😺😸😹😼🐱😻😾😿🙀😽")
    caminho = 'preve_porco_OR_cachorro/gato.jpg'
elif previsoes == 0:
    print("O animal o qual me forneceu informações é um SARUÉ 🦨🦨🦨🦨🦨🦨🦨🦨")
    caminho = 'preve_porco_OR_cachorro/sarue.jpg'
    
try:
    img = mpimg.imread(caminho)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
