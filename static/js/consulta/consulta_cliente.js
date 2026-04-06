const tbody = document.getElementById("tbody-cliente");

async function carregarClientes() {
    try {
        const res = await fetch("http://127.0.0.1:8000/clients/");
        const data = await res.json();

        const clientes = data.users; 

        tbody.innerHTML = ""; // limpa tabela antes de popular

        clientes.forEach((cliente) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${cliente.name}</td>
                <td>${cliente.number}</td>
                <td>${cliente.address}</td>
                <td>${cliente.cpf}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (err) {
        console.error("Erro ao carregar clientes:", err);
    }
}

// Chama a função quando a página carrega
document.addEventListener("DOMContentLoaded", carregarClientes);