# Projeto Biometria Comportamental

Este projeto é dividido em duas partes principais:

1. **Features**: Focado na coleta, preparação e extração de features a partir dos dados brutos.
2. **Model**: Responsável pelo treinamento e avaliação de modelos de machine learning.

## Estrutura do Projeto

project/

│

├── model/

│ ├── main.py

│ ├── data_processing.py

│ ├── model_training.py

│ ├── metrics.py

│ ├── requirements.txt

│ └── README.md

│

├── features/

│ ├── main.py

│ ├── data_collection.py

│ ├── feature_extraction.py

│ ├── helper_functions.py

│ ├── requirements.txt

│ └── README.md

│

├── main.py

├── README.md

└── requirements.txt


### 1. Diretório `model/`

Este diretório contém scripts relacionados ao treinamento e avaliação de modelos de machine learning. O fluxo de trabalho típico envolve:

- Carregamento e processamento dos dados.
- Treinamento de diferentes classificadores.
- Avaliação dos modelos utilizando métricas como acurácia, FAR, FRR e F1-score.
- Documentação detalhada no arquivo `README.md` dentro do diretório.

**Arquivos principais:**

- `main.py`: Script principal que orquestra o fluxo de treinamento e avaliação.
- `data_processing.py`: Funções para carregar e dividir os dados.
- `model_training.py`: Funções para treinar modelos específicos.
- `metrics.py`: Funções para calcular e retornar métricas dos modelos.
- `requirements.txt`: Lista de dependências necessárias.
- `README.md`: Documentação específica do diretório.


### 2. Diretório `features/`

Este diretório contém scripts para a coleta, preparação e extração de features a partir dos dados brutos. A extração de features visa preparar os dados para os modelos de machine learning.

**Arquivos principais:**

- `data_collection.py`: Script para coleta e preparação dos dados.
- `feature_extraction.py`: Responsável pela extração das features dos dados coletados.
- `helper_functions.py`: Funções auxiliares para normalização e salvamento das features extraídas.
- `main.py`: Script principal que orquestra a execução dos outros scripts de features.
- `requirements.txt`: Lista de dependências necessárias.
- `README.md`: Documentação específica do diretório.

## Como Executar

1. **Executar Scripts de Features**:
   - Navegue até o diretório `features/`.
   - Execute o script `main.py` para iniciar o processo de coleta e extração de features.

2. **Treinamento de Modelos**:
   - Navegue até o diretório `model/`.
   - Execute o script `main.py` para iniciar o treinamento e avaliação dos modelos.

Obs: Opicionalmente pode-se executar o método main.py presente na raiz do projeto, ele visa executar o script de features e o treinamento do modelo.

## Dependências

Cada subdiretório possui seu próprio arquivo `requirements.txt` listando as dependências necessárias. Utilize o comando abaixo dentro de cada diretório para instalar as dependências:

`pip install -r requirements.txt

## Documentação
Documentação detalhada para cada parte do projeto pode ser encontrada nos respectivos arquivos README.md dentro dos diretórios model/ e features/.

## Contribuindo
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob os termos da MIT License.
