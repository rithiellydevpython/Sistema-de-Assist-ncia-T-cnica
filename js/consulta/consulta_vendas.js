const vendas = JSON.parse(localStorage.getItem("vendas")) || [];

const tbody = document.getElementById("tbody-venda");

vendas.forEach(function (venda) {
    const tr = document.createElement("tr");

    tr.innerHTML = `
        <td>${venda.marca}</td>
        <td>${venda.modelo}</td>
        <td>${venda.valor}</td>
        <td>${venda.data}</td>
    `;

    tbody.appendChild(tr);
});