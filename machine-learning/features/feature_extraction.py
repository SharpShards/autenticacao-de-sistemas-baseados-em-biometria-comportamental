import pandas as pd
import math
from collections import deque
from sklearn.preprocessing import MinMaxScaler as mms

def extract_features(df_key, df_mou, df_beh):
    """
    Extrai e calcula as features dos dados de teclado, mouse e comportamento.

    Parâmetros:
    df_key (DataFrame): DataFrame contendo os dados de teclado.
    df_mou (DataFrame): DataFrame contendo os dados de mouse.
    df_beh (DataFrame): DataFrame contendo os dados de comportamento.

    Retorna:
    DataFrame: DataFrame contendo as features extraídas.
    """

    df_fea = pd.DataFrame(data=df_key['session'].unique())
    df_fea.rename(columns={0: 'Amostra'}, inplace=True)
    df_fea.set_index('Amostra', inplace=True)

    assign_labels(df_fea, df_key)
    calculate_keyboard_features(df_fea, df_key)
    calculate_mouse_features(df_fea, df_mou)
    calculate_behavior_features(df_fea, df_key, df_mou, df_beh)

    return df_fea

def assign_labels(df_fea, df_key):
    """
    Atribui rótulos (labels) às amostras no DataFrame de features.

    Parâmetros:
    df_fea (DataFrame): DataFrame onde as labels serão atribuídas.
    df_key (DataFrame): DataFrame contendo as informações de labels associadas às sessões.
    """

    df_fea['label'] = ""
    for loop in df_fea.index:
        df_fea.loc[loop]['label'] = df_key.loc[df_key['session'] == loop, 'user'].unique()[0]

def calculate_keyboard_features(df_fea, df_key):
    """
    Calcula as features relacionadas ao uso do teclado, incluindo tempo entre teclas, tempo pressionando teclas,
    e a distância entre as teclas pressionadas.

    Parâmetros:
    df_fea (DataFrame): DataFrame onde as features serão armazenadas.
    df_key (DataFrame): DataFrame contendo os dados de teclado.
    """

    # Inicialização de pares
    pairs = {}
    key = 0
    down = deque()

    # Teclado - Tempo Entre Teclas Diferentes
    quant = 1
    times = {}
    for samp in df_key['session'].unique():
        df_sam = df_key[df_key['session'] == samp]
        user = df_sam.loc[df_sam['session'] == samp, 'user'].values[0]

        if user not in times:
            times[user] = {}

        if "Amostra " + str(samp) not in times[user]:
            times[user]['Amostra ' + str(samp)] = {}

        for inp in range(1, 6):  # Divide as análises em campos
            df_sub = df_sam[df_sam["input"] == str(inp)]

            for loop in df_sub.index:
                if ((df_sub.loc[loop]['event'] == 'keydown') and (df_sub.loc[loop]['epoch'] != df_sub.iloc[0]['epoch']) and
                   ((df_key.loc[loop - 1]['event'] != 'keydown') or (df_key.loc[loop]['position'] != df_key.loc[loop - 1]['position']))):
                    down.append([df_sub.loc[loop]['position'], df_sub.loc[loop]['epoch']])

            for loop in df_sub.index:
                if len(down) > 0 and df_sub.loc[loop]["event"] == "keyup":
                    first = df_sub.loc[loop]["epoch"]
                    second = down[0][1]

                    times[user]['Amostra ' + str(samp)][str(df_sub.loc[loop]["position"] + ' > ' + down[0][0]) + ' ('+ str(quant) +')' + ' ('+ str(inp) +')'] = (int(second) - int(first))
                    quant += 1

                    key += 1
                    pairs[key] = {
                        'user': user,
                        'sample': samp,
                        'input': inp,
                        'pair': [down[0][0], df_sub.loc[loop]["position"]],
                        'time': (int(second) - int(first))
                    }
                    down.popleft()

            quant = 1
            down = deque()

    # Teclado - Tempo Pressionando A Mesma Tecla
    time_press = {}
    for samp in df_key['session'].unique():
        user = df_key.loc[df_key['session'] == samp, 'user'].values[0]

        if user not in time_press:
            time_press[user] = {}

        if "Amostra " + str(samp) not in time_press[user]:
            time_press[user]['Amostra ' + str(samp)] = {}

        cond = df_key['session'] == samp
        df_sub = df_key[cond]

        for loop in df_sub.index:
            if ((df_sub.loc[loop]['event'] == 'keydown' and loop != df_sub.index[-1]) and
               (df_sub.loc[loop + 1]['event'] != 'keydown' or df_sub.loc[loop + 2]['event'] != 'keydown')):
                time_down = df_sub.loc[loop]['epoch']

                control = loop
                for busca in df_sub.index:
                    if busca > control:
                        if (df_sub.loc[busca]['position'] == df_sub.loc[loop]['position'] and
                            df_sub.loc[busca]['event'] == 'keyup'):
                            time_up = df_sub.loc[busca]['epoch']
                            break

                time_press[user]['Amostra ' + str(samp)][len(time_press[user]['Amostra ' + str(samp)]) + 1] = [
                    df_sub.loc[loop]['key_name'], (int(time_up) - int(time_down))
                ]

    # Teclado - Duração
    t = []
    for sample in df_key['session'].unique():
        user = df_key.loc[df_key['session'] == sample, 'user'].values[0]

        for loop in time_press[user]['Amostra ' + str(sample)]:
            t.append(int(time_press[user]['Amostra ' + str(sample)][loop][1]))

        t = pd.Series(t)

        df_fea.loc[sample, 'press_max'] = t.max()
        df_fea.loc[sample, 'press_min'] = t.min()
        df_fea.loc[sample, 'press_mea'] = round(t.mean(), 2)
        df_fea.loc[sample, 'press_med'] = round(t.median(), 2)
        df_fea.loc[sample, 'press_std'] = round(t.std(), 2)

        t = []

    # Teclado - Distância
    keyboard = {
        1: {2: 'Digit1', 3: 'Digit2', 4: 'Digit3', 5: 'Digit4', 6: 'Digit5', 7: 'Digit6', 8: 'Digit7', 9: 'Digit8', 10: 'Digit9', 11: 'Digit0', 14: 'Backspace', 15: 'Backspace'},
        2: {1: 'Tab', 2: 'KeyQ', 3: 'KeyW', 4: 'KeyE', 5: 'KeyR', 6: 'KeyT', 7: 'KeyY', 8: 'KeyU', 9: 'KeyI', 10: 'KeyO', 11: 'KeyP', 14: 'Enter', 15: 'Enter', 21: 'Numpad7', 22: 'Numpad8', 23: 'Numpad9'},
        3: {1: 'CapsLock', 2: 'KeyA', 3: 'KeyS', 4: 'KeyD', 5: 'KeyF', 6: 'KeyG', 7: 'KeyH', 8: 'KeyJ', 9: 'KeyK', 10: 'KeyL', 11: 'KeyÇ', 14: 'Enter', 15: 'Enter', 21: 'Numpad4', 22: 'Numpad5', 23: 'Numpad6'},
        4: {1: 'ShiftLeft', 3: 'KeyZ', 4: 'KeyX', 5: 'KeyC', 6: 'KeyU', 7: 'KeyB', 8: 'KeyN', 9: 'KeyM', 14: 'ShiftRight', 15: 'ShiftRight', 21: 'Numpad1', 22: 'Numpad2', 23: 'Numpad3', 24: 'Enter'},
        5: {5: 'Space', 6: 'Space', 7: 'Space', 8: 'Space', 9: 'Space', 10: 'Space', 21: '0', 22: '0', 23: 'Enter'},
    }

    release, press = [], []
    ds, rel, pre = {}, False, False

    for k in pairs:
        for loop in keyboard:
            for subloop in keyboard[loop]:
                if ((keyboard[loop][subloop] == pairs[k]['pair'][0]) and (rel == False)):
                    release = [pairs[k]['pair'][0], [loop, subloop]]
                    rel = True

                if ((keyboard[loop][subloop] == pairs[k]['pair'][1]) and (pre == False)):
                    press = [pairs[k]['pair'][1], [loop, subloop]]
                    pre = True

        pairs[k]['coord'] = {'release': release[1], 'press': press[1]}

        rel, pre = False, False

    clusters = {}
    for loop in pairs:
        distance = abs((pairs[loop]['coord']['release'][0] - pairs[loop]['coord']['press'][0])) + abs(
            (pairs[loop]['coord']['release'][1] - pairs[loop]['coord']['press'][1]))

        pairs[loop]['d'] = str(distance)

    ds = {}
    for loop in df_key['user'].unique():
        for subloop in pairs:
            user, sam, d = pairs[subloop]['user'], pairs[subloop]['sample'], pairs[subloop]['d']

            if user not in ds:
                ds[user] = {}

            if sam not in ds[user]:
                ds[user][sam] = {}

            if d not in ds[user][sam]:
                ds[user][sam][d] = {}

            if pairs[subloop]['user'] == loop:
                ds[user][sam][d][subloop] = pairs[subloop]['time']

    for loop in ds:
        for subloop in ds[loop]:
            soma, pesos, div, pot = 0, 0, 0, 1

            for subsubloop in ds[loop][subloop]:
                s = pd.Series(ds[loop][subloop][subsubloop])

                soma += sum(s * int(subsubloop))
                pesos += int(subsubloop) * len(s)

                for d in s:
                    if d != 0:
                        div += int(subsubloop) / d

                for p in s:
                    if p != 0:
                        pot += int(subsubloop) * math.log(abs(p))

            map_value = round(soma / pesos, 2)
            mhp_value = round(pesos / div, 2)
            mgp_value = round(math.exp(pot / pesos), 2)

            df_fea.loc[subloop, str('distance_map')] = map_value
            df_fea.loc[subloop, str('distance_mhp')] = mhp_value
            df_fea.loc[subloop, str('distance_mgp')] = mgp_value

def calculate_mouse_features(df_fea, df_mou):
    """
    Calcula as features relacionadas ao uso do mouse, incluindo distância percorrida, precisão,
    e velocidade dos movimentos.

    Parâmetros:
    df_fea (DataFrame): DataFrame onde as features serão armazenadas.
    df_mou (DataFrame): DataFrame contendo os dados de mouse.
    """

    quant = 0
    movement, moves, move = {}, deque(), deque()

    for samp in df_mou['session'].unique():
        user = df_mou.loc[df_mou['session'] == samp, 'user'].values[0]

        if user not in movement:
            movement[user] = {}

        if "Amostra" + str(samp) not in movement[user]:
            movement[user][samp] = {}

        cond = df_mou['session'] == samp
        df_sub = df_mou[cond]

        anterior = df_sub.iloc[0]

        for loop in df_sub.index:
            if df_sub.loc[loop]["event"] == "mousemove":
                tempo = int(df_sub.loc[loop]['epoch']) - int(anterior['epoch'])

                if tempo >= 500:
                    moves.append(move)
                    move = deque()
                    move.append(["move", df_sub.loc[loop]['coordenadas'], df_sub.loc[loop]['epoch']])
                else:
                    move.append(["move", df_sub.loc[loop]['coordenadas'], df_sub.loc[loop]['epoch']])

            elif df_sub.loc[loop]["event"] == "mousedown":
                moves.append(move)
                move = deque()
                move.append(["click", df_sub.loc[loop]['coordenadas'], df_sub.loc[loop]['epoch']])

            elif df_sub.loc[loop]["event"] == "mouseup":
                move.append(["click", df_sub.loc[loop]['coordenadas'], df_sub.loc[loop]['epoch']])
                moves.append(move)
                move = deque()

            if df_sub.loc[loop]['epoch'] != anterior['epoch']:
                anterior = df_sub.loc[loop]

        descarte = []
        for loop in moves:
            if len(loop) < 2:
                descarte.append(loop)

        if len(descarte) > 0:
            for loop in descarte:
                moves.remove(loop)

        quant_move = 0
        for ms in moves:
            quant += 1

            if "Movement" + str(quant) not in movement[user][samp]:
                movement[user][samp]["Movement " + str(quant)] = {}

            for m in ms:
                movement[user][samp]["Movement " + str(quant)][quant_move + 1] = m
                quant_move += 1

            quant_move = 0
        moves = deque()

    d = []
    prec = {}

    for user in movement:
        for sample in movement[user]:
            for moves in movement[user][sample]:
                if len(movement[user][sample][moves]) > 3:
                    first = movement[user][sample][moves][1]
                    last = movement[user][sample][moves][len(movement[user][sample][moves])]

                    if first[0] == "move":
                        coord1 = first[1].strip("()").replace(" ", "").split(",")
                        coord2 = last[1].strip("()").replace(" ", "").split(",")

                        distance = int(round(
                            (math.sqrt((int(coord2[0]) - int(coord1[0])) ** 2 + (int(coord2[1]) - int(coord1[1])) ** 2)),
                            0))

                        d.append(distance)

                        if user not in prec:
                            prec[user] = {}

                        if sample not in prec[user]:
                            prec[user][sample] = {}

                        if moves not in prec[user][sample]:
                            prec[user][sample][moves] = {}

                        prec[user][sample][moves]["distance"] = distance

                        # Calcula e salva a trajetória
                        traj = sum(d)
                        prec[user][sample][moves]["trajectory"] = traj

            d = pd.Series(d)

            df_fea.loc[sample, 'distance_max'] = d.max()
            df_fea.loc[sample, 'distance_min'] = d.min()
            df_fea.loc[sample, 'distance_mea'] = round(d.mean(), 2)
            df_fea.loc[sample, 'distance_med'] = round(d.median(), 2)

            d = []

    precisions = []
    for user in prec:
        for sample in prec[user]:
            for moves in prec[user][sample]:
                if 'trajectory' in prec[user][sample][moves] and prec[user][sample][moves]['distance'] != 0 and prec[user][sample][moves]['trajectory'] != 0:
                    precision = int(round(
                        (prec[user][sample][moves]['distance'] / prec[user][sample][moves]['trajectory']), 2) * 100)
                    precisions.append(precision)

            p = pd.Series(precisions)

            df_fea.loc[sample, 'precison_max'] = p.max()
            df_fea.loc[sample, 'precison_min'] = p.min()
            df_fea.loc[sample, 'precison_mea'] = round(p.mean(), 2)
            df_fea.loc[sample, 'precison_med'] = round(p.median(), 2)

            precisions = []

    s = []
    for user in movement:
        for sample in movement[user]:
            for moves in movement[user][sample]:
                if len(movement[user][sample][moves]) > 3:
                    first = movement[user][sample][moves][1]
                    last = movement[user][sample][moves][len(movement[user][sample][moves])]

                    if first[0] == "move":
                        coord1 = first[1].strip("()").replace(" ", "").split(",")
                        coord2 = last[1].strip("()").replace(" ", "").split(",")

                        distance = int(round(
                            (math.sqrt((int(coord2[0]) - int(coord1[0])) ** 2 + (int(coord2[1]) - int(coord1[1])) ** 2)),
                            0))

                        time = (int(last[2]) - int(first[2])) / 1000

                        speed = int(round(distance / time, 2))

                        s.append(speed)

            s = pd.Series(s)

            df_fea.loc[sample, 'speed_max'] = s.max()
            df_fea.loc[sample, 'speed_min'] = s.min()
            df_fea.loc[sample, 'speed_mea'] = round(s.mean(), 2)
            df_fea.loc[sample, 'speed_med'] = round(s.median(), 2)

            s = []

    t = []
    clicks = {}

    for user in movement:
        for sample in movement[user]:
            for moves in movement[user][sample]:
                press = movement[user][sample][moves][1]
                release = movement[user][sample][moves][len(movement[user][sample][moves])]

                if press[0] == "click":
                    time = int(release[2]) - int(press[2])
                    t.append(time)

            t = pd.Series(t)

            df_fea.loc[sample, 'click_max'] = t.max()
            df_fea.loc[sample, 'click_min'] = t.min()
            df_fea.loc[sample, 'click_mea'] = round(t.mean(), 2)
            df_fea.loc[sample, 'click_med'] = round(t.median(), 2)

            t = []

def calculate_behavior_features(df_fea, df_key, df_mou, df_beh):
    """
    Calcula as features relacionadas ao comportamento do usuário, como uso de teclas especiais,
    ordem de preenchimento, e número de erros.

    Parâmetros:
    df_fea (DataFrame): DataFrame onde as features serão armazenadas.
    df_key (DataFrame): DataFrame contendo os dados de teclado.
    df_mou (DataFrame): DataFrame contendo os dados de mouse.
    df_beh (DataFrame): DataFrame contendo os dados de comportamento.
    """

    for samp in df_key["session"].unique():
        df_sub = df_key[df_key["session"] == samp]

        left, right = 0, 0
        for loop in df_sub['position']:
            if loop == "ShiftLeft":
                left += 1
            elif loop == "ShiftRight":
                right += 1

        total = left + right
        if total == 0:
            total = 1

        df_fea.loc[samp, 'shift_right'] = round((right * 100) / total, 2)
        df_fea.loc[samp, 'shift_left'] = round((left * 100) / total, 2)

        for loop in df_sub["session"].unique():
            ord = df_beh.loc[(loop - 1)]["order"].split("-")

            quant = 1
            for subloop in range(0, 5):
                if quant == 1:
                    df_fea.loc[samp, 'order_cn'] = ord[subloop]
                elif quant == 2:
                    df_fea.loc[samp, 'order_m'] = ord[subloop]
                elif quant == 3:
                    df_fea.loc[samp, 'order_y'] = ord[subloop]
                elif quant == 4:
                    df_fea.loc[samp, 'order_sc'] = ord[subloop]
                elif quant == 5:
                    df_fea.loc[samp, 'order_n'] = ord[subloop]

                quant += 1

        tab, quant = 0, 0
        for loop in df_sub['position']:
            if loop == "Tab":
                quant += 1

        tab = quant / 2
        if tab > 4:
            tab = 4

        total = round((tab * 100) / 4, 2)

        df_fea.loc[samp, 'tab'] = quant
        df_fea.loc[samp, 'tab_switch'] = total
        df_fea.loc[samp, 'mouse_switch'] = 100 - total

        caps, shift = 0, 0
        for loop in df_sub['key_name']:
            if loop == "CapsLock":
                caps += 1
            elif loop == "Shift":
                shift += 1

        total = caps + shift
        if total == 0:
            total = 1

        df_fea.loc[samp, 'shift_up'] = round((shift * 100) / total, 2)
        df_fea.loc[samp, 'capslock_up'] = round((caps * 100) / total, 2)

        digit, pad = 0, 0
        for loop in df_sub['position']:
            if loop[0:6] == "Numpad":
                pad += 1
            elif loop[0:5] == "Digit":
                digit += 1

        total = pad + digit
        if total == 0:
            total = 1

        df_fea.loc[samp, 'digit'] = round((digit * 100) / total, 2)
        df_fea.loc[samp, 'numpad'] = round((pad * 100) / total, 2)

        form = int(df_beh.loc[(samp - 1)]["formFinishE"]) - int(df_beh.loc[(samp - 1)]["formStartE"])
        cn = int(df_beh.loc[(samp - 1)]["cnFinishE"]) - int(df_beh.loc[(samp - 1)]["cnStartE"])
        m = int(df_beh.loc[(samp - 1)]["mFinishE"]) - int(df_beh.loc[(samp - 1)]["mStartE"])
        y = int(df_beh.loc[(samp - 1)]["yFinishE"]) - int(df_beh.loc[(samp - 1)]["yStartE"])
        sc = int(df_beh.loc[(samp - 1)]["scFinishE"]) - int(df_beh.loc[(samp - 1)]["scStartE"])
        n = int(df_beh.loc[(samp - 1)]["naFinishE"]) - int(df_beh.loc[(samp - 1)]["naStartE"])

        df_fea.loc[samp, 'total_form'] = form
        df_fea.loc[samp, 'total_cn'] = cn
        df_fea.loc[samp, 'total_m'] = m
        df_fea.loc[samp, 'total_y'] = y
        df_fea.loc[samp, 'total_sc'] = sc
        df_fea.loc[samp, 'total_n'] = n

        k = len(df_sub)
        m = len(df_mou[df_mou["session"] == samp])

        df_fea.loc[samp, 'total_key'] = k
        df_fea.loc[samp, 'total_move'] = m

        up, low = 0, 0
        for loop in df_sub["key_name"]:
            if loop.isupper():
                up += 1
            elif loop.islower():
                low += 1

        if (up > 0) and (low == 0):
            status = 1
        if (up == 0) and (low > 0):
            status = 2
        if (up > 0) and (low > 0):
            status = 3

        df_fea.loc[samp, 'letters'] = status

        back = 0
        for loop in df_sub["position"]:
            if loop == "Backspace":
                back += 1

        total = int(back / 2)

        df_fea.loc[samp, 'erros'] = total

        over = 0
        anterior = df_sub.iloc[0]

        for loop in df_sub.index:
            if (df_sub.loc[loop]["epoch"] != anterior["epoch"]) and (df_sub.loc[loop]['event'] == "keydown") and (anterior["event"] == "keydown"):
                over += 1

            anterior = df_sub.loc[loop]

        df_fea.loc[samp, 'overlay'] = over

    df_fea["shift_right"] = df_fea["shift_right"].astype(int)
    df_fea["shift_left"] = df_fea["shift_left"].astype(int)
    df_fea["order_cn"] = df_fea["order_cn"].astype(int)
    df_fea["order_m"] = df_fea["order_m"].astype(int)
    df_fea["order_y"] = df_fea["order_y"].astype(int)
    df_fea["order_sc"] = df_fea["order_sc"].astype(int)
    df_fea["order_n"] = df_fea["order_n"].astype(int)
    df_fea["tab"] = df_fea["tab"].astype(int)
    df_fea["tab_switch"] = df_fea["tab_switch"].astype(int)
    df_fea["mouse_switch"] = df_fea["mouse_switch"].astype(int)
    df_fea["shift_up"] = df_fea["shift_up"].astype(int)
    df_fea["capslock_up"] = df_fea["capslock_up"].astype(int)
    df_fea["digit"] = df_fea["digit"].astype(int)
    df_fea["numpad"] = df_fea["numpad"].astype(int)
    df_fea["total_form"] = df_fea["total_form"].astype(int)
    df_fea["total_cn"] = df_fea["total_cn"].astype(int)
    df_fea["total_m"] = df_fea["total_m"].astype(int)
    df_fea["total_y"] = df_fea["total_y"].astype(int)
    df_fea["total_sc"] = df_fea["total_sc"].astype(int)
    df_fea["total_n"] = df_fea["total_n"].astype(int)
    df_fea["total_key"] = df_fea["total_key"].astype(int)
    df_fea["total_move"] = df_fea["total_move"].astype(int)
    df_fea["erros"] = df_fea["erros"].astype(int)
    df_fea["overlay"] = df_fea["overlay"].astype(int)

def normalize_and_save_features(df_fea, output_path):
    """
    Normaliza as features e as salva em um arquivo Excel.

    Parâmetros:
    df_fea (DataFrame): DataFrame contendo as features a serem normalizadas.
    output_path (str): Caminho do arquivo onde os dados normalizados serão salvos.
    """

    scaler = mms()
    df_fea_normalized = df_fea.copy()
    df_fea_normalized[df_fea.columns.difference(['label'])] = scaler.fit_transform(df_fea[df_fea.columns.difference(['label'])])
    
    df_fea_normalized.to_excel(output_path, index=False)
