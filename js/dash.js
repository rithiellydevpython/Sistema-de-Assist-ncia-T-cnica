const lista = document.getElementById("servico-lista");

function renderizarCardServico() {

    const servicos = JSON.parse(localStorage.getItem("servicos")) || [];

    lista.innerHTML = "";

    servicos.forEach((item, index) => {

        const card = document.createElement("div");
        card.classList.add("card-servico");

        card.innerHTML = `
        <h3>${item.modelo}</h3>
        <p>${item.servico}</p>
        <p>${item.cliente}</p>
        <p>${item.data}</p>
        <p>${item.valor}</p>
        <p>${item.status}</p>
        `
        lista.appendChild(card);
    });

}

renderizarCardServico();