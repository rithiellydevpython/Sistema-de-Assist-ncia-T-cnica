const tbody = document.getElementById("tbody-aparelho");

async function carregarAparelhos() {
    try {
        const res = await fetch("http://127.0.0.1:8000/aparelhos/");
        
        // Verifica se a resposta foi OK
        if (!res.ok) {
            throw new Error(`Erro na requisição: ${res.status}`);
        }

        let aparelhos = await res.json();

        // Se não for array, transforma em array
        if (!Array.isArray(aparelhos)) {
            // Se for um objeto com chave "devices" ou similar, pega o array interno
            if (aparelhos.devices && Array.isArray(aparelhos.devices)) {
                aparelhos = aparelhos.devices;
            } else {
                // Caso seja objeto único, transforma em array de um elemento
                aparelhos = [aparelhos];
            }
        }

        // Limpa tbody antes de adicionar novos dados
        tbody.innerHTML = "";

        // Popula a tabela
        aparelhos.forEach(aparelho => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${aparelho.code || "-"}</td>
                <td>${aparelho.marca || "-"}</td>
                <td>
                    <button onclick="editarAparelho('${aparelho.code}')">Editar</button>
                    <button onclick="deletarAparelho('${aparelho.code}')">Deletar</button>
                </td>
            `;

            tbody.appendChild(tr);
        });

    } catch (error) {
        console.error("Erro ao carregar aparelhos:", error);
        tbody.innerHTML = `<tr><td colspan="3">Erro ao carregar aparelhos</td></tr>`;
    }
}

// Chamada inicial
carregarAparelhos();