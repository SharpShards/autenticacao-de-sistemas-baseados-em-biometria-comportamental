# Artigo WTICG 2024
Este repositório faz parte do apêndice do artigo "Autenticação de Sistemas Baseados em Biometria Comportamental", submetido para o Workshop de Trabalhos de Iniciação Científica e de Graduação do XVIII Simpósio Brasileiro em Segurança da Informação e de Sistemas Computacionais.

Resumo: "O surgimento de avanços tecnológicos demanda métodos de segurança cada vez mais sofisticados para proteger dispositivos pessoais. A utilização de keystrokes para identificação biométrica é promissora, mas ainda pouco explorada, especialmente em sistemas biométricos multimodais. Neste trabalho, propomos um método para monitorar e analisar as interações do usuário com seus dispositivos, extraindo características únicas a partir de keystrokes e utilizando aprendizado de máquina para verificar a identidade do usuário. Nossos experimentos com Random Forest, SVM, KNN e Regressão Logística obtiveram taxas de acurácia superiores a 99%."

## Componentes
- Keylogger: Software utilizado para monitorar e coletar as amostras utilizadas no artigo.
- Dataset: Arquivo com amostras usadas para alcançar os resultados apresentados.
- Machine Learning: Código para autenticação biométrica e com todas as etapas necessárias para chegar aos resultados apresentados.

## Resumo
Neste repositório apresentamos as etapas para reproduzir os resultados iniciais apresentados no artigo: a instalação de ferramentas e da linguagem Python, a importação de bibliotecas Python e a simulação dos resultados através do código no arquivo Python.

O README apresenta informações de (i) Requisitos mínimos do sistema para executar o código; (ii) Como instalar a IDE e o Python; (iii) Como importar as bibliotecas Python utilizadas no código; (iv) Como simular o treinamento e teste do modelo de amchine learning.

### Requisitos de Sistema
- Sistema Operacional: Windows 10
- Processador: Intel Core i3
- Memória RAM: 4GB
- Armazenamento: 100MB de espaço disponível

### Instalações
A IDE utilizada foi o Visual Studio Code (VSCode) e pode ser instalada atravé do site: https://code.visualstudio.com/download

A linguagem de programação Python também deve ser baixada no site: https://www.python.org/downloads/. Recomenda-se a instalação do Python 3, independentemente da versão. A versão utilizada neste estudo foi a Python 3.9.

Uma vez que ambos o VSCode e o Python estejam instalados, também intale e configure a extensão Python oferecida pela Microsoft para executar o código. Um passo a passo pode ser encontrado no site: https://marketplace.visualstudio.com/items?itemName=ms-python.python

### Simulação
Com as ferramentas e bibliotecas necessárias instaladas, basta iniciar um "Run and Debug" no arquivo main.py da pasta machine-learning, e o código será executado, gerando os resultados da autenticação.
