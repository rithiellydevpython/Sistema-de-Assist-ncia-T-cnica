document.getElementById("form-compras").addEventListener("submit", async (e) => {
    e.preventDefault();

    const compra = {
        produto: document.getElementById("compras_produtos").value,
        valor: parseFloat(document.getElementById("valor_compras").value),
        quantidade: parseInt(document.getElementById("quantidade").value),
        data: document.getElementById("data").value
    };

    await fetch("http://127.0.0.1:8000/management/compras", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(compra)
    });

    e.target.reset();
    carregarCompras();
});

document.getElementById("form-despesas").addEventListener("submit", async (e) => {
    e.preventDefault();

    const despesa = {
        nome: document.getElementById("nome_despesa").value,
        valor: document.getElementById("valor_despesa").value,
        pagamento: document.getElementById("pagamento_despesa").value
    };

    await fetch("http://127.0.0.1:8000/management/despesas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(despesa)
    });

    e.target.reset();
    carregarDespesas();
});

document.getElementById("form_funcionarios").addEventListener("submit", async (e) => {
    e.preventDefault();

    const funcionario = {
        nome: document.getElementById("funcionarios").value,
        cargo: document.getElementById("cargo").value,
        salario: document.getElementById("salario").value
    };

    await fetch("http://127.0.0.1:8000/management/funcionarios", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(funcionario)
    });

    e.target.reset();
    carregarFuncionarios();
});


// salvar

async function carregarDespesas() {
    const res = await fetch("http://127.0.0.1:8000/management/despesas");
    const dados = await res.json();

    const container = document.getElementById("lista-despesas");
    container.innerHTML = "";

    dados.forEach(item => {
        container.innerHTML += `
            <div class="card">
                <p><strong>Nome:</strong> ${item.nome}</p>
                <p><strong>Valor:</strong> R$ ${item.valor}</p>
                <p><strong>Pagamento:</strong> ${item.pagamento}</p>
            </div>
        `;
    });
}

// async function carregarCompras() {
//     const res = await fetch("http://127.0.0.1:8000/management/compras");
//     const dados = await res.json();

//     const container = document.getElementById("lista-compras");
//     container.innerHTML = "";

//     dados.forEach(item => {
//         container.innerHTML += `
//             <div class="card">
//                 <p><strong>Produto:</strong> ${item.produto}</p>
//                 <p><strong>Valor:</strong> R$ ${item.valor}</p>
//                 <p><strong>Quantidade:</strong> ${item.quantidade}</p>
//                 <p><strong>Data:</strong> ${item.data}</p>
//             </div>
//         `;
//     });
// }

async function carregarCompras() {
    const res = await fetch("http://127.0.0.1:8000/management/compras");
    const dados = await res.json();

    console.log("RESPOSTA:", dados);

    if (!Array.isArray(dados)) {
        console.log("Não veio lista:", dados);
        return;
    }

    const container = document.getElementById("lista-compras");
    container.innerHTML = "";

    dados.forEach(item => {
        container.innerHTML += `
            <div class="card">
                <p><strong>Produto:</strong> ${item.produto}</p>
                <p><strong>Valor:</strong> R$ ${item.valor}</p>
                <p><strong>Quantidade:</strong> ${item.quantidade}</p>
                <p><strong>Data:</strong> ${item.data}</p>
            </div>
        `;
    });
}

async function carregarFuncionarios() {
    const res = await fetch("http://127.0.0.1:8000/management/funcionarios");
    const dados = await res.json();

    const container = document.getElementById("lista-funcionarios");
    container.innerHTML = "";

    dados.forEach(item => {
        container.innerHTML += `
            <div class="card">
                <p><strong>Nome:</strong> ${item.nome}</p>
                <p><strong>Cargo:</strong> ${item.cargo}</p>
                <p><strong>Salário:</strong> R$ ${item.salario}</p>
            </div>
        `;
    });
}

document.addEventListener("DOMContentLoaded", () => {
    carregarCompras();
    carregarDespesas();
    carregarFuncionarios();
});

