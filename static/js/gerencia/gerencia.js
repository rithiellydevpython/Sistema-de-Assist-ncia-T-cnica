document.getElementById("form-compras").addEventListener("submit", async (e) => {
    e.preventDefault();

    const compra = {
        produto: document.getElementById("compras_produtos").value,
        valor: parseFloat(document.getElementById("valor_compras").value),
        quantidade: parseInt(document.getElementById("quantidade").value),
        data: document.getElementById("data").value
    };

    const res = await fetch("http://127.0.0.1:8000/management/compras", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(compra)
    });

    const data = await res.json(); // 👈 LÊ UMA VEZ SÓ

    if (!res.ok) {
        console.log("❌ ERRO DETALHADO:", data);
    } else {
        console.log("✔ SUCESSO:", data);
    }
});

document.getElementById("form-despesas").addEventListener("submit", async (e) => {
    e.preventDefault();

    const despesa = {
        nome: document.getElementById("nome_despesa").value,
        valor: parseFloat(document.getElementById("valor_despesa").value),
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
        salario: parseFloat(document.getElementById("salario").value)
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
            <button onclick="editarDespesa(${item.id})">Editar</button>
            <button onclick="excluirDespesa(${item.id})">Excluir</button>
        </div>
        `;
    });
}

async function carregarCompras() {
    const res = await fetch("http://127.0.0.1:8000/management/compras");
    const dados = await res.json();

    const container = document.getElementById("lista-compras");
    container.innerHTML = "";

    dados.forEach(item => {
        container.innerHTML += `
        <div class="card">
            <p><strong>Produto:</strong> ${item.produto}</p>
            <p><strong>Valor:</strong> R$ ${item.valor}</p>
            <p><strong>Quantidade:</strong> ${item.quantidade}</p>
            <p><strong>Data:</strong> ${item.data}</p>
            <button onclick="editarCompra(${item.id})">Editar</button>
            <button onclick="excluirCompra(${item.id})">Excluir</button>
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
                <button onclick="editarFuncionario(${item.id})">Editar</button>
                <button onclick="excluirFuncionario(${item.id})">Excluir</button>
            </div>
        `;
    });
}

document.addEventListener("DOMContentLoaded", () => {
    carregarCompras();
    carregarDespesas();
    carregarFuncionarios();
});

async function editarFuncionario(id) {
    const novoNome = prompt("Digite o novo nome:");
    const novoCargo = prompt("Digite o novo cargo:");
    const novoSalario = parseFloat(prompt("Digite o novo salário:"));

    // validação básica
    if (!novoNome || !novoCargo || isNaN(novoSalario)) {
        console.log("❌ Dados inválidos");
        return;
    }

    try {
        const res = await fetch(`http://127.0.0.1:8000/management/funcionarios/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                nome: novoNome,
                cargo: novoCargo,
                salario: novoSalario
            })
        });

        const data = await res.json();

        if (!res.ok) {
            console.log("❌ ERRO:", data);
            return;
        }

        console.log("✔ Funcionário atualizado:", data);

        carregarFuncionarios(); // 🔥 atualiza lista

    } catch (error) {
        console.error("❌ ERRO:", error);
    }
}

async function excluirFuncionario(id) {
    if (!confirm("Tem certeza que deseja excluir este funcionário?")) {
        return;
    }
    try {        const res = await fetch(`http://127.0.0.1:8000/management/funcionarios/${id}`, {
        method: "DELETE"
    });
    const data = await res.json();

    if (!res.ok) {
        console.log("❌ ERRO:", data);
        return;
    }

    console.log("✔ Funcionário excluído:", data);

    carregarFuncionarios(); // 🔥 atualiza lista

} catch (error) {
    console.error("❌ ERRO:", error);
}
}

async function editarDespesa(id) {
    const novoNome = prompt("Digite o novo nome:");
    const novoValor = parseFloat(prompt("Digite o novo valor:"));
    const novoPagamento = prompt("Digite a nova forma de pagamento:");  

    if (!novoNome || isNaN(novoValor) || !novoPagamento) {
        console.log("❌ Dados inválidos");
        return;
    }

    try {
        const res = await fetch(`http://127.0.0.1:8000/management/despesas/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                nome: novoNome, 
                valor: novoValor,
                pagamento: novoPagamento
            })
        });
        const data = await res.json();

        if (!res.ok) {
            console.log("❌ ERRO:", data);
            return;
        }
        console.log("✔ Despesa atualizada:", data);
        carregarDespesas(); // 🔥 atualiza lista
    }
    catch (error) {
        console.error("❌ ERRO:", error);
    }
}

async function excluirDespesa(id) {
    if (!confirm("Tem certeza que deseja excluir esta despesa?")) {
        return;
    }
    try {
        const res = await fetch(`http://127.0.0.1:8000/management/despesas/${id}`, {
            method: "DELETE"
        });
        const data = await res.json();

        if (!res.ok) {
            console.log("❌ ERRO:", data);
            return;
        }

        console.log("✔ Despesa excluída:", data);

        carregarDespesas(); // 🔥 atualiza lista

    } catch (error) {
        console.error("❌ ERRO:", error);
    }
}       

async function editarCompra(id) {
    const novoProduto = prompt("Digite o novo produto:");
    const novoValor = parseFloat(prompt("Digite o novo valor:"));
    const novaQuantidade = parseInt(prompt("Digite a nova quantidade:"));
    const novaData = prompt("Digite a nova data (YYYY-MM-DD):");

    if (!novoProduto || isNaN(novoValor) || isNaN(novaQuantidade) || !novaData) {
        console.log("❌ Dados inválidos");
        return;
    }

    try {
        const res = await fetch(`http://127.0.0.1:8000/management/compras/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                produto: novoProduto,
                valor: novoValor,
                quantidade: novaQuantidade,
                data: novaData
            })
        });
        const data = await res.json();

        if (!res.ok) {
            console.log("❌ ERRO:", data);
            return;
        }
        console.log("✔ Compra atualizada:", data);
        carregarCompras(); // 🔥 atualiza lista
    }
    catch (error) {
        console.error("❌ ERRO:", error);
    }
}

async function excluirCompra(id) {
    if (!confirm("Tem certeza que deseja excluir esta compra?")) {
        return;
    }
    try {
        const res = await fetch(`http://127.0.0.1:8000/management/compras/${id}`, {
            method: "DELETE"
        });
        const data = await res.json();

        if (!res.ok) {
            console.log("❌ ERRO:", data);
            return;
        }

        console.log("✔ Compra excluída:", data);

        carregarCompras(); // 🔥 atualiza lista

    } catch (error) {
        console.error("❌ ERRO:", error);
    }
}

