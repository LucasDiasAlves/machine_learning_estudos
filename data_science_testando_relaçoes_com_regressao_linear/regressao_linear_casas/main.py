import pandas as pd
from sklearn.model_selection import train_test_split 
from statsmodels.formula.api import ols
from sklearn.metrics import r2_score
import statsmodels.api as sm
import matplotlib as plt

base_dados = './data_science_testando_relaçoes_com_regressao_linear/regressao_linear_casas/Preços_de_casas.csv'
dados = pd.read_csv(base_dados)
dados = dados.drop(columns='Id') #retirando a coluna ID pois não é eficiente para o treinamento.
corr = dados.corr()
y = dados['preco_de_venda']
x = dados.drop(columns='preco_de_venda')


x_train, x_test, y_train, y_test = train_test_split(x,y , test_size = 0.4 , random_state = 230)
df_train = pd.DataFrame(data = x_train)
df_train['preco_de_venda'] = y_train

modelo_0 = ols('preco_de_venda ~ area_primeiro_andar', data = df_train).fit()


x_train = sm.add_constant(x_train)
# print(x_train.head)

modelo_1 = sm.OLS(y_train, x_train[['const','existe_segundo_andar','area_segundo_andar','quantidade_banheiros','capacidade_carros_garagem','qualidade_da_cozinha_Excelente']]).fit()

modelo_2 = sm.OLS(y_train,x_train[['const','existe_segundo_andar','quantidade_banheiros','capacidade_carros_garagem','qualidade_da_cozinha_Excelente']]).fit()

modelo_3 = sm.OLS(y_train, x_train[['const','existe_segundo_andar','quantidade_banheiros','qualidade_da_cozinha_Excelente']]).fit()

# print(modelo_0.summary())

# print(modelo_0.resid)
# print(modelo_0.resid.hist())
# plt.tittle("Distribuiçãp dos residuos")
# plt.show()

y_predict = modelo_0.predict(x_test)
print("R²")
print("Modelo 0: ", modelo_0.rsquared)
print("Modelo 1: ", modelo_1.rsquared)
print("Modelo 2: ", modelo_2.rsquared)
print("Modelo 3: ", modelo_3.rsquared)

print(len(modelo_0.params)) # retorna o numero de parametros do modelo
print(len(modelo_1.params))
print(len(modelo_2.params))
print(len(modelo_3.params))

# print(corr['preco_de_venda'])
# print(dados.columns)