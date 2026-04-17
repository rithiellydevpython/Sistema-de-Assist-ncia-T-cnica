
const API = "http://127.0.0.1:8000/devices";

// Carrega ao abrir
window.onload = carregarAparelhos;

// LISTAR APARELHOS
async function carregarAparelhos() {
    try {
        const res = await fetch(API);

        if (!res.ok) {
            throw new Error("Erro ao buscar aparelhos");
        }

        const data = await res.json();
        const devices = data.devices || [];

        const tbody = document.getElementById("tbody-aparelho");

        tbody.innerHTML = "";

        if (!devices.length) {
            tbody.innerHTML = `<tr><td colspan="4">Nenhum aparelho encontrado</td></tr>`;
            return;
        }

        devices.forEach(device => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${device.code}</td>
                <td>${device.marca}</td>
                <td>${device.modelo}</td>
                <td>
                    <button onclick="editar('${device.code}')">Editar</button>
                    <button onclick="deletar('${device.code}')">Deletar</button>
                </td>
            `;

            tbody.appendChild(tr);
        });

    } catch (error) {
        console.error(error);

        const tbody = document.getElementById("tbody-aparelho");
        tbody.innerHTML = `<tr><td colspan="4">Erro ao carregar aparelhos</td></tr>`;
    }
}

// EDITAR APARELHO

async function editar(code) {

    const novaMarca = prompt("Nova marca:");
    const novoModelo = prompt("Novo modelo:");

    if (!novaMarca || !novoModelo) return;

    try {
        const res = await fetch(`${API}/${code}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                code: code,
                marca: novaMarca,
                modelo: novoModelo
            })
        });

        if (!res.ok) {
            throw new Error("Erro ao atualizar aparelho");
        }

        carregarAparelhos();

    } catch (error) {
        console.error(error);
        alert("Erro ao atualizar aparelho");
    }
}

// DELETAR APARELHO
async function deletar(code) {

    const confirmar = confirm("Deseja deletar?");
    if (!confirmar) return;

    try {
        const res = await fetch(`${API}/${code}`, {
            method: "DELETE"
        });

        if (!res.ok) {
            throw new Error("Erro ao deletar aparelho");
        }

        carregarAparelhos();

    } catch (error) {
        console.error(error);
        alert("Erro ao deletar aparelho");
    }
}
