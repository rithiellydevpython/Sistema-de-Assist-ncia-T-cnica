const API = "http://127.0.0.1:8000/clients";

const tbody = document.getElementById("tbody-cliente");

window.onload = carregarClientes;

// 🔎 LISTAR CLIENTES
async function carregarClientes() {

  try {
    const res = await fetch(API);

    if (!res.ok) {
      throw new Error("Erro ao buscar clientes");
    }
 
    const data = await res.json();

    const clients = data.clientes; //importantissimo usar isso 

    tbody.innerHTML = "";

    if (!clients.length) {
      tbody.innerHTML = `<tr><td colspan="4">Nenhum cliente encontrado</td></tr>`;
      return;
    }

    clients.forEach(client => {
      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${client.name}</td>
        <td>${client.number}</td>
        <td>${client.address}</td>
        <td>${client.cpf}</td>
        <td>
          <button onclick="editarCliente('${client.cpf}')">Editar</button>
          <button onclick="deletarCliente('${client.cpf}')">Deletar</button>
        </td>
      `;

      tbody.appendChild(tr);
    });

  } catch (error) {
    console.error(error);
    tbody.innerHTML = `<tr><td colspan="4">Erro ao carregar clientes</td></tr>`;
  }
}


// ✏️ EDITAR CLIENTE
async function editarCliente(cpf) {
  const novoNome = prompt("Novo nome:");
  const novoTelefone = prompt("Novo telefone:");
  const novoEndereco = prompt("Novo endereço:");

  if (!novoNome || !novoTelefone || !novoEndereco) return;

  try {
    const res = await fetch(`${API}/${cpf}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: novoNome,
        number: novoTelefone,
        address: novoEndereco 
      })
    });

    if (!res.ok) {
      throw new Error("Erro ao atualizar cliente");
    }

    carregarClientes();

  } catch (error) {
    console.error(error);
    alert("Erro ao atualizar cliente");
  }
}


// 🗑️ DELETAR CLIENTE
async function deletarCliente(cpf) {

  if (!confirm("Deseja deletar este cliente?")) return;

  try {
    const res = await fetch(`${API}/${cpf}`, {
      method: "DELETE"
    });

    if (!res.ok) {
      throw new Error("Erro ao deletar cliente");
    }

    carregarClientes();

  } catch (error) {
    console.error(error);
    alert("Erro ao deletar cliente");
  }
}


