// Consulta estoques direto do backend
async function carregarEstoque() {
    try {
        const res = await fetch("http://127.0.0.1:8000/estoque/");
        if (!res.ok) throw new Error("Erro ao buscar estoque");

        const data = await res.json();
        const lista = document.getElementById("lista-estoque");
        lista.innerHTML = "";

        const listaEstoque = data.estoque || data; // dependendo do retorno do backend

        listaEstoque.forEach(item => {
            const card = document.createElement("div");
            card.classList.add("card-estoque");

            card.innerHTML = `
                <h3>${item.marca} ${item.modelo}</h3>
                <p>Código: ${item.codigo}</p>
                <p>Descrição: ${item.descricao}</p>
            `;

            lista.appendChild(card);
        });

    } catch (err) {
        console.error("Erro ao carregar estoque:", err);
    }
}

// Executa ao abrir a página
carregarEstoque();