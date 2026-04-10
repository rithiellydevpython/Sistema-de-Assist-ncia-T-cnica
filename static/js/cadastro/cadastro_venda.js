const form = document.getElementById("form-venda");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
        model: document.getElementById("model").value,
        description: document.getElementById("description").value,
        client_id: parseInt(document.getElementById("client_id").value),
        date: document.getElementById("date").value,
        value: parseFloat(document.getElementById("value").value),
        status: document.getElementById("status").value
    };

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