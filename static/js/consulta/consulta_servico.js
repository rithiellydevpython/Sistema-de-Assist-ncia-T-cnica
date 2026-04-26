console.log("JS consulta carregou");

const API = "http://127.0.0.1:8000/services";
const API_CLIENTES = "http://127.0.0.1:8000/clients";

const tbody = document.getElementById("tbody-servico");

// 🧠 mapa de clientes
let mapaClientes = {};


// 🚀 carregar clientes no mapa
async function carregarClientes() {
  try {
    const res = await fetch(API_CLIENTES);
    if (!res.ok) throw new Error();

    const data = await res.json();
    const clientes = data.clientes || [];

    mapaClientes = {}; // limpa antes

    clientes.forEach(cliente => {
      mapaClientes[cliente.id] = `${cliente.name} - ${cliente.cpf}`;
    });

  } catch (error) {
    console.error("Erro ao carregar clientes:", error);
  }
}


// 🚀 carregar serviços
async function carregarServicos() {

  await carregarClientes(); // 👈 importante

  try {
    const res = await fetch(API);
    if (!res.ok) throw new Error();

    const data = await res.json();
    const servicos = data.services || [];

    tbody.innerHTML = "";

    if (!servicos.length) {
      tbody.innerHTML = `<tr><td colspan="7">Nenhum serviço encontrado</td></tr>`;
      return;
    }

    servicos.forEach(servico => {
      const tr = document.createElement("tr");

      const nomeCliente = mapaClientes[servico.client_id] || "Desconhecido";

      tr.innerHTML = `
        <td>${servico.model}</td>
        <td>${servico.description}</td>
        <td>${nomeCliente}</td>
        <td>${servico.date}</td>
        <td>${servico.value}</td>
        <td>${servico.status}</td>
        <td>
          <button onclick='editar(${servico.id}, ${JSON.stringify(servico)})'>Editar</button>
          <button onclick="deletar(${servico.id})">Deletar</button>
        </td>
      `;

      tbody.appendChild(tr);
    });

  } catch (error) {
    console.error(error);
    tbody.innerHTML = `<tr><td colspan="7">Erro ao carregar serviços</td></tr>`;
  }
}


// ✏️ EDITAR
async function editar(id, servicoAtual) {

  const novoModelo = prompt("Novo modelo:", servicoAtual.model);
  const novoServico = prompt("Novo serviço:", servicoAtual.description);
  const novoValor = parseFloat(prompt("Novo valor:", servicoAtual.value));
  const novoStatus = prompt("Novo status:", servicoAtual.status);

  if (!novoModelo || !novoServico || isNaN(novoValor) || !novoStatus) return;

  try {
    const res = await fetch(`${API}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: novoModelo,
        description: novoServico,
        value: novoValor,
        status: novoStatus,
        client_id: servicoAtual.client_id, // 👈 necessário
        date: servicoAtual.date            // 👈 necessário
      })
    });

    if (!res.ok) throw new Error();

    carregarServicos();

  } catch (error) {
    console.error(error);
    alert("Erro ao atualizar serviço");
  }
}


// ❌ DELETAR
async function deletar(id) {

  if (!confirm("Deseja deletar este serviço?")) return;

  try {
    const res = await fetch(`${API}/${id}`, {
      method: "DELETE"
    });

    if (!res.ok) throw new Error();

    carregarServicos();

  } catch (error) {
    console.error(error);
    alert("Erro ao deletar serviço");
  }
}


// 🚀 iniciar
window.onload = carregarServicos;