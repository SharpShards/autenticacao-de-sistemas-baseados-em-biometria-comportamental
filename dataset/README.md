# Dataset
Arquivos CSV contendo dados da interação de um grupo de usuários com seus computadores compõem o banco de dados utilizado para conduzir o estudo e permitir autenticação dos usuários a partir das amostras geradas.

## Status
- Usuários: 13
- Amostras: 100
- Total: 1300

## Perfil
Os usuários se voluntariaram para gerar as amostras e participar do estudo. Assim, possuem características e vivências diversas.
- Idade: Temos usuários de 9 a 60 anos, sem restrições.
- Gênero: 6 homens e 7 mulheres.
- Nacionalidade: Todos brasileiros.
- Costumes: Alguns utilizam o computador diariamente para trabalho, outros o utilizam ocasionalmente para lazer, e há aqueles que não têm o hábito de usar o dispositivo.

## Estrutura
Cada amostra possui cinco campos, sendo eles:
1. id_sample: Identificador único daquela amostra.
2. user: Pessoa responsável por gerar aquela amostra.
3. dig: Dados referente à interação do usuário com o teclado.
4. mou: Dados referente à interação do usuário com o mouse.
5. comp: Dados referente ao comportamento do usuário.

### Teclado
Registra cada tecla digitada pelo usuário, assim como sua posição no teclado, o campo de texto em que foi digitada, e o momento em que foi pressionada e solta. 

| Tecla | Posição | Evento | Campo | Epoch | Timestamp |
| ----- | ------- | ------ | ----- | ----- | --------- |
| Shift | ShiftLeft | keydown | 5 | 1717609253880 | 2024-06-05 14:40:53:880 |
| Shift | ShiftLeft | keyup | 5 | 1717609253952 | 2024-06-05 14:40:53:952 |

### Mouse
Monitora o cursor do mouse na interface, retornando suas coordenadas, bem como o momento em que se movimenta e pressiona ou solta o botão. 

| Coordenadas | Evento | Epoch | Timestamp |
| ----------- | ------ | ----- | --------- |
| (936, 1420) | mousemove | 1717609253880 | 2024-06-05 14:40:53:880 |
| (936, 1422) | mousemove | 1717609253952 | 2024-06-05 14:40:53:952 |
| (936, 1422) | mousedown | 1717609253961 | 2024-06-05 14:40:53:961 |
| (936, 1422) | mouseup| 1717609253987 | 2024-06-05 14:40:53:987 |

### Comportamento
Identifica preferências do usuário, como a ordem em que ele preenche os campos do formulário, quais teclas numéricas utiliza, qual tecla usa para digitar letras maiúsculas e o momento que preenche cada campo de texto e o formulário como um todo.

| Ordem | Tipo Número | Tipo Uppercase | Timestamp Início Nome | Epoch Início Nome | Timestamp Final Nome | Epoch Final Nome | ... | Timestamp Início Formulário | Epoch Início Formulário | Timestamp Final Formulário | Epoch Final Formulário |
| ----- | ----------- | ------------- | --------------------- | ----------------- | -------------------- | ---------------- | --- | --------------------------- | ----------------------- | -------------------------- | ---------------------- |
| 1-2-3-4-5 | Numpad | CapsLock | 2024-06-05 14:40:53:880 | 1717609253880 | 2024-06-05 14:40:53:880 | 1717609253880 | ... | 2024-06-05 14:40:53:880 | 1717609253880 | 2024-06-05 14:40:53:880 | 1717609253880 |
| 5-1-2-3-4 | Digit | Shift | 2024-06-05 14:40:53:952 | 1717609253952 | 2024-06-05 14:40:53:880 | 1717609253880 | ... | 2024-06-05 14:40:53:880 | 1717609253880 | 2024-06-05 14:40:53:880 | 1717609253880 |
