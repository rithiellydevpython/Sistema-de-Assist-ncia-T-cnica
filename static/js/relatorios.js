document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("form-filtro-vendas").addEventListener("submit", async (e) => {
        e.preventDefault();

        const inicio = document.getElementById("vendas-data-inicio").value;
        const fim = document.getElementById("vendas-data-fim").value;

        const res = await fetch(`http://localhost:8000/relatorios/vendas?data_inicio=${inicio}&data_fim=${fim}`);
        const data = await res.json();

        document.querySelector(".valor-vendas").textContent = `R$ ${data.total}`;
    });

    document.getElementById("form-filtro-os").addEventListener("submit", async (e) => {
        e.preventDefault();

        const status = document.getElementById("status-os").value;

        const res = await fetch(`http://localhost:8000/relatorios/os?status=${status}`);
        const data = await res.json();

        document.querySelector(".total-os").textContent = data.total;
    });

    document.getElementById("form-filtro-financas").addEventListener("submit", async (e) => {
        e.preventDefault();

        const tipo = document.getElementById("tipo-financa").value;

        const res = await fetch(`http://localhost:8000/relatorios/financas?tipo=${tipo}`);
        const data = await res.json();

        document.querySelector(".saldo-financas").textContent = `R$ ${data.saldo}`;
    });

});