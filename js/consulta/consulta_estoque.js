const lista = document.getElementById('lista-estoque');
const estoque = JSON.parse(localStorage.getItem("estoque")) || [];

function renderizarEstoque() {
    lista.innerHTML = "";

    estoque.forEach((item, index) => {
        const card = document.createElement("div");
        card.classList.add("card-estoque");

        card.innerHTML = `
        <h3>${item.marca} ${item.modelo}</h3>
        <p><strong>Código:</strong> ${item.codigo}</p>
        <p>${item.descricao}</p>
            <div class="acoes">
                <button class="btn-editar">Editar</button>
                <button class="btn-excluir" onclick="excluirItem(${index})">Excluir</button>
            </div>
        `;

        lista.appendChild(card);

    });
}

function excluirItem(index) {
    estoque.splice(index, 1);
    localStorage.setItem("estoque", JSON.stringify(estoque));
    renderizarEstoque();
}

renderizarEstoque();
