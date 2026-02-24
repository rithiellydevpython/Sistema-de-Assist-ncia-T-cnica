let aparelhos = JSON.parse(localStorage.getItem("aparelhos")) || [];

const form = document.getElementById("form-aparelho");
const inputCodigo = document.getElementById("codigo-aparelho");
const inputMarca = document.getElementById("marca-aparelho");
const inputModelo = document.getElementById("modelo-aparelho");

form.addEventListener("submit", function (event){
    event.preventDefault();

    const aparelho = {
        marca: inputMarca.value,
        modelo: inputModelo.value,
        codigo: inputCodigo.value
    };

    aparelhos.push(aparelho);

    localStorage.setItem("aparelhos", JSON.stringify(aparelhos));

    form.reset();
    
});