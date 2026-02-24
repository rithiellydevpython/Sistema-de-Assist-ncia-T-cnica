let servicos = JSON.parse(localStorage.getItem("servicos")) || []; // cria o array

//seleciona os elementos

const form = document.getElementById("form-servico");
const inputModelo = document.getElementById("modelo-servico");
const inputServico = document.getElementById("servico-realizado");
const inputCliente = document.getElementById("cliente-servico");
const inputData = document.getElementById("data-servico");
const inputValor = document.getElementById("valor-servico");
const selectStatus = document.getElementById("status-servico");


//evento de submit

//essa função cria um objeto serviço, adiciona no array, salva no localStorage e limpa o formulário

form.addEventListener("submit", function (event){
    event.preventDefault();

    const servico = {
        modelo: inputModelo.value,
        servico: inputServico.value,
        cliente: inputCliente.value,
        data: inputData.value,
        valor: inputValor.value,
        status: selectStatus.value
    };

    servicos.push(servico);

    localStorage.setItem("servicos", JSON.stringify(servicos));

    form.reset();

});




