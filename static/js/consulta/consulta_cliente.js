const API = "http://127.0.0.1:8000/servicos";

const tbody = document.getElementById("tbody-servico");

window.onload = carregarServicos;

// 🔎 LISTAR SERVIÇOS
async function carregarServicos() {
  try {
    const res = await fetch(API);

    if (!res.ok) {
      throw new Error("Erro ao buscar serviços");
    }

    const servicos = await res.json();

    tbody.innerHTML = "";

    if (!servicos.length) {
      tbody.innerHTML = `<tr><td colspan="7">Nenhum serviço encontrado</td></tr>`;
      return;
    }

    servicos.forEach(servico => {
      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${servico.modelo}</td>
        <td>${servico.servico}</td>
        <td>${servico.cliente}</td>
        <td>${servico.data}</td>
        <td>R$ ${servico.valor}</td>
        <td>${servico.status}</td>
        <td>
          <button onclick="editar('${servico.id}')">Editar</button>
          <button onclick="deletar('${servico.id}')">Deletar</button>
        </td>
      `;

      tbody.appendChild(tr);
    });

  } catch (error) {
    console.error(error);
    tbody.innerHTML = `<tr><td colspan="7">Erro ao carregar serviços</td></tr>`;
  }
}

// ✏️ EDITAR (SEM DATA)
async function editar(id) {

  const novoModelo = prompt("Novo modelo:");
  const novoServico = prompt("Novo serviço:");
  const novoValor = parseFloat(prompt("Novo valor:"));
  const novoStatus = prompt("Novo status:");

  if (!novoModelo || !novoServico || isNaN(novoValor) || !novoStatus) return;

  try {
    const res = await fetch(`${API}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        modelo: novoModelo,
        servico: novoServico,
        valor: novoValor,
        status: novoStatus
      })
    });

    if (!res.ok) {
      throw new Error("Erro ao atualizar serviço");
    }

    carregarServicos();

  } catch (error) {
    console.error(error);
    alert("Erro ao atualizar serviço");
  }
}

// 🗑️ DELETAR
async function deletar(id) {

  if (!confirm("Deseja deletar este serviço?")) return;

  try {
    const res = await fetch(`${API}/${id}`, {
      method: "DELETE"
    });

    if (!res.ok) {
      throw new Error("Erro ao deletar serviço");
    }

    carregarServicos();

  } catch (error) {
    console.error(error);
    alert("Erro ao deletar serviço");
  }
}