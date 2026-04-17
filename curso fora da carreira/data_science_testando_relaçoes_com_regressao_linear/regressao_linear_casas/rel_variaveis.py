import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

base_dados = './data_science_testando_relaçoes_com_regressao_linear/regressao_linear_casas/Preços_de_casas.csv'

dados = pd.read_csv(base_dados)

dados = dados.drop(columns='Id') #retirando a coluna ID pois não é eficiente para o treinamento.

# plt.scatter(dados['area_primeiro_andar'], dados['preco_de_venda'])
# plt.axline(xy1=(66, 250000), xy2=(190,1800000), color='red')
# plt.title('Relação entre Preço e Area')
# plt.xlabel('area do primeiro andar')
# plt.ylabel('preco de venda')

# # # FORMA CORRETA (Recomendada)
# # fig = px.scatter(
# #     dados,                         # Primeiro argumento: o DataFrame
# #     x='area_primeiro_andar',       # String com o nome da coluna
# #     y='preco_de_venda',            # String com o nome da coluna
# #     trendline='ols', 
# #     trendline_color_override='red'
# # )

# # fig.show()
# plt.show()

# sns.pairplot(dados)
sns.pairplot(dados, y_vars='preco_de_venda', x_vars = ['quantidade_banheiros','area_segundo_andar'])
plt.show()