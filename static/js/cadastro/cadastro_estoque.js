// Função para renderizar cards de estoque
async function renderizarEstoque() {
    try {
        const res = await fetch("http://127.0.0.1:8000/estoque/");
        if (!res.ok) throw new Error("Erro ao buscar estoque do backend");

        const data = await res.json();

        console.log("Resposta do backend:", data);

        const lista = document.getElementById("lista-estoque");
        lista.innerHTML = ""; // limpa antes de renderizar

        const listaEstoque = data.estoque || data;

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

// Pegando o formulário
const form = document.getElementById("form-estoque");

// Função de cadastro: envia dados para backend e atualiza os cards
form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const item = {
        marca: document.getElementById("marca-estoque").value,
        modelo: document.getElementById("modelo-estoque").value,
        codigo: document.getElementById("codigo-estoque").value,
        descricao: document.getElementById("descricao-estoque").value
    };

    try {
        const res = await fetch("http://127.0.0.1:8000/estoque/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(item)
        });

        if (!res.ok) throw new Error("Erro ao cadastrar item no backend");

        await res.json();
        form.reset();
        renderizarEstoque();  // <--- agora está definido antes de chamar
        alert("Item cadastrado com sucesso!");
    } catch (err) {
        console.error("Erro ao cadastrar item:", err);
        alert("Erro ao cadastrar item no estoque");
    }
});

// Renderiza cards ao carregar a página
renderizarEstoque();

