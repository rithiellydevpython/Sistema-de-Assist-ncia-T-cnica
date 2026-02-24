const aparelhos = JSON.parse(localStorage.getItem("aparelhos")) || [];

const tbody = document.getElementById("tbody-aparelho");

aparelhos.forEach(function (aparelho) {
    const tr = document.createElement("tr");

    tr.innerHTML = `
        <td>${aparelho.codigo}</td>
        <td>${aparelho.marca}</td>
        <td>${aparelho.modelo}</td>
    `;

    tbody.appendChild(tr);
});