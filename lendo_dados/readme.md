# Detalhes

neste projeto é para verificar se um usuario ira comprar items em uma loja.
diferente da previsão do porco e cachorro, aqui separamos os dados de treino para os dados de teste, para não ocorrer **OVERFIT**, oque seria o algoritmo decorar os dados, e não prever oque vem.

---

usamos uma biblioteca do sklearn par ao treinamento do nosso modelo, e passamos uma seed aleatoria para a captação dos dados para treino e teste, pois assim, no cenarios dos porcos e cachorros, elimna uma a chance de cair apenas porco no treino e cachorro no teste, se acontecer isso o algoritmo não foi bem treinado.

---

Imagine que você está trabalhando em um projeto de Machine Learning para desenvolver um modelo que possa prever se um email é spam ou não. Você tem um conjunto de dados contendo milhares de emails, cada um rotulado como 'spam' ou 'não spam'. A questão é: como garantir que o modelo aprenda a classificar esses e-mails de forma eficaz e confiável?

A resposta começa com uma prática fundamental em machine learning: a separação dos dados em conjuntos de treino e teste. Essa divisão é crucial para avaliar o desempenho do modelo de forma justa e realista.

## O que são dados de treino e teste?
Dados de Treino: São usados para "ensinar" o modelo. É com esse conjunto de dados que o algoritmo aprende a identificar padrões e fazer previsões ou classificações.

## Dados de Teste:
São usados para avaliar o desempenho do modelo. Eles são mantidos separados e só são usados após o modelo estar completamente treinado. A ideia é testar o modelo com dados que ele nunca viu antes, simulando como ele performaria em situações reais.

## Como separar os dados?
A proporção típica para dividir os dados varia dependendo do tamanho do conjunto de dados e da natureza do problema, mas uma divisão comum é 80% para treino e 20% para teste. Isso significa que 80% do total dos dados disponíveis são usados para treinar o modelo, enquanto os restantes 20% são reservados para testá-lo.

## Métodos de divisão:

### Aleatória:
A divisão aleatória consiste em separar os dados de forma totalmente randômica. Isso significa que cada dado tem a mesma chance de ser incluído no conjunto de treino ou no conjunto de teste, sem qualquer consideração adicional. Esse método é útil quando os dados são balanceados, ou seja, quando as classes no conjunto de dados estão representadas de forma proporcional.

### Estratificada:
Em problemas de classificação, essa técnica garante que as proporções das diferentes classes sejam mantidas nos conjuntos de treino e teste. Por exemplo, se 30% dos seus e-mails são spam, 30% dos dados de treino e de teste também deverão ser spam. Esse método é especialmente importante em problemas de classificação com classes desbalanceadas. Manter as proporções das classes ajuda a garantir que o modelo seja treinado e avaliado de forma justa, evitando cenários onde, por exemplo, o modelo vê muito mais exemplos de uma classe do que da outra.

Separar os dados em conjuntos de treino e teste é mais do que uma etapa técnica, é uma estratégia fundamental para desenvolver modelos de Machine Learning robustos e confiáveis. Ao garantir que seu modelo possa eficazmente generalizar além dos dados de treinamento, você aumenta significativamente as chances de sucesso em sua aplicação prática.