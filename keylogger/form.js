let inputValorConv = document.querySelector("#pValorConv");

// Formata campo pra definir o valor que será convertido
let inputValor = document.querySelector('#txtValor');
    inputValor.addEventListener('keyup', function FormatarValor(){
        let valor = inputValor.value.replace('R$', '').trim();

        // Deixa um R$ na frente do valor sempre que é alterado
        inputValor.value = "R$ " + valor;

        // Atualiza valor convertido
        inputValorConv.innerText = "M$ " + (valor * 2.6).toFixed(2);
    })

// Reabre a página para apagar dados já digitados e mostrar ao usuário que enviou os dados
// let final = document.querySelector('#dvBotao');
//     final.addEventListener('click', function RecarregarPag(){
//         window.location.assign("index.html");
//     })

// Monta as informações do cartão fictício
// Cada vez que o site é aberto as informações mudam
let alea = ''

let aleaNum = document.querySelector("#lblNum");
    for(let loop = 0; loop < 16; loop++){
        alea = alea + "" + Math.floor(Math.random() * 9 + 1)

        if(alea.length == 4 || alea.length == 9 || alea.length == 14){
            alea = alea + " ";
        }
    }

    aleaNum.innerText = alea;

alea = ''

let aleaCs = document.querySelector("#lblCVC");
    for(let loop = 0; loop < 3; loop++){
        alea = alea + "" + Math.floor(Math.random() * 9 + 1)
    }

    aleaCs.innerText = alea;

alea = ''

let aleaVen = document.querySelector("#lblVen");
    alea = "" + Math.floor(Math.random() * 12 + 1) // Mês

    if(alea.length == 1){
        alea = '0' + alea;
    }

    alea = alea + "/20"; // Começo Ano
    
    alea = alea + "" + Math.floor(Math.random() * 9 + 1) // 3º Dígito Ano
    alea = alea + "" + Math.floor(Math.random() * 9 + 1) // 4º Dígito Ano

    aleaVen.innerText = alea;