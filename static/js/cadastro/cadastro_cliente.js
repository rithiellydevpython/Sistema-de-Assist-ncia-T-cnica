const form = document.getElementById("form-cliente");

// Pegando dados do LocalStorage
let clientes = JSON.parse(localStorage.getItem("clientes")) || [];

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    // Criando objeto com os dados do formulário
    const cliente = {
        name: document.getElementById("nome-cliente").value,
        number: document.getElementById("numero-cliente").value,
        address: document.getElementById("endereco-cliente").value,
        cpf: document.getElementById("cpf-cliente").value
    };

    // const cliente = {
    //     name: document.getElementById("nome").value,
    //     number: document.getElementById("numero").value,
    //     address: document.getElementById("endereco").value,
    //     cpf: document.getElementById("cpf").value
    // };

    // Salvando no LocalStorage
    clientes.push(cliente);
    localStorage.setItem("clientes", JSON.stringify(clientes));

    try {
        // Enviando para o backend
        const res = await fetch("http://127.0.0.1:8000/clients/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(cliente)
        });

        if (!res.ok) {
            const erro = await res.json();
            console.log("Erro detalhado completo:", JSON.stringify(erro, null, 2));
            throw new Error("Erro na API ao cadastrar cliente");
        }


        const data = await res.json();
        console.log("Cadastrado com sucesso! ID:", data.user_id);

        alert("Cliente cadastrado com sucesso!");
        form.reset();

        // Redirecionando para dashboard
        window.location.href = "/html/dashboard";

    } catch (err) {
        console.error("Erro ao cadastrar cliente:", err);
        alert("Erro ao cadastrar cliente. Veja o console para detalhes.");
    }
});