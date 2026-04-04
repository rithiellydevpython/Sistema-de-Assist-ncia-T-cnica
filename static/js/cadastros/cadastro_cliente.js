const form = document.getElementById("form-cliente");
form.addEventListener("submit", async function(event){
    event.preventDefault();

    const cliente = {
        nome: document.getElementById("nome-cliente").value,
        numero: document.getElementById("numero-cliente").value,
        endereco: document.getElementById("endereco-cliente").value,
        cpf: document.getElementById("cpf-cliente").value
    };

    try {
        const res = await fetch("http://127.0.0.1:8000/clients/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(cliente)
        });

        const data = await res.json();
        console.log(data.message, "ID:", data.user_id);
        form.reset();
    } catch (err) {
        console.error("Erro ao cadastrar cliente:", err);
    }
});