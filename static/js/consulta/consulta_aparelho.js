const tbody = document.getElementById("tbody-aparelho");

async function carregarAparelhos() {
    try {
        const res = await fetch("http://127.0.0.1:8000/devices/");
        const data = await res.json();  // data = { devices: [...] }
        const devices = data.devices || [];  // pega só o array

        tbody.innerHTML = "";

        devices.forEach(device => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${device.code}</td>
                <td>${device.marca}</td>
                <td>${device.modelo}</td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error("Erro ao carregar aparelhos:", error);
        tbody.innerHTML = `<tr><td colspan="3">Erro ao carregar aparelhos</td></tr>`;
    }
}

// Chama a função ao carregar a página
window.addEventListener("DOMContentLoaded", carregarAparelhos);