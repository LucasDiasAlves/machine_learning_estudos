## Site de projetos

descobrindo em uma base de dados de um site de projetos, qunatos projetos foram finalziados, baseando em :
- horas de projeto;
- preço do projeto;

Plotamos 2 gráficos:
- finalizados;
- não finalizados;
Para assim podermos entender como a relação de preço pelas horas trabalham.

Limpamos a base de dados para ter apenas horas_esperadas > 0; pois ocorria algum erro na base de dados com esses horarios

---

## 📊 Análise de Desempenho e Fronteira de Decisão
Após treinar o modelo LinearSVC e plotar a fronteira de decisão (fundo do gráfico) sobreposta aos dados reais de teste (scatter plot), identificamos uma limitação fundamental na abordagem atual:

### Incompatibilidade Visual: 
A área de preenchimento gerada pelas previsões do modelo não acompanha a distribuição real dos dados de teste.

### A Causa (Limitação Linear): 
O algoritmo LinearSVC é projetado para encontrar relações estritamente lineares (traçando uma linha reta para separar as classes). No entanto, a dispersão das horas esperadas e preços nesta base de dados apresenta um comportamento claramente não-linear.

### Conclusão: 
O modelo está sofrendo de underfitting para este problema específico. Uma linha reta é incapaz de capturar as nuances e curvas que definem se um projeto será finalizado ou não.