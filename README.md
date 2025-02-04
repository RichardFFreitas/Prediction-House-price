# Previsão de Preço de Imóveis
### Este é um projeto de previsão de preços de imóveis utilizando aprendizado de máquina, especificamente o algoritmo Gradient Boosting, com a biblioteca scikit-learn. O objetivo do projeto é prever o preço de um imóvel com base em características como o número de quartos, área, localização e outros dados.

# Descrição
### O modelo foi treinado utilizando dois conjuntos de dados de imóveis, e a partir desses dados, é possível prever o preço de um imóvel com base nas suas características. O projeto é completo, abrangendo desde a manipulação e pré-processamento dos dados até a implementação do modelo e a visualização dos resultados.

# 🛠️ Tecnologias Utilizadas
### Python: Linguagem de programação.
### scikit-learn: Biblioteca de aprendizado de máquina.
### pandas: Manipulação e análise de dados.
### matplotlib: Visualização de dados.
### seaborn: Visualização de dados estatísticos.

# Estrutura do Projeto
```python
├── data/ # Pasta contendo os datasets em formato CSV
│   ├── df1.csv # Dataset de características de imóveis
│   └── df2.csv # Dataset de informações adicionais sobre imóveis
├── model.py # Código principal para treinamento e avaliação do modelo
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto
```

# Instalação
### Pré-requisitos
#### Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode verificar isso executando:
```python
python --version
``` 
# Passos para instalar

### Clone este repositório:

```python
git clone https://github.com/usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
# Instale as dependências utilizando Poetry:

```python
poetry install
```

# Dependências
## Este projeto depende das seguintes bibliotecas:

#### scikit-learn
#### pandas
#### matplotlib
#### seaborn

# Como Usar
## Prepare os dados: Coloque os arquivos CSV (df1.csv e df2.csv) na pasta data/.

Execute o script model.py para treinar o modelo e fazer previsões:

```python
python model.py
```

O modelo irá realizar a previsão do preço de imóveis com base nos dados fornecidos e gerar um gráfico comparando o preço real com o preço previsto.

Resultados Esperados
Após a execução do script, o modelo irá exibir o gráfico de dispersão comparando o preço real versus o preço previsto. O gráfico será gerado utilizando a biblioteca matplotlib.
Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
