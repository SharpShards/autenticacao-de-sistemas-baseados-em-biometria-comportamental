# Biometria Comportamental com Modelos de Machine Learning

Este projeto realiza o treinamento e a avaliação de diferentes classificadores de machine learning utilizando um conjunto de features previamente processado. A análise inclui o cálculo de métricas como acurácia, FAR (False Acceptance Rate), FRR (False Rejection Rate), F1-score e validação cruzada.

## Estrutura do Projeto

model/
│
├── main.py
├── data_processing.py
├── model_training.py
├── metrics.py
└── requirements.txt
└── README.md # Documentação do projeto


- **main.py**: Script principal que orquestra o fluxo do projeto, desde o carregamento dos dados até a avaliação dos modelos.
- **data_processing.py**: Contém funções para carregar e dividir os dados entre conjuntos de treino e teste.
- **model_training.py**: Implementa funções para treinar diferentes modelos de machine learning.
- **metrics.py**: Contém funções para calcular as métricas de desempenho dos modelos.
- **requirements.txt**: Lista as dependências do projeto.

## Dependências

As dependências necessárias para executar o projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

`pip install -r requirements.txt

## Como Executar

Certifique-se de que todos os arquivos estão no diretório do projeto.
Coloque o arquivo de dados features.xlsx no diretório results/.

Execute o script principal:

`python main.py

Os resultados serão salvos em um arquivo Excel chamado metrics.xlsx dentro do diretório results/.


# Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

# Licença
Este projeto está licenciado sob os termos da MIT License.





