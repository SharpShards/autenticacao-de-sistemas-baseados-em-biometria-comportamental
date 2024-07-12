# Importar bibliotecas
## Manipular arquivo com dados coletados
import pandas as pd
## Manipular timestamp e epoch
from datetime import datetime as dt
## Plotar dados
import matplotlib as plt
## Gerar sequências numéricas
import numpy as np
## Usar funções matemáticas
import math
## Machine Learning
from sklearn.svm import OneClassSVM as svm
## Calcular accuracy
from sklearn import metrics
## Calcular FAR e FRR
from sklearn.metrics import confusion_matrix as cm

"""## Coleta Dados"""

# Recebe arquivos e converte em DataFrames
file = pd.read_csv('user.csv')
df_user = pd.DataFrame(data = file)
df_user = df_user.set_index('id_user')

file = pd.read_csv('keyboard.csv')
df_key = pd.DataFrame(data = file)
df_key = df_key.set_index('id_keyb')

file = pd.read_csv('mouse.csv')
df_mou = pd.DataFrame(data = file)
df_mou = df_mou.set_index('id_mouse')

file = pd.read_csv('behavior.csv')
df_beh = pd.DataFrame(data = file)
df_beh = df_beh.set_index('id_beh')

file = pd.read_csv('sample.csv')
df_sam = pd.DataFrame(data = file)
df_sam.set_index('id_sample', inplace = True)

# Usuários: Lucas (1), Agda (24), Malkai (27), Jose W (25), Lara (28), Augusto (26) e Gabriel (29)
# Quantidade: 10

# Ajustar quais amostras serão usadas
df_sam = df_sam.loc[
    (df_sam['id_session'] <= 10) | # Eu 1 (10)
    ((df_sam['id_session'] >= 61) & (df_sam['id_session'] <= 115)) | # Agda (10), Malkai (8), Jose W (10), Lara (10), Augusto (2) e Gabriel (10)
    ((df_sam['id_session'] >= 116) & (df_sam['id_session'] <= 123)) | # Augusto (8)
    ((df_sam['id_session'] >= 139) & (df_sam['id_session'] <= 140)) # Malkai (2)
                    ]

"""## Processamento

### Tempo Pressionando A Mesma Tecla
"""

## Declaração
times_press = {}

## Roda todas as amostras
for samp in df_sam['id_session'].unique():
  ## Declara user
  user = df_sam.loc[df_sam['id_session'] == samp, 'id_user'].values[0]

  ## Starta user
  if('Usuário ' + str(user) not in times_press):
    times_press['Usuário ' + str(user)] = {}

  ## Starta dict
  if("Amostra" + str(samp) not in times_press['Usuário ' + str(user)]):
    times_press['Usuário ' + str(user)]['Amostra ' + str(samp)] = {}

  ## Gera sub-dataframe com dados da amostra
  cond = (df_sam['id_session'] == samp) & (df_sam['id_data_key'] != 0)
  df_sub = df_sam[cond]
  ### Ordena os registros
  ### Por algum motivo foram salvos no banco invertido
  df_sub = df_sub.sort_index()

  ## Separa em pares de teclas.
  for loop in df_sub.index:
    ## Se o dado for referente a tecla down.
    if(df_key.loc[df_sub.loc[loop]['id_data_key']]['event'] == 'keydown'):
      time_down = df_key.loc[df_sub.loc[loop]['id_data_key']]['epoch']

      ## Buscar par referente a tecla up.
      control = int(df_sub.loc[loop]['id_data_key']) ## id da tecla down.

      for busca in df_sub['id_data_key']: ## Começa a contar após a posição da tecla down
        ## Se a tecla for da mesma posição, mas for up.
        if(busca > control):
          if(df_key.loc[busca]['position'] == df_key.loc[df_sub.loc[loop]['id_data_key']]['position']
          and df_key.loc[busca]['event'] == 'keyup'):
            time_up = df_key.loc[busca]['epoch']
            break

      ## Salvar tempos
      times_press['Usuário ' + str(user)]['Amostra ' + str(samp)][len(times_press['Usuário ' + str(user)]['Amostra ' + str(samp)]) + 1] = [df_key.loc[df_sub.loc[loop]['id_data_key']]['key_name'], (time_up - time_down)]

  ## Retira última tecla por erro na coleta.
  times_press['Usuário ' + str(user)]['Amostra ' + str(samp)].pop(len(times_press['Usuário ' + str(user)]['Amostra ' + str(samp)]))

times_press

"""### Tempo Entre Teclas Diferentes"""

## Declaração
quant = 0

times = {}

down = {}
up = {}

ord = {}

key = 0
pairs = {}

## Roda todas as amostras
for samp in df_sam['id_session'].unique():
  ## Gera sub-dataframe da amostra
  df_sub = df_sam[(df_sam['id_session'] == samp) & (df_sam['id_data_key'] != 0)]
  ### Ordena os registros
  ### Por algum motivo foram salvos no banco invertido
  df_sub = df_sub.sort_index()

  ## Declara user
  user = df_sub.loc[df_sam['id_session'] == samp, 'id_user'].values[0]

  ## Starta user
  if('Usuário ' + str(user) not in times):
    times['Usuário ' + str(user)] = {}

  ## Starta dict
  if("Amostra" + str(samp) not in times['Usuário ' + str(user)]):
    times['Usuário ' + str(user)]['Amostra ' + str(samp)] = {}

  ## Calcula o tempo entre as teclas
  for inp in range(1,6): ## Divide as análises em campos
    quant = 0

    first = 0
    last = 0

    ## Separa em teclas down e up
    for loop in df_sub['id_data_key']:
      if((df_key.loc[loop]['event'] == 'keydown') and (df_key.loc[loop]['input'] == inp)):
        down[loop] = [df_key.loc[loop]['position'], df_key.loc[loop]['input'], df_key.loc[loop]['epoch']]

        ord[quant] = df_key.loc[loop]['position']

        ## Determinar a ordem das teclas
        if(first == 0):
          first = loop ### Salva a chave do primeiro item
        else:
          quant += 1
      elif((df_key.loc[loop]['event'] == 'keyup') and ((df_key.loc[loop]['input'] == inp))):
        up[loop] = [df_key.loc[loop]['position'], df_key.loc[loop]['input'], df_key.loc[loop]['epoch']]
        last = loop ### Salva a chave do último item

    ## Deletando valores que não serão usados
    del down[first]
    del up[last]

    ## Calcula o tempo
    quant = 0

    for loop in df_sub['id_data_key']:
      ## Busca as teclas
      if(loop in up):
        first = up[loop][2]

        for busca in down:
          if(down[busca][0] == ord[quant]):
            second = down[busca][2]
            break

        quant += 1

        ## Colocar 'quant' no index, senão, caso as duas teclas up e down sejam
        ## iguais a outras no mesmo campo e na mesma amostra, ele substitui
        times['Usuário ' + str(user)]['Amostra ' + str(samp)][str(up[loop][0] + ' > ' + str(down[busca][0])) + ' ('+ str(quant) +')' + ' ('+ str(inp) +')'] = (second - first)/1000

        ## Registra pares para próxima feature
        key += 1
        pairs[key] = {'user' : user, 'sample' : samp, 'input' : inp, 'pair' : [str(up[loop][0]), str(down[busca][0])], 'time' : (second - first)/1000}

        # Deleta o que já foi usado. Se não, caso a tecla seja igual, ela pega a epoch
        # da tecla que já foi usada.
        up.pop(loop)
        down.pop(busca)

  # Zerando pra que uma amostra não afete outra
  up = {}
  down = {}

times

"""## Features"""

# Inicialização Data-Frame com features
df_fea = pd.DataFrame(data = df_sam['id_session'].unique())
df_fea.rename(columns={0 : 'Amostra'}, inplace=True)
df_fea.set_index('Amostra',inplace=True)

# Atribuindo labels
## Criando coluna
df_fea['label'] = 0

## Relacionando labels às amostras
for loop in df_fea.index:
  df_fea.loc[loop]['label'] = df_sam.loc[df_sam['id_session'] == loop, 'id_user'].values[0]

"""### Duração"""

## Declaração
t = []

max = 0
min = 0
mea = 0
med = 0
std = 0

## Roda por todas as amostras
for sample in df_sam['id_session'].unique():
  ## Declara user
  user = df_sam.loc[df_sam['id_session'] == sample, 'id_user'].values[0]

  ## Pega só os tempos e salva em t
  for loop in times_press['Usuário ' + str(user)]['Amostra ' + str(sample)]:
    t.append(int(times_press['Usuário ' + str(user)]['Amostra ' + str(sample)][loop][1]))

  ## Gera Serie
  t = pd.Series(t)

  ## Cálculos
  ### Máximo
  max = t.max()
  ### Mínimo
  min = t.min()
  ### Média
  mea = round(t.mean(), 2)
  ### Mediana
  med = round(t.median(), 2)
  ### Desvio Padrão
  std = round(t.std(), 2)

  df_fea.loc[sample, 'press_max'] = max
  df_fea.loc[sample, 'press_min'] = min
  df_fea.loc[sample, 'press_mea'] = mea
  df_fea.loc[sample, 'press_med'] = med
  df_fea.loc[sample, 'press_std'] = std

  ## Volta t para uma lista normal para poder usar append.
  t =  []

"""### Distância"""

## Declarações
keyboard = {
    1: {2: 'Digit1', 3: 'Digit2', 4: 'Digit3', 5: 'Digit4', 6: 'Digit5', 7: 'Digit6', 8: 'Digit7', 9: 'Digit8', 10: 'Digit9', 11: 'Digit0', 14: 'Backspace', 15: 'Backspace'},
    2: {1: 'Tab', 2: 'KeyQ', 3: 'KeyW', 4: 'KeyE', 5: 'KeyR', 6: 'KeyT', 7: 'KeyY', 8: 'KeyU', 9: 'KeyI', 10: 'KeyO', 11: 'KeyP', 14: 'Enter', 15: 'Enter', 21: 'Numpad7', 22: 'Numpad8', 23: 'Numpad9'},
    3: {1: 'CapsLock', 2: 'KeyA', 3: 'KeyS', 4: 'KeyD', 5: 'KeyF', 6: 'KeyG', 7: 'KeyH', 8: 'KeyJ', 9: 'KeyK', 10: 'KeyL', 11: 'KeyÇ', 14: 'Enter', 15: 'Enter', 21: 'Numpad4', 22: 'Numpad5', 23: 'Numpad6'},
    4: {1: 'ShiftLeft', 3: 'KeyZ', 4: 'KeyX', 5: 'KeyC', 6: 'KeyU', 7: 'KeyB', 8: 'KeyN', 9: 'KeyM', 14: 'ShiftRight', 15: 'ShiftRight', 21: 'Numpad1', 22: 'Numpad2', 23: 'Numpad3', 24: 'Enter'},
    5: {5: 'Space', 6: 'Space', 7: 'Space', 8: 'Space', 9: 'Space', 10: 'Space', 21: '0', 22: '0', 23: 'Enter'},
}

release = []
press = []

ds = {}

rel = False
pre = False

quant = 0

### Encontrar cada par
for k in pairs:
  ### Encontra pares no mapa
  for loop in keyboard:
    for subloop in keyboard[loop]:
      ### Os Falses são pra indicar que encontrou um par e não vai precisar mais entrar aqui
      if((keyboard[loop][subloop] == pairs[k]['pair'][0]) and (rel == False)):
        release = [pairs[k]['pair'][0], [loop, subloop]]
        rel = True

      if((keyboard[loop][subloop] == pairs[k]['pair'][1]) and (pre == False)):
        press = [pairs[k]['pair'][1], [loop, subloop]]
        pre = True

  ### Salva coordenadas
  pairs[k]['coord'] = {'release' : release[1], 'press' : press[1]}
  quant += 1

  ### Zera pra ele poder entrar pra procurar os outros pares
  rel = False
  pre = False

## Calcular Distância
### Declaração
clusters = {}

### Calcula a distância entre as teclas
for loop in pairs:
  ### MOD(x release - x press) + MOD(y release - y press)
  distance = abs((pairs[loop]['coord']['release'][0] - pairs[loop]['coord']['press'][0])) + abs((pairs[loop]['coord']['release'][1] - pairs[loop]['coord']['press'][1]))

  ### Substitui as coordenadas pela distância
  pairs[loop]['d'] = str(distance)

## Calcular Feature
ds = {}

### Separa os tempos em cada distância respectiva
for loop in df_sam['id_user'].unique():  ### Por usuários
    for subloop in pairs:
      ### Declaração
      user = 'Usuário ' + str(pairs[subloop]['user'])
      sam = pairs[subloop]['sample']
      d = pairs[subloop]['d']

      ### Startar user
      if(user not in ds):
        ds[user] = {}

      ### Startar amostra
      if(sam not in ds[user]):
        ds[user][sam] = {}

      ### Startar d
      if(d not in ds[user][sam]):
        ds[user][sam][d] = {}

      ### Salvar time por d
      if(pairs[subloop]['user'] == loop):
        ds[user][sam][d][subloop] = pairs[subloop]['time']

### Features
#### Entra no cada usuário
for loop in ds:
  #### Entra em cada amostra
  for subloop in ds[loop]:
    #### Entra em cada distância e converte em Serie para calcular
    for subsubloop in ds[loop][subloop]:
      s = pd.Series(ds[loop][subloop][subsubloop])

      #### Cálculos
      ##### Máximo
      max = s.max()
      ##### Média
      mea = round(s.mean(), 2)
      ##### Mediana
      med = round(s.median(), 2)
      ##### Variação
      var = round(s.var(), 2)
      ### Desvio Padrão
      std = round(s.std(), 2)
      ### Desvio Médio absoluto
      mad = round((s - mea).abs().mean(), 2)

      df_fea.loc[subloop, str('d' + subsubloop + '_max')] = max
      df_fea.loc[subloop, str('d' + subsubloop + '_mea')] = mea
      df_fea.loc[subloop, str('d' + subsubloop + '_med')] = med
      df_fea.loc[subloop, str('d' + subsubloop + '_var')] = var
      df_fea.loc[subloop, str('d' + subsubloop + '_std')] = std
      df_fea.loc[subloop, str('d' + subsubloop + '_mad')] = mad

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df_fea

"""## Classificação"""

# Declaração
result = []
stt = {}

# Ajuste
df_fea = df_fea.fillna(0)

# Separar dataframes entre teste e treino
## 70% treino e 30% teste

# Calcular Accuracy
for loop in df_fea['label'].unique():
## Amostras para Teste
  df_test = df_fea[((df_fea['label'] == 1) & ((df_fea.index >= 8) & (df_fea.index <= 10))) | # Eu
                  (df_fea['label'] == 24) & ((df_fea.index == 82) | (df_fea.index == 83) | (df_fea.index == 84)) | # Agda
                  ((df_fea['label'] == 26) & ((df_fea.index == 63) | (df_fea.index == 66) | (df_fea.index == 116))) | # Augusto
                  ((df_fea['label'] == 27) & ((df_fea.index == 67) | (df_fea.index == 139) | (df_fea.index == 140))) | # Malkai
                  ((df_fea['label'] == 25) & ((df_fea.index == 62) | (df_fea.index == 65) | (df_fea.index == 69))) | # Jose W
                  (df_fea['label'] == 28) & ((df_fea.index == 78) | (df_fea.index == 95) | (df_fea.index == 97)) | # Lara
                  (df_fea['label'] == 29) & ((df_fea.index == 85) | (df_fea.index == 86) | (df_fea.index == 87)) # Gabriel
                  ]

  ## Amostras para Treino
  if(loop == 1):
    df_train = df_fea[(df_fea['label'] == 1) & (df_fea.index <= 7)]
  elif(loop == 24):
    df_train = df_fea[(df_fea['label'] == 24) & ((df_fea.index == 61) | (df_fea.index == 64) | (df_fea.index == 68) | (df_fea.index == 77) | (df_fea.index == 79) | (df_fea.index == 80) | (df_fea.index == 81))]
  elif(loop == 26):
    df_train = df_fea[(df_fea['label'] == 26) & ((df_fea.index >= 117) | (df_fea.index <= 123))]
  elif(loop == 27):
    df_train = df_fea[(df_fea['label'] == 27) & ((df_fea.index >= 109) | (df_fea.index <= 115))]
  elif(loop == 25):
    df_train = df_fea[(df_fea['label'] == 25) & ((df_fea.index >= 70) | (df_fea.index <= 76))]
  elif(loop == 28):
    df_train = df_fea[(df_fea['label'] == 28) & ((df_fea.index >= 98) | (df_fea.index <= 104))]
  elif(loop == 29):
    df_train = df_fea[(df_fea['label'] == 29) & ((df_fea.index >= 88) | (df_fea.index <= 94))]

  ## Ajutando labels teste
  leg = df_test[df_test['label'] == loop].index
  ileg = df_test[df_test['label'] != loop].index

  df_test.loc[leg, 'label'] = 1
  df_test.loc[ileg, 'label'] = -1

  ## Separando labels do set de teste
  labels = df_test['label']
  df_test.drop(columns = 'label', inplace=True)

  ## Tirando labels do set para treino
  df_train.drop(columns = 'label', inplace=True)

  ## Modelo
  ### Criação
  modelo = svm(kernel = 'rbf', nu = 0.01)
  modelo.fit(df_train)

  ### Predição
  pred = modelo.predict(df_test)

  ### Salvar labels e predicts
  stt[loop] = {'label' : labels, 'predict' : pred}

  ### Accuracy
  acc = metrics.accuracy_score(labels, pred)
  acc = round(acc * 100, 2)

  print('Usuário ', loop,': ', acc, '%')
  print('')

  #### Acumula as accuracy
  result.append(acc)

# Accuracy final
result = round(sum(result)/len(result), 2)

print(' ')
print(' ')
print(' ')
print(' ')
print('Final: ', result, '%')
print(' ')
print(' ')
print(' ')
print(' ')

"""### Métricas"""

# Declaração
far = []
frr = []
# Calcular a matriz de confusão
for loop in stt:
  conf_matrix = cm(stt[loop]['label'].to_numpy(), stt[loop]['predict'])

  # Extrair os valores da matriz de confusão
  TN, FP, FN, TP = conf_matrix.ravel()

  # Calcular FRR e FAR
  frr.append(round(FN / (FN + TP), 2) * 100)
  far.append(round(FP / (FP + TN), 2) * 100)

frr = round(sum(frr)/len(frr))
far = round(sum(far)/len(far))

print("False Acceptance Rate (FAR):", far)
print("False Rejection Rate (FRR):", frr)
print(' ')
print(' ')