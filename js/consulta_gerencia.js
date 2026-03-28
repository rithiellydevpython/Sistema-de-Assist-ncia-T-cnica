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

renderizarCard();