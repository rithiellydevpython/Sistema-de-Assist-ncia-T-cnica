const API = "http://127.0.0.1:8000/services";
const API_CLIENTES = "http://127.0.0.1:8000/clients";

const form = document.getElementById("form-servico");
const inputModelo = document.getElementById("modelo-servico");
const inputServico = document.getElementById("servico-realizado");
const selectCliente = document.getElementById("cliente-servico");
const inputData = document.getElementById("data-servico");
const inputValor = document.getElementById("valor-servico");
const selectStatus = document.getElementById("status-servico");

async function carregarClientes() {
    try {
        const res = await fetch(API_CLIENTES);

        if (!res.ok) throw new Error("Erro ao buscar clientes");

        const data = await res.json();

        console.log("CLIENTES API:", data); // 👈 DEBUG IMPORTANTE

        const clientes = Array.isArray(data) ? data : data.clientes;

        selectCliente.innerHTML = `<option value="">Selecione um cliente</option>`;

        clientes.forEach(cliente => {
            const option = document.createElement("option");

            option.value = cliente.id;
            option.textContent = `${cliente.name} - ${cliente.cpf}`;

            selectCliente.appendChild(option);
        });

    } catch (error) {
        console.error("Erro ao carregar clientes:", error);
    }
}

form.addEventListener("submit", async function (event){
    event.preventDefault();

    const clientId = parseInt(selectCliente.value);
    const valor = parseFloat(inputValor.value);

    if (
        !inputModelo.value ||
        !inputServico.value ||
        isNaN(clientId) ||
        isNaN(valor) ||
        !inputData.value ||
        !selectStatus.value
    ) {
        alert("Preencha todos os campos corretamente!");
        return;
    }

    const servico = {
        model: inputModelo.value,
        description: inputServico.value,
        client_id: clientId, 
        date: inputData.value,
        value: valor,
        status: selectStatus.value
    };

    console.log("ENVIANDO:", servico);

    try {
        const res = await fetch(API, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(servico)
        });

        if (!res.ok) {
            const erro = await res.text();
            console.error("Erro backend:", erro);
            throw new Error();
        }

        alert("Serviço cadastrado com sucesso!");
        form.reset();

    } catch (error) {
        console.error(error);
        alert("Erro ao cadastrar serviço");
    }
});

window.onload = carregarClientes;
