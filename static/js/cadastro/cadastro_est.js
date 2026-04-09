const form = document.getElementById("form-estoque");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const item = {
        marca: document.getElementById("marca-estoque").value,
        model: document.getElementById("modelo-estoque").value,
        code: document.getElementById("codigo-estoque").value,
        description: document.getElementById("descricao-estoque").value
    };

    console.log("Enviando item:", item); // 👈 AQUI

    try {
        const response = await fetch("http://127.0.0.1:8000/estoque/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(item)
        });

        console.log("Resposta:", response); // 👈 AQUI

        if (!response.ok) {
            throw new Error("Erro ao cadastrar");
        }

        const data = await response.json();
        console.log("Resposta do backend:", data);

        alert("Item cadastrado com sucesso!");
        form.reset();

    } catch (error) {
        console.error("Erro:", error);
        alert("Erro ao cadastrar item");
    }
});