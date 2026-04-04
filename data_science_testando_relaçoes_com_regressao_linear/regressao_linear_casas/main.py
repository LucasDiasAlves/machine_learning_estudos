import pandas as pd


base_dados = './data_science_testando_relaçoes_com_regressao_linear/regressao_linear_casas/Preços_de_casas.csv'

dados = pd.read_csv(base_dados)

dados = dados.drop(columns='Id') #retirando a coluna ID pois não é eficiente para o treinamento.
corr = dados.corr()

print(corr['preco_de_venda'])
print(dados.columns)