import pandas as pd

url = "https://gist.githubusercontent.com/guilhermesilveira/12291c548acaf544596795709020e3db/raw/325bdef098bd9cbc2189215b7e32e22f437f29f3/projetos.csv"

dados = pd.read_csv(url)

dados = dados["nao_finalizado"].map({1: 0, 0: 1})
print(dados.head())