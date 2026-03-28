let estoque = JSON.parse(localStorage.getItem("estoque")) || [];


const form = document.getElementById("form-estoque");
const inputMarca = document.getElementById("marca-estoque");
const inputModelo = document.getElementById("modelo-estoque");
const inputCodigo = document.getElementById("codigo-estoque");
const inputDescricao= document.getElementById("descricao-estoque");

form.addEventListener("submit", function (event){
    event.preventDefault();

    const item = {
        marca: inputMarca.value,
        modelo: inputModelo.value, 
        codigo: inputCodigo.value,
        descricao: inputDescricao.value
    };

    estoque.push(item);

    localStorage.setItem("estoque", JSON.stringify(estoque));

    form.reset();

    renderizarEstoque();
});
