const servicos = JSON.parse(localStorage.getItem("servicos")) || [];

const tbody = document.getElementById("tbody-servico");

servicos.forEach(function (servico) {
  const tr = document.createElement("tr");

  tr.innerHTML = `
    <td>${servico.modelo}</td>
    <td>${servico.servico}</td>
    <td>${servico.cliente}</td>
    <td>${servico.data}</td>
    <td> R$ ${servico.valor}</td>
    <td>${servico.status}</td>
  `;

  tbody.appendChild(tr);
});



