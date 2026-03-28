const clientes = JSON.parse(localStorage.getItem("clientes")) || [];

const tbody = document.getElementById("tbody-cliente");

clientes.forEach(function (cliente){
    const tr = document.createElement("tr");

    tr.innerHTML = `
        <td>${cliente.nome}</td>
        <td>${cliente.numero}</td>
        <td>${cliente.endereco}</td>
        <td>${cliente.cpf}</td>
    `;

    tbody.appendChild(tr);
});