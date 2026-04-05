const tbody = document.getElementById("tbody-aparelho");

async function carregarAparelhos() {
    try {
        const res = await fetch("http://127.0.0.1:8000/aparelhos/");
        const aparelhos = await res.json();

        aparelhos.forEach(function (aparelho) {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${aparelho.codigo}</td>
                <td>${aparelho.marca}</td>
                <td>${aparelho.modelo}</td>
            `;

            tbody.appendChild(tr);
        });
    } catch (err) {
        console.error("Erro ao carregar aparelhos:", err);
    }
}

carregarAparelhos();