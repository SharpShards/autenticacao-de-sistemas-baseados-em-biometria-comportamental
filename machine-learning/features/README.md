# Extração de Features de Sessões de Teclado e Mouse

Este projeto é voltado para a coleta, processamento e extração de features de dados coletados durante sessões de uso de teclado e mouse. O objetivo é transformar esses dados em um formato que pode ser utilizado para análises subsequentes, como a classificação de padrões de uso.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

features/

│

├── data_collection.py # Script para coleta e preparação dos dados

├── feature_extraction.py # Script para extração de features

├── helper_functions.py # Funções auxiliares para normalização e salvamento

├── main.py # Script principal para orquestrar a execução

├── requirements.txt # Lista de dependências do projeto

└── README.md # Documentação do projeto


### Dependências

O projeto utiliza as seguintes bibliotecas Python:

- `pandas`
- `polars`
- `numpy`
- `scikit-learn`

Você pode instalar todas as dependências utilizando o comando:

`pip install -r requirements.txt


### Arquivos Principais
data_collection.py: Contém funções para carregar os dados a partir de um arquivo CSV e extrair as sessões de uso do teclado, mouse e comportamento dos usuários.

feature_extraction.py: Contém funções para processar os dados extraídos e calcular diversas features relacionadas ao uso do teclado e do mouse.

helper_functions.py: Inclui funções auxiliares como a normalização de features e o salvamento dos resultados em um arquivo Excel.

main.py: O script principal que utiliza as funções de coleta de dados e extração de features, realiza a normalização dos dados e salva o resultado final.

### Como Executar
Coloque seus dados no arquivo data/main.csv. Certifique-se de que o arquivo está formatado corretamente para ser lido pelo script.

### Execute o script principal:

`python src/main.py

Após a execução, as features extraídas e normalizadas serão salvas no arquivo results/features.xlsx.

### Como Contribuir
Se você deseja contribuir com este projeto, sinta-se à vontade para enviar pull requests ou abrir issues. Sugestões para melhorias no código, estrutura ou documentação são sempre bem-vindas.

### Licença
Este projeto é licenciado sob a Licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

### Contato
Para mais informações ou perguntas sobre este projeto, você pode entrar em contato por e-mail [lucas15azevedo@gmail.com].
