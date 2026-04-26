const form = document.getElementById("form-venda");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
        model: document.getElementById("modelo-venda").value,
        date: document.getElementById("data-venda").value,
        value: parseFloat(document.getElementById("valor-venda").value),
        marca: document.getElementById("marca-venda").value
    };

    console.log(dados);

    console.log(typeof dados.date, dados.date);


    try {    
        const res = await fetch("http://127.0.0.1:8000/vendas/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const result = await res.json();
        console.log(result);

        alert("Venda cadastrada com sucesso!");

    } catch (error) {
        console.error("Erro:", error);
        alert("Erro ao cadastrar venda");
    }
});