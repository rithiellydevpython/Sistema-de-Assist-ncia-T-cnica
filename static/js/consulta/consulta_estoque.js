const lista = document.getElementById("lista-estoque");

async function carregarEstoque() {
    try {
        const response = await fetch("http://127.0.0.1:8000/estoque/");

        if (!response.ok) {
            throw new Error("Erro ao buscar estoque");
        }

        const data = await response.json();
        console.log("Dados recebidos:", data);

        // suporta dois formatos de resposta
        const itens = data.estoque || data;

        lista.innerHTML = "";

        itens.forEach(item => {
            const card = document.createElement("div");
            card.classList.add("card-estoque");

            card.innerHTML = `
                <h3>${item.marca} ${item.model}</h3>
                <p><strong>Código:</strong> ${item.code}</p>
                <p><strong>Descrição:</strong> ${item.description}</p>
            `;

            lista.appendChild(card);
        });

    } catch (error) {
        console.error("Erro ao carregar estoque:", error);

        lista.innerHTML = "<p>Erro ao carregar estoque</p>";
    }
}


// carrega automaticamente ao abrir a página
carregarEstoque();