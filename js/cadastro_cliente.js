let clientes = JSON.parse(localStorage.getItem("clientes")) || [];

const form = document.getElementById("form-cliente");
const inputNome = document.getElementById("nome-cliente");
const inputNumero = document.getElementById("numero-cliente");
const inputEndereco = document.getElementById("endereco-cliente");
const inputCpf = document.getElementById("cpf-cliente");

form.addEventListener("submit", function (event){
    event.preventDefault();

    const cliente = {
        nome: inputNome.value,
        numero: inputNumero.value, 
        endereco: inputEndereco.value,
        cpf: inputCpf.value
    };

    clientes.push(cliente);

    localStorage.setItem("clientes", JSON.stringify(clientes));

    form.reset();
});
