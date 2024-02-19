from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector 

app = Flask(__name__)
CORS(app, resources={r"/receber": {"origins": "https://582b-2804-658c-215c-9c00-bc98-166-e41f-266e.ngrok-free.app"}})

# Configura o banco
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'sentinela'
}

@app.route('/', methods=['GET'])
def hello():
    return "Hello!"

# Rota para receber dados via HTTP POST
@app.route('/receber', methods=['POST'])
@cross_origin()
    
def receber():
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Extrair dados do corpo da requisição POST
        data = request.json

        # Determinar Sessão
        cursor.execute("select MAX(id_session) from sample;")
        session = cursor.fetchone()[0]

        if(session == None):
            session = 1
        else:
            session = session + 1

        def montarAmostra(table, user, data, session):
            # Monta query
            if(table == 'keyboard'):
                query = "insert into sample values(%s, %s, %s, %s, %s, %s)"
                values = ('', data, '0', '0', user, session)
            elif(table == 'mouse'):
                query = "insert into sample values(%s, %s, %s, %s, %s, %s)"
                values = ('', '0', data, '0', user, session)
            elif(table == 'behavior'):
                query = "insert into sample values(%s, %s, %s, %s, %s, %s)"
                values = ('', '0', '0', data, user, session)

            # Executa query
            cursor.execute(query, values)

        # Query User
        person = data['user']
        
        # Monta query
        query = "insert into user select %s, %s where not exists(select nome from user where nome=%s);"
        values = ('', person, person)

        # Executa query
        cursor.execute(query, values)

        # Retorna o ID gerado para o último usuário inserido
        cursor.execute("select id_user from user where nome='" + person + "'")
        user = cursor.fetchone()[0]

        # Query Keyboard
        for loop in range(1, len(data['dig'])):
            key = data['dig'][str(loop)]['tecla']
            pos = data['dig'][str(loop)]['pos']
            ev = data['dig'][str(loop)]['evento']
            inp = data['dig'][str(loop)]['campo']
            ts = data['dig'][str(loop)]['ts']
            ep = data['dig'][str(loop)]['epoch']
            
            # Monta query
            query = "insert into keyboard values(%s, %s, %s, %s, %s, %s, %s)"
            values = ('', key, pos, ev, inp, ts, ep)

            # Executa query
            cursor.execute(query, values)

            # Retorna o ID gerado para o último registro inserido
            cursor.execute("SELECT LAST_INSERT_ID()")
            id = cursor.fetchone()[0]

            # Regista uma Amostra
            montarAmostra("keyboard", user, id, session)

        # Query Mouse
        for loop in range(1, len(data['mou'])):
            ev = data['mou'][str(loop)]['event_m']
            coo = data['mou'][str(loop)]['coord']
            ts = data['mou'][str(loop)]['ts_m']
            ep = data['mou'][str(loop)]['epoch_m']
            
            # Monta query
            query = "insert into mouse values(%s, %s, %s, %s, %s)"
            values = ('', ev, coo, ts, ep)

            # Executa query
            cursor.execute(query, values)

            # Retorna o ID gerado para o último registro inserido
            cursor.execute("SELECT LAST_INSERT_ID()")
            id = cursor.fetchone()[0]

            # Regista uma Amostra
            montarAmostra("mouse", user, id, session)
        
        # Query Comportamento
        inp = data['comp']["1"]['ord']
        num = data['comp']["1"]['num_type']
        upp = data['comp']["1"]['up_type']

        naStTs = data['comp']["1"]['time_txt']['txtNom']['Started']['Timestamp']
        naStE = data['comp']["1"]['time_txt']['txtNom']['Started']['Epoch']
        naFnTs = data['comp']["1"]['time_txt']['txtNom']['Finished']['Timestamp']
        naFnE = data['comp']["1"]['time_txt']['txtNom']['Finished']['Epoch']

        cnStTs = data['comp']["1"]['time_txt']['txtNum']['Started']['Timestamp']
        cnStE = data['comp']["1"]['time_txt']['txtNum']['Started']['Epoch']
        cnFnTs = data['comp']["1"]['time_txt']['txtNum']['Finished']['Timestamp']
        cnFnE = data['comp']["1"]['time_txt']['txtNum']['Finished']['Epoch']

        scStTs = data['comp']["1"]['time_txt']['txtCVC']['Started']['Timestamp']
        scStE = data['comp']["1"]['time_txt']['txtCVC']['Started']['Epoch']
        scFnTs = data['comp']["1"]['time_txt']['txtCVC']['Finished']['Timestamp']
        scFnE = data['comp']["1"]['time_txt']['txtCVC']['Finished']['Epoch']

        mStTs = data['comp']["1"]['time_txt']['txtMes']['Started']['Timestamp']
        mStE = data['comp']["1"]['time_txt']['txtMes']['Started']['Epoch']
        mFnTs = data['comp']["1"]['time_txt']['txtMes']['Finished']['Timestamp']
        mFnE = data['comp']["1"]['time_txt']['txtMes']['Finished']['Epoch']

        yStTs = data['comp']["1"]['time_txt']['txtAno']['Started']['Timestamp']
        yStE = data['comp']["1"]['time_txt']['txtAno']['Started']['Epoch']
        yFnTs = data['comp']["1"]['time_txt']['txtAno']['Finished']['Timestamp']
        yFnE = data['comp']["1"]['time_txt']['txtAno']['Finished']['Epoch']

        sTs = data['comp']["1"]['time_form']['Started']['Timestamp']
        sE = data['comp']["1"]['time_form']['Started']['Epoch']
        fTs = data['comp']["1"]['time_form']['Finished']['Timestamp']
        fE = data['comp']["1"]['time_form']['Finished']['Epoch']
        
        # Monta query
        query = "insert into behavior values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = ('', inp, num, upp, naStTs, naStE, naFnTs, naFnE, cnStTs, cnStE, cnFnTs, cnFnE, scStTs, scStE, scFnTs, scFnE, mStTs, mStE, mFnTs, mFnE, yStTs, yStE, yFnTs, yFnE, sTs, sE, fTs, fE)

        # Executa query
        cursor.execute(query, values)

        # Retorna o ID gerado para o último registro inserido
        cursor.execute("SELECT LAST_INSERT_ID()")
        id = cursor.fetchone()[0]

        # Regista uma Amostra
        montarAmostra("behavior", user, id, session)

        # Salva as alterações no banco
        conn.commit()

        # Fecha a conexão com o banco
        cursor.close()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Dados salvos com sucesso'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    # Executar o servidor na porta 5000
    # #Inmetro1234#
    app.run(host='192.168.89.113',port=5000)