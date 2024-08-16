import json
import polars as pl
import pandas as pd

def collect_data(file_path):
    """
    Coleta e organiza dados de um arquivo CSV para formar três DataFrames distintos:
    teclado, mouse e comportamento.

    Parâmetros:
    file_path (str): Caminho para o arquivo CSV contendo os dados.

    Retorna:
    tuple: Três DataFrames (df_key, df_mou, df_beh) contendo dados de teclado, mouse e comportamento, respectivamente.
    """
    df_datas = pl.read_csv(file_path)
    df_datas = df_datas.drop("id_sample")

    l_key, l_mou, l_beh = [], [], []
    session = 1

    for loop in range(0, len(df_datas)):
        user = df_datas['user'][loop]

        l_key = process_keyboard_data(df_datas, loop, session, user, l_key)
        l_mou = process_mouse_data(df_datas, loop, session, user, l_mou)
        l_beh = process_behavior_data(df_datas, loop, session, user, l_beh)
        
        print("Amostra ", session, " do user ", user, " carregada!")
        session += 1

    df_key = pd.DataFrame(l_key)
    df_mou = pd.DataFrame(l_mou)
    df_beh = pd.DataFrame(l_beh)

    return df_key, df_mou, df_beh

def process_keyboard_data(df_datas, loop, session, user, l_key):
    """
    Processa os dados de teclado de uma amostra específica e adiciona os registros à lista fornecida.

    Parâmetros:
    df_datas (DataFrame): DataFrame contendo todos os dados brutos.
    loop (int): Índice atual no loop de processamento.
    session (int): Número da sessão (amostra) atual.
    user (str): Identificador do usuário.
    l_key (list): Lista de registros de teclado acumulados.

    Retorna:
    list: Lista atualizada com os registros de teclado processados.
    """    

    objeto = json.loads(df_datas['dig'][loop])

    for k in range(1, len(objeto) + 1):
        registro = {
            'key_name': objeto[str(k)]['M']['tecla']['S'],
            'position': objeto[str(k)]['M']['pos']['S'],
            'event': objeto[str(k)]['M']['evento']['S'],
            'input': objeto[str(k)]['M']['campo']['N'],
            'epoch': objeto[str(k)]['M']['epoch']['N'],
            'timestamp': objeto[str(k)]['M']['ts']['S'],
            'session': session,
            'user': user
        }
        l_key.append(registro)
    return l_key

def process_mouse_data(df_datas, loop, session, user, l_mou):
    """
    Processa os dados de mouse de uma amostra específica e adiciona os registros à lista fornecida.

    Parâmetros:
    df_datas (DataFrame): DataFrame contendo todos os dados brutos.
    loop (int): Índice atual no loop de processamento.
    session (int): Número da sessão (amostra) atual.
    user (str): Identificador do usuário.
    l_mou (list): Lista de registros de mouse acumulados.

    Retorna:
    list: Lista atualizada com os registros de mouse processados.
    """

    objeto = json.loads(df_datas['mou'][loop])

    for m in range(1, len(objeto) + 1):
        registro = {
            'coordenadas': objeto[str(m)]['M']['coord']['S'],
            'event': objeto[str(m)]['M']['event_m']['S'],
            'epoch': objeto[str(m)]['M']['epoch_m']['N'],
            'timestamp': objeto[str(m)]['M']['ts_m']['S'],
            'session': session,
            'user': user
        }
        l_mou.append(registro)
    return l_mou

def process_behavior_data(df_datas, loop, session, user, l_beh):
    """
    Processa os dados de comportamento de uma amostra específica e adiciona os registros à lista fornecida.

    Parâmetros:
    df_datas (DataFrame): DataFrame contendo todos os dados brutos.
    loop (int): Índice atual no loop de processamento.
    session (int): Número da sessão (amostra) atual.
    user (str): Identificador do usuário.
    l_beh (list): Lista de registros de comportamento acumulados.

    Retorna:
    list: Lista atualizada com os registros de comportamento processados.
    """

    objeto = json.loads(df_datas['comp'][loop])

    for b in range(1, len(objeto) + 1):
        registro = {
            'order': objeto[str(b)]['M']['ord']['S'],
            'numbers_type': objeto[str(b)]['M']['num_type']['S'],
            'uppercase_type': objeto[str(b)]['M']['up_type']['S'],
            'cnStartTs': objeto[str(b)]['M']['time_txt']['M']['txtNum']['M']['Started']['M']['Timestamp']['S'],
            'cnStartE': objeto[str(b)]['M']['time_txt']['M']['txtNum']['M']['Started']['M']['Epoch']['N'],
            'cnFinishTs': objeto[str(b)]['M']['time_txt']['M']['txtNum']['M']['Finished']['M']['Timestamp']['S'],
            'cnFinishE': objeto[str(b)]['M']['time_txt']['M']['txtNum']['M']['Finished']['M']['Epoch']['N'],
            'scStartTs': objeto[str(b)]['M']['time_txt']['M']['txtCVC']['M']['Started']['M']['Timestamp']['S'],
            'scStartE': objeto[str(b)]['M']['time_txt']['M']['txtCVC']['M']['Started']['M']['Epoch']['N'],
            'scFinishTs': objeto[str(b)]['M']['time_txt']['M']['txtCVC']['M']['Finished']['M']['Timestamp']['S'],
            'scFinishE': objeto[str(b)]['M']['time_txt']['M']['txtCVC']['M']['Finished']['M']['Epoch']['N'],
            'mStartTs': objeto[str(b)]['M']['time_txt']['M']['txtMes']['M']['Started']['M']['Timestamp']['S'],
            'mStartE': objeto[str(b)]['M']['time_txt']['M']['txtMes']['M']['Started']['M']['Epoch']['N'],
            'mFinishTs': objeto[str(b)]['M']['time_txt']['M']['txtMes']['M']['Finished']['M']['Timestamp']['S'],
            'mFinishE': objeto[str(b)]['M']['time_txt']['M']['txtMes']['M']['Finished']['M']['Epoch']['N'],
            'yStartTs': objeto[str(b)]['M']['time_txt']['M']['txtAno']['M']['Started']['M']['Timestamp']['S'],
            'yStartE': objeto[str(b)]['M']['time_txt']['M']['txtAno']['M']['Started']['M']['Epoch']['N'],
            'yFinishTs': objeto[str(b)]['M']['time_txt']['M']['txtAno']['M']['Finished']['M']['Timestamp']['S'],
            'yFinishE': objeto[str(b)]['M']['time_txt']['M']['txtAno']['M']['Finished']['M']['Epoch']['N'],
            'naStartTs': objeto[str(b)]['M']['time_txt']['M']['txtNom']['M']['Started']['M']['Timestamp']['S'],
            'naStartE': objeto[str(b)]['M']['time_txt']['M']['txtNom']['M']['Started']['M']['Epoch']['N'],
            'naFinishTs': objeto[str(b)]['M']['time_txt']['M']['txtNom']['M']['Finished']['M']['Timestamp']['S'],
            'naFinishE': objeto[str(b)]['M']['time_txt']['M']['txtNom']['M']['Finished']['M']['Epoch']['N'],
            'formStartTs': objeto[str(b)]['M']['time_form']['M']['Started']['M']['Timestamp']['S'],
            'formStartE': objeto[str(b)]['M']['time_form']['M']['Started']['M']['Epoch']['N'],
            'formFinishTs': objeto[str(b)]['M']['time_form']['M']['Finished']['M']['Timestamp']['S'],
            'formFinishE': objeto[str(b)]['M']['time_form']['M']['Finished']['M']['Epoch']['N'],
            'session': session,
            'user': user
        }
        l_beh.append(registro)
    return l_beh
