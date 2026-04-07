import pandas as pd
from sklearn.model_selection import train_test_split 
from statsmodels.formula.api import ols

base_dados = './data_science_testando_relaçoes_com_regressao_linear/regressao_linear_casas/Preços_de_casas.csv'

dados = pd.read_csv(base_dados)

dados = dados.drop(columns='Id') #retirando a coluna ID pois não é eficiente para o treinamento.
corr = dados.corr()

y = dados['preco_de_venda']
x = dados.drop['preco_de_venda']

x_train, x_test, y_train, y_test = train_test_split(x,y , test_size = 0.4 , random_state = 230)

df_train = pd.DataFrame(data = x_train)
df_train['preco_de_venda'] = y_train

modelo_0 = ols('preco_de_venda ~ area_primeiro_andar', data = df_train).fit()

print(modelo_0.params)
print(modelo_0.summary())
print(modelo_0.rsquared)

print(corr['preco_de_venda'])
print(dados.columns)