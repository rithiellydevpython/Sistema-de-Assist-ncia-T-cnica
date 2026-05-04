const lista = document.getElementById("lista-estoque");

async function carregarEstoque() {
    try {
        const response = await fetch("http://127.0.0.1:8000/estoque/");

        if (!response.ok) {
            throw new Error("Erro ao buscar estoque");
        }

        const data = await response.json();
        console.log("Dados recebidos:", data);

        const itens = data.estoque || data;

        lista.innerHTML = "";

        itens.forEach(item => {
            const card = document.createElement("div");
            card.classList.add("card-estoque");

            card.innerHTML = `
                <h3>${item.marca} ${item.model}</h3>
                <p><strong>Código:</strong> ${item.code}</p>
                <p><strong>Descrição:</strong> ${item.description}</p>

                <div class="acoes">
                    <button onclick="editarItem(${item.id})">Editar</button>
                    <button onclick="excluirItem(${item.id})">Excluir</button>
                </div>
            `;

            lista.appendChild(card);
        });

    } catch (error) {
        console.error("Erro ao carregar estoque:", error);
        lista.innerHTML = "<p>Erro ao carregar estoque</p>";
    }
}

async function editarItem(id) {
    const novaMarca = prompt("Digite a nova marca:");
    const novoModelo = prompt("Digite o novo modelo:");
    const novoCodigo = prompt("Digite o novo código:");
    const novaDescricao = prompt("Digite a nova descrição:");

    if (!novaMarca || !novoModelo || !novoCodigo || !novaDescricao) {
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/estoque/" + id, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                marca: novaMarca,
                model: novoModelo,
                code: novoCodigo,
                description: novaDescricao
            })
        });

        if (!response.ok) {
            throw new Error("Erro ao editar item");
        }
        alert("Item editado com sucesso!");
        carregarEstoque();
    } catch (error) {
        console.error("Erro ao editar item:", error);
        alert("Erro ao editar item");
    }
}

async function excluirItem(id) {
    if (!confirm("Tem certeza que deseja excluir este item?")) {
        return;
    }
    try {
        const response = await fetch("http://127.0.0.1:8000/estoque/" + id, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Erro ao excluir item");
        }
        alert("Item excluído com sucesso!");
        carregarEstoque();
    } catch (error) {
        console.error("Erro ao excluir item:", error);
        alert("Erro ao excluir item");
    }
}

function voltar() {
    if (document.referrer !== "") {
        window.history.back();
    } else {
        window.location.href = "/dashboard"; // ou sua página principal
    }
}


carregarEstoque();