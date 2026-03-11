# Entendendo o projeto
trabalhamos com Classificação, um tipo de problema de aprendizado de máquina onde o objetivo é categorizar ou rotular dados em diferentes classes ou categorias. Por exemplo, classificar emails como "spam" ou "não spam", ou identificar se uma imagem contém um "gato" ou um "cachorro".

Iniciamos nosso projeto definindo as características de porcos e cachorros e utilizamos um algoritmo chamado LinearSVC para realizar a classificação desses animais.

---

## Entendendo o LinearSVC
O **LinearSVC** é um tipo de algoritmo de Máquinas de Vetores de Suporte (SVM) que utiliza **uma função linear** para separar os dados em diferentes classes. Vamos entender como ele funciona de maneira simplificada:

### Coleta de Dados: 
Primeiro, coletamos dados sobre porcos e cachorros. Esses dados podem incluir características como peso, altura, cor do pelo, comprimento das orelhas, etc. Cada exemplo no nosso conjunto de dados tem várias características e um rótulo indicando se é um porco ou um cachorro.

### Treinamento do Modelo:
O LinearSVC analisa esses dados e tenta encontrar a melhor linha (ou hiperplano, se tivermos mais de duas características) que separa as classes de porcos e cachorros. A melhor linha é aquela que maximiza a distância entre os exemplos mais próximos de cada classe, chamados de vetores de suporte.

### Classificação de Novos Dados: 
Uma vez que o modelo foi treinado e encontrou a linha de separação, ele pode ser usado para classificar novos dados. Se um novo exemplo cair de um lado da linha, será classificado como porco; se cair do outro lado, será classificado como cachorro.