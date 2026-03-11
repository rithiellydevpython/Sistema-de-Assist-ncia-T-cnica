let compras = JSON.parse(localStorage.getItem("compras")) || [];

const form = document.getElementById("form-compras");
const inputValor = document.getElementById("valor-compra");
const inputUnitario = document.getElementById("valor-unitario");
const inputQuantidade = document.getElementById("quantidade");
const inputMotivo = document.getElementById("motivo");

form.addEventListener("submit", function (event){

    event.preventDefault();

    const compra = {
        valor: inputValor.value,
        unitario: inputUnitario.value,
        quantidade: inputQuantidade.value,
        motivo: inputMotivo.value
    }

    compras.push(compra);

    localStorage.setItem("compras", JSON.stringify(compras));

    form.reset();
})

let saidas = JSON.parse(localStorage.getItem("saidas")) || [];

const formSaida = document.getElementById("form-saidas");
const inputPagamento = document.getElementById("pagamento");
const inputValorPagamento = document.getElementById("valor-pagamento"); 
const inputMetodo = document.getElementById("metodo-pagamento");

formSaida.addEventListener("submit", function (event){
    

    event.preventDefault();

    const saida = {
        pagamento: inputPagamento.value,
        valor: inputValorPagamento.value,
        metodo: inputMetodo.value
    }

    saidas.push(saida);

    localStorage.setItem("saidas", JSON.stringify(saidas));

    formSaida.reset();
});

let funcionarios = JSON.parse(localStorage.getItem("funcionarios")) || [];

const formFuncionarios = document.getElementById("form-funcionarios");
const inputFuncionario = document.getElementById("funcionario");
const inputSalario = document.getElementById("salario");
const inputSalarioPagamento = document.getElementById("metodo-pagamento-salario");

formFuncionarios.addEventListener("submit", function (event){

    event.preventDefault();

    const funcionario = {
        funcionario: inputFuncionario.value,
        salario: inputSalario.value,
        pagamento: inputSalarioPagamento.value
    }

    funcionarios.push(funcionario);

    localStorage.setItem("funcionarios",JSON.stringify(funcionarios));

    formFuncionarios.reset();
})