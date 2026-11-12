document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("form-filtro-vendas").addEventListener("submit", async (e) => {
        e.preventDefault();

        // const formulario = document.getElementById("form-filtro-vendas");
        const datainicio = document.getElementById("vendas-data-inicio").value;
        const datafim = document.getElementById("vendas-data-fim").value;
        const valorVendas = document.querySelector(".valor-vendas");

        const res = await fetch(`http://localhost:8000/relatorios/vendas?data_inicio=${datainicio}&data_fim=${datafim}`);
        const data = await res.json();

        valorVendas.textContent = `R$ ${data.total}`;
    }
    );


document.getElementById("form-filtro-os").addEventListener("submit", async (e) => {
    e.preventDefault();

    const status = document.getElementById("status-os").value;
    const dataInicio = document.getElementById("data-inicio-os").value;
    const dataFim = document.getElementById("data-fim-os").value;

    const totalOS = document.querySelector(".total-os");

    const parametros = new URLSearchParams();

    if (status) {
        parametros.append("status", status);
    }

    if (dataInicio) {
        parametros.append("data_inicio", dataInicio);
    }

    if (dataFim) {
        parametros.append("data_fim", dataFim);
    }

    try {
        const res = await fetch(
            `http://localhost:8000/relatorios/os?${parametros.toString()}`
        );

        if (!res.ok) {
            throw new Error("Erro ao consultar as ordens de serviço.");
        }

        const data = await res.json();

        totalOS.textContent = data.total;

    } catch (erro) {
        console.error("Erro:", erro);
    }
});

    document.getElementById("form-filtro-financas").addEventListener("submit", async (e) => {
        e.preventDefault();

        const tipo = document.getElementById("tipo-financa").value;

        const res = await fetch(`http://localhost:8000/relatorios/financas?tipo=${tipo}`);
        const data = await res.json();

        document.querySelector(".saldo-financas").textContent = `R$ ${data.saldo}`;
    });

});