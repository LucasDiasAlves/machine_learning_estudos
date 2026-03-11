from sklearn.svm import LinearSVC

# features [1 sim, 0 nao]
# pelo longo
# perna curta
# faz auau?

# ------------------ dados de porcos e cachorros ---------------------------
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1 ,1]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1, 1, 1, 0, 0, 0] # definicao se é cachorro ou porco, 1 porco, 0 cachorro

modelo = LinearSVC() # modelo de treino
modelo.fit(dados, classes) # dados para treinar o modelo 

# animal_misterioso = [1, 1, 0]
# a = modelo.predict([animal_misterioso])
# ---------------------------------------------------------------------

# passando dados para animais misteriosos para o sistema prever
misterio1 = [1,1,1] 
misterio2 = [1,1,0]
misterio3 = [0,1,1]

testes = [misterio1, misterio2, misterio3]
previsoes = modelo.predict(testes) # prevendo o animal

teste_classes = [0, 1, 1]

# ======================= acuracia ============================
corretos = (previsoes == teste_classes).sum()
total = len(testes)
texa_de_acertos = corretos / total * 100

print(f"acuaracia: {texa_de_acertos:.2f}%")