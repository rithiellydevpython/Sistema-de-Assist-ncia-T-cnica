<<<<<<< HEAD
const lista = document.getElementById("dash-lista");

function renderizarCard() {

    const compras = JSON.parse(localStorage.getItem("compras")) || [];

    lista.innerHTML = "";

    compras.forEach((item, index) => {

        const card = document.createElement("div");
        card.classList.add("card-dash");

        card.innerHTML = `
        <h3>${item.valor}</h3>
        <p>${item.unitario}</p>
        <p>${item.quantidade}</p>
        <p>${item.motivo}</p>
        `
        lista.appendChild(card);
    });

}

=======
const lista = document.getElementById("dash-lista");

function renderizarCard() {

    const compras = JSON.parse(localStorage.getItem("compras")) || [];

    lista.innerHTML = "";

    compras.forEach((item, index) => {

        const card = document.createElement("div");
        card.classList.add("card-dash");

        card.innerHTML = `
        <h3>${item.valor}</h3>
        <p>${item.unitario}</p>
        <p>${item.quantidade}</p>
        <p>${item.motivo}</p>
        `
        lista.appendChild(card);
    });

}

>>>>>>> 5a20f43233c429883c1467714c6e5ffbf3204a6b
renderizarCard();