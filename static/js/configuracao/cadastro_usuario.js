const form = document.getElementById("form-usuario")

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const usuario = {
        nome: document.getElementById("nome").value,
        email: document.getElementById("email").value,
        senha: document.getElementById("senha").value
    }

    try {
        const res = await fetch("http://127.0.0.1:8000/usuario/", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(usuario)
        });

        if (!res.ok) {
            throw new Error("Erro na API ao cadastrar usuario");
        }

        const data = await res.json();
        console.log("Cadastrado com sucesso!");
        form.reset();

        window.location.href = "/html/dashboard";

    } catch (err) {
        console.error("Erro ao cadastrar cliente:", err);
        alert("erro ao cadastrar cliente")
    }
});