# Artigo WTICG 2024
Este repositório faz parte do apêndice do artigo "Autenticação de Sistemas Baseados em Biometria Comportamental", submetido para o Workshop de Trabalhos de Iniciação Científica e de Graduação do XVIII Simpósio Brasileiro em Segurança da Informação e de Sistemas Computacionais.

Resumo: "O surgimento de avanços tecnológicos evidenciam a necessidade de métodos de segurança mais avançados para garantir a privacidade de dispositivos pessoais. Na literatura, o uso de keystroke ainda é pouco explorado, principalmente utilizando multi-modal fatores. Neste trabalho, propomos um método de monitoramento de teclados e mouses para análise da interação de usuários com seus dispositivos. Features são extraídas dos keystrokes e analisadas utilizando Machine Learning, nos permitindo determinar se o usuário é de fato o usuário legítimo. Os experimentos retornaram bons resultados com o Random Forest."

## Componentes
- Keylogger: Site utilizado para coletar as amostras utilizadas no artigo.
- Orientações: Arquivo enviado para os voluntários com instruções de como produzir as amostras.
- Dataset: Arquivo com amostras usadas para alcançar os resultados apresentados.
- Machine Learning: Código com todas as etapas necessárias para chegar aos resultados apresentados.

## Resumo
Neste repositório apresentamos as etapas para reproduzir os resultados iniciais apresentados no artigo: a instalação de ferramentas e da linguagem Python, a importação de bibliotecas Python e a simulação dos resultados através do código no arquivo Python.

O README apresenta informações de (i) Como instalar a IDE e o Python; (ii) Como importar as bibliotecas Python utilizadas no código; (iii) Como simular o treinamento e teste do modelo de amchine learning.

### Instalações
A IDE utilizada foi o Visual Studio Code (VSCode) e pode ser instalada atravé do site: https://code.visualstudio.com/download

A linguagem de programação Python também deve ser baixada no site: https://www.python.org/downloads/

Uma vez que ambos o VSCode e o Python estejam instalados, também intale, dentro do VSCode, a extensão Python oferecida pela Microsoft.

### Importações
No terminal do VSCode, insira as seguintes linhas para importar as bibliotecas necessárias.
- pip install pandas
- pip install matplotlib
- pip install numpy
- pip install scikit-learn

### Simulação
Com as ferramentas e bibliotecas necessárias instaladas, basta iniciar um "Run and Debug" que o código será executado e os resultados serão apresentados no terminal.

Atualmente, a simulação está gerando os resultados esperados e apresentados no artigo. Com algumas pequenas mudanças positivas: o Usuário 3 passou a apresentar uma accuracy de 76% e o FRR alcançou 24%.
