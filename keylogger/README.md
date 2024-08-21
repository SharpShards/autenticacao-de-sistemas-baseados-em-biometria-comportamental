# Keylogger
Software utilizado para monitorar e registrar interações do usuário com o teclado e o mouse.

## Desenvolvimento
O script foi desenvolvido de forma autônoma, autoral e personalizada. A interface, desenvolvida em HTML e CSS, é baseada em uma tela generalizada do processo
de finalização de pagamento. Um keylogger foi implementado em JavaScript no site. Assim, toda vez que o usuário movimenta o mouse ou pressiona uma
tecla, um evento é disparado e um conjunto de informações sobre ele é registrado. Esses dados são organizados e enviados por meio de uma requisição POST
para um serviço de banco de dados na nuvem da AWS, chamado DynamoDB, onde são armazenados para uso posterior.

## Implementação
Todo o código foi implementado na nuvem e pode ser executado online, como qualquer site. Não é necessário executar nenhum código desta sessão. Decidimos tornar
todo o processo online para permitir que os voluntários realizassem a coleta de forma remota e independente.

Para acessar o keylogger e gerar uma amostra, basta acessar o link: http://autenticacao-biometria-comportamental.s3-website-sa-east-1.amazonaws.com/ e interagir com
o formulário.

## Coleta
Um grupo de voluntários foi selecionado e orientado para realizar coletas constantes. 
                                                                                                                                  
Nos referimos ao processo de preencher o formulário e pressionar o botão de finalizar como "sessão". Portanto, toda vez que o usuário preenche o formulário, isso
corresponde a uma sessão. Os dados coletados em uma sessão equivalem a uma amostra, que por sua vez representa um conjunto de registros, variando entre 200 a 500 
por sessão, dependendo das ações do usuário.

Os voluntários foram instruídos a realizar múltiplas sessões consecutivas por aproximadamente 15 minutos ao dia. No formulário, o usuário deve digitar um valor
qualquer no campo de texto da área "Conversão", escolher entre Crédito e Débito na área de "Método de Pagamento" e, logo abaixo, digitar as informações do cartão
de crédito fictício apresentado no canto superior esquerdo da tela. As informações do cartão são alteradas de forma alaeatória a cada recarga da página, evitando
interferências nas amostras coletadas.

A lista completa com todas as instruções apresentadas aos voluntários está disponível no arquivo Orientações.pdf. As instruções contidas nesse arquivo são
importantes para preservar a integridade das amostras geradas.
