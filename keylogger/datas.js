// Armazena os dados
let id_dig = 1;
let id_mou = 1;

let amostra = {
    dig: {},
    mouse: {},
    comp: {},
    user: {}
}

// Ajeitar Timestamp
function ajeitarTS(){
    let ts = new Date;

    let year = ts.getFullYear();
    let month = String(ts.getMonth() + 1).padStart(2, '0');
    let day = String(ts.getDate()).padStart(2, '0');
    let hour = String(ts.getHours()).padStart(2, '0');
    let minute = String(ts.getMinutes()).padStart(2, '0');
    let second = String(ts.getSeconds()).padStart(2, '0');
    let milli = String(ts.getMilliseconds()).padStart(6, '0');

    return year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second + ":" + milli;
}


// Dados de digitação
let tecla, event, campo, ts, epoch;

// Funções
function monitorarTecla(e){
    tecla = e.key;
    pos = e.code;
    evento = e.type;
    ts = ajeitarTS();
    epoch = Date.now();

    // Converte nome do campo para número correspondente
    if(e.target.id == 'txtNum'){
        campo = 1;
    }else if(e.target.id == 'txtMes'){
        campo = 2;
    }else if(e.target.id == 'txtAno'){
        campo = 3;
    }else if(e.target.id == 'txtCVC'){
        campo = 4;
    }else if(e.target.id == 'txtNom'){
        campo = 5;
    }

    // Montar objeto
    amostra.dig[id_dig] = {tecla, pos, evento, campo, ts, epoch};

    // Incrementa id
    id_dig++;
}

// Eventos
let num = document.querySelector("#txtNum");
    num.addEventListener('keydown', monitorarTecla);
    num.addEventListener('keyup', monitorarTecla);

let month = document.querySelector("#txtMes");
    month.addEventListener('keydown', monitorarTecla);
    month.addEventListener('keyup', monitorarTecla);

let year = document.querySelector("#txtAno");
    year.addEventListener('keydown', monitorarTecla);
    year.addEventListener('keyup', monitorarTecla);

let cs = document.querySelector("#txtCVC");
    cs.addEventListener('keydown', monitorarTecla);
    cs.addEventListener('keyup', monitorarTecla);

let nom = document.querySelector("#txtNom");
    nom.addEventListener('keydown', monitorarTecla);
    nom.addEventListener('keyup', monitorarTecla);


// Dados do mouse
let coord, event_m, pos_m, ts_m, epoch_m;
let stt = true;

// Funções
function clickCursor(event){
    event_m = event.type;
    coord = "(" + event.pageX + ", " + event.pageY + ")";
    ts_m = ajeitarTS();
    epoch_m = Date.now();

    amostra.mouse[id_mou] = {event_m, coord, ts_m, epoch_m};

    id_mou++;
}

function movimentoCursor(event){
    // Sem intervalo entre registros
    event_m = event.type;
    coord = "(" + event.pageX + ", " + event.pageY + ")";
    ts_m = ajeitarTS();
    epoch_m = Date.now();

    amostra.mouse[id_mou] = {event_m, coord, ts_m, epoch_m};

    id_mou++;

    // Com intervalo entre registors

    // if(stt){
    //     stt = false;

    //     setTimeout(function(){
    //         stt = true;
    
    //         event_m = event.type;
    //         coord = "(" + event.pageX + ", " + event.pageY + ")";
    //         ts_m = ajeitarTS();
    //         epoch_m = Date.now();
        
    //         amostra.mouse[id_mou] = {event_m, coord, ts_m, epoch_m};
        
    //         id_mou++;
    //     }, 250);
    // }
}

// Eventos
let body = document.querySelector('body');
    body.addEventListener('mousemove', movimentoCursor);
    body.addEventListener('mousedown', clickCursor);
    body.addEventListener('mouseup', clickCursor);


// Dados de comportamento

// Declarações
let ord_control = 0;
let num_control = new Set();
let up_control = new Set();

let ord = [];
let num_type = '';
let up_type = '';
let time_txt = {
    'txtNum' : {
        'Started' : {'Timestamp' : '', 'Epoch' : ''},
        'Finished' : {'Timestamp' : '', 'Epoch' : ''}
    },
    'txtNom' : {
        'Started' : {'Timestamp' : '', 'Epoch' : ''},
        'Finished' : {'Timestamp' : '', 'Epoch' : ''}
    },
    'txtMes' : {
        'Started' : {'Timestamp' : '', 'Epoch' : ''},
        'Finished' : {'Timestamp' : '', 'Epoch' : ''}
    },
    'txtAno' : {
        'Started' : {'Timestamp' : '', 'Epoch' : ''},
        'Finished' : { 'Timestamp' : '', 'Epoch' : ''}
    },
    'txtCVC' : { 
        'Started' : {'Timestamp' : '', 'Epoch' : ''},
        'Finished' : {'Timestamp' : '', 'Epoch' : ''}
    }
}
let time_form = {
    'Started' : {'Timestamp' : '', 'Epoch' : ''},
    'Finished' : {'Timestamp' : '', 'Epoch' : ''}
}

// Funções
function ordemCampos(e){
    for(let loop = 0; loop <= ord.length; loop++){
        if(ord[loop] == e.target.id){
            ord_control += 1; 
        }
    }

    if(ord_control == 0){
        ord[ord.length] = e.target.id;
    }

    ord_control = 0;
}

function diferenciarNum(e){
    if(e.code[0] == 'N'){
        num_control.add('Numpad');
    }else{
        num_control.add('Digit');
    }

    if(num_control.size == 1){
        num_type = num_control.values().next().value;
    }else{
        num_type = 'Mixed';
    }
}

function diferenciarUp(e){
    if(e.key == 'Shift'){
        up_control.add('Shift');
    }else if(e.key == 'CapsLock'){
        up_control.add('CapsLock');
    }else{
        up_control.add('None');
    }

    up_control.delete('None');

    if(up_control.size == 0){
        up_type = 'None';
    }else if(up_control.size == 1){
        up_type = up_control.values().next().value;
    }else{
        up_type = 'Mixed';
    }
}

function monitorarInicio(e){
    // Campos isolados
    if(time_txt[e.target.id]['Started']['Timestamp'] == '' && time_txt[e.target.id]['Started']['Epoch'] == ''){
        time_txt[e.target.id]['Started']['Timestamp'] = ajeitarTS();
        time_txt[e.target.id]['Started']['Epoch'] = Date.now();
    }


    // Form todo
    if(time_form['Started']['Timestamp'] == '' && time_form['Started']['Epoch'] == ''){
        time_form['Started']['Timestamp'] = ajeitarTS();
        time_form['Started']['Epoch'] = Date.now();
    }
}

function monitorarFim(e){
    // Campos isolados
    if(time_txt[e.target.id]['Finished']['Timestamp'] == '' && time_txt[e.target.id]['Finished']['Epoch'] == ''){
        time_txt[e.target.id]['Finished']['Timestamp'] = ajeitarTS();
        time_txt[e.target.id]['Finished']['Epoch'] = Date.now();
    }


    // Form todo
    time_form['Finished']['Timestamp'] = ajeitarTS();
    time_form['Finished']['Epoch'] = Date.now();
}

// Eventos
num.addEventListener("input", ordemCampos);
num.addEventListener("keydown", diferenciarNum);
num.addEventListener("focus", monitorarInicio);
num.addEventListener("blur", monitorarFim);

month.addEventListener("input", ordemCampos);
month.addEventListener("keydown", diferenciarNum);
month.addEventListener("focus", monitorarInicio);
month.addEventListener("blur", monitorarFim);

year.addEventListener("input", ordemCampos);
year.addEventListener("keydown", diferenciarNum);
year.addEventListener("focus", monitorarInicio);
year.addEventListener("blur", monitorarFim);

cs.addEventListener("input", ordemCampos);
cs.addEventListener("keydown", diferenciarNum);
cs.addEventListener("focus", monitorarInicio);
cs.addEventListener("blur", monitorarFim);

nom.addEventListener("input", ordemCampos);
nom.addEventListener("keydown", diferenciarUp);
nom.addEventListener("focus", monitorarInicio);
nom.addEventListener("blur", monitorarFim);


// Mandar dados para banco de dados
let salvar = document.querySelector("button");
    salvar.addEventListener('click', async function salvarDados(){
        // Formatar ordem
        for(let loop = 0; loop <= ord.length; loop++){
            if(ord[loop] == 'txtNum'){
                ord[loop] = 1;
            }else if(ord[loop] == 'txtMes'){
                ord[loop] = 2;
            }else if(ord[loop] == 'txtAno'){
                ord[loop] = 3;
            }else if(ord[loop] == 'txtCVC'){
                ord[loop] = 4;
            }else if(ord[loop] == 'txtNom'){
                ord[loop] = 5;
            }
        }

        ord = ord['0'] + "-" + ord['1'] + "-" + ord['2'] + "-" + ord['3'] + "-" + ord['4']
        
        // Adicionar dados de comportamento
        amostra['comp'] = {1 : {ord, num_type, up_type, time_txt, time_form}};

            // Arruma os dados para enviar
            var dados = {
                "dig": amostra['dig'],
                "mou": amostra['mouse'],
                "comp": amostra['comp'],
                "user": nom.value
            };

            // Monta a requisição
            var request = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(dados)
            };

            // URL da API
            var url = 'http://192.168.89.113:5000/receber';

            // Enviar a requisição
            fetch(url, request)
                .then(response => response.json())
                .then(data => {
                    console.log('Resposta da API:', data);
                })
                .catch(error => {
                    console.error('Erro ao enviar requisição:', error);
                });
        
        // Zerar formulários
        // window.location.replace('index.html');
    });