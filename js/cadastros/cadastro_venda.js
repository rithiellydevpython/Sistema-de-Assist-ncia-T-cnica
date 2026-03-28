let vendas = JSON.parse(localStorage.getItem("vendas")) || [];


const form = document.getElementById("form-venda");
const inputMarca = document.getElementById("marca-venda");
const inputModelo = document.getElementById("modelo-venda");
const inputValor = document.getElementById("valor-venda");
const inputData = document.getElementById("data-venda");

form.addEventListener("submit", function (event){
    event.preventDefault();

    const venda = {
        marca: inputMarca.value,
        modelo: inputModelo.value, 
        valor: inputValor.value,
        data: inputData.value
    };

    vendas.push(venda);

    localStorage.setItem("vendas", JSON.stringify(vendas));

    form.reset();
});
