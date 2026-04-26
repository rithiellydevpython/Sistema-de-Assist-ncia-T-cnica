const API = "http://127.0.0.1:8000/vendas";

const tbody = document.getElementById("tbody-venda");

window.onload = carregarVendas;

async function carregarVendas() {
    try {
        const res = await fetch(API);

        if (!res.ok) {
            throw new Error("Erro ao buscar vendas");
        }

        const vendas = await res.json(); // 👈 aqui

        tbody.innerHTML = ""; 

        if (!vendas.length) {
            tbody.innerHTML = `<tr><td colspan="4">Nenhuma venda encontrada</td></tr>`;
            return;
        }
 

        vendas.forEach(venda => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${venda.marca}</td>
                <td>${venda.model}</td>
                <td>${venda.value}</td>
                <td>${new Date(venda.date).toLocaleDateString("pt-BR")}</td>     
                <td>
                    <button onclick="editar('${venda.id}')">Editar</button>
                    <button onclick="deletar('${venda.id}')">Deletar</button>
                </td>
                `;

            tbody.appendChild(tr);
        });

    } catch (error) {
        console.log(error);
        tbody.innerHTML = `<tr><td colspan="5">Erro ao carregar vendas</td></tr>`;
    }
}


async function editar(id, modelAtual, marcaAtual, valueAtual, dateAtual) {

    const novoModelo = prompt("Novo modelo:", modelAtual)?.trim();
    const novaMarca = prompt("Nova marca:", marcaAtual)?.trim();
    const novoValor = parseFloat(prompt("Novo valor:", valueAtual));
    const novaData = prompt("Nova data (YYYY-MM-DD):", dateAtual)?.trim();

    if (!novoModelo || !novaMarca || isNaN(novoValor) || !novaData) return;

    try {
        const res = await fetch(`${API}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                model: novoModelo,
                marca: novaMarca,
                value: novoValor,
                date: novaData
            })
        });

        if (!res.ok) {
            throw new Error("Erro ao atualizar venda");
        }

        carregarVendas();

    } catch (error) {
        console.error(error);
        alert("Erro ao atualizar venda");
    }
}

// DELETAR APARELHO
async function deletar(id) {

    if (!confirm("Deseja deletar esta venda?")) return;

    try {
        const res = await fetch(`${API}/${id}`, {
            method: "DELETE"
        });

        if (!res.ok) {
            throw new Error("Erro ao deletar venda");
        }

        carregarVendas();

    } catch (error) {
        console.error(error);
        alert("Erro ao deletar venda");
    }
}