# 1° análise inicial com o PairPlot da Seaborn para verificar a relação entre as variáveis.
# 2° construir modelos de regressão linear;
# 3° realizar a comparação desses modelos; 

import pandas as pd
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from sklearn.metrics import r2_score
import statsmodels.api as sm
import matplotlib.pyplot as plt 
import seaborn as sns

base_dados = './data_science_testando_relaçoes_com_regressao_linear/desafio/hoteis.csv'

dados = pd.read_csv(base_dados)
print(dados.head())

sns.pairplot(dados)
plt.show()