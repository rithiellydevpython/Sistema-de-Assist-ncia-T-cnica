const API = "http://127.0.0.1:8000/clients";

window.onload = carregarClientes;

async function carregarClientes() {
    try {
        const res = await fetch(API);

        if (!res.ok) {
            throw new Error("Erro ao buscar clientes");
        }

        const data = await res.json();
        const clientes = data.clientes || [];

        const tbody = document.getElementById("tbody-cliente");

        tbody.innerHTML = "";

        if (!clientes.length) {
            tbody.innerHTML = `<tr><td colspan="5">Nenhum cliente encontrado</td></tr>`;
            return;
        }

        clientes.forEach((cliente) => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${cliente.name}</td>
                <td>${cliente.number}</td>
                <td>${cliente.address}</td>
                <td>${cliente.cpf}</td>
                <td>
                    <button onclick="editar('${cliente.cpf}')">Editar</button>
                    <button onclick="deletar('${cliente.cpf}')">Deletar</button>
                </td>
            `;

            tbody.appendChild(tr);
        });

    } catch (err) {
        console.error("Erro ao carregar clientes:", err);

        const tbody = document.getElementById("tbody-cliente");
        tbody.innerHTML = `<tr><td colspan="5">Erro ao carregar clientes</td></tr>`;
    }
}

async function editar(cpf){
    const novoNumero = prompt("novo numero de telefone: ");
    const novoEndereco = prompt("Novo endereço: ");

    if (!novoNumero || !novoEndereco) return;

    try {
        const res = await fetch(`${API}/${cpf}`, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                number: novoNumero,
                address: novoEndereco
            })
        });

        if (!res.ok) {
            throw new Error("Erro ao atualizar cliente");
        }

        carregarClientes()

    } catch (error) {
        console.error(error);
        alert("Erro ao atualizar cliente");
    }
}

async function deletar(cpf) {
    const confirmar = confirm("Tem certeza que deseja deletar este cliente?");

    if (!confirmar) return;

    try {
        const res = await fetch(`${API}/${cpf}`, {
            method: "DELETE"
        });

        if (!res.ok) {
            const erro = await res.json();
            console.error("Erro ao deletar:", erro);
            throw new Error("Erro ao deletar cliente");
        }

        alert("Cliente deletado com sucesso!");

        // 🔄 recarrega a tabela
        carregarClientes();

    } catch (error) {
        console.error(error);
        alert("Erro ao deletar cliente");
    }
}