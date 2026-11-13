
const API = "http://127.0.0.1:8000/services";
const API_CLIENTES = "http://127.0.0.1:8000/clients/";

const form = document.getElementById("form-servico");
const inputModelo = document.getElementById("modelo-servico");
const inputServico = document.getElementById("servico-realizado");
const buscaCliente = document.getElementById("busca-cliente");
const selectCliente = document.getElementById("cliente-servico");
const listaClientes = document.getElementById("lista-clientes");
const inputData = document.getElementById("data-servico");
const inputValor = document.getElementById("valor-servico");
const selectStatus = document.getElementById("status-servico");

let clientesCarregados = [];

// CARREGAR CLIENTES DA API
async function carregarClientes() {
    try {
        const res = await fetch(API_CLIENTES);

        if (!res.ok) {
            throw new Error("Erro ao buscar clientes: " + res.status);
        }

        const data = await res.json();

        console.log("RESPOSTA DA API:", data);

        clientesCarregados = Array.isArray(data)
            ? data
            : data.clientes || [];

        console.log("CLIENTES CARREGADOS:", clientesCarregados);
        console.log("QUANTIDADE DE CLIENTES:", clientesCarregados.length);

    } catch (error) {
        console.error("ERRO AO CARREGAR CLIENTES:", error);
    }
}

// MOSTRAR E FILTRAR CLIENTES
function mostrarClientes(filtro = "") {

    console.log("FUNÇÃO MOSTRAR CLIENTES FOI CHAMADA");
    console.log("TOTAL DE CLIENTES:", clientesCarregados.length);

    listaClientes.innerHTML = "";

    const pesquisa = filtro.trim().toLowerCase();

    const resultado = clientesCarregados.filter(cliente => {

        const nome = String(cliente.name || "").toLowerCase();
        const cpf = String(cliente.cpf || "").toLowerCase();

        return nome.includes(pesquisa) || cpf.includes(pesquisa);
    });

    console.log("RESULTADO DA PESQUISA:", resultado);

    resultado.forEach(cliente => {

        const opcao = document.createElement("button");

        opcao.type = "button";
        opcao.textContent = `${cliente.name} - ${cliente.cpf}`;

        opcao.addEventListener("click", () => {

            buscaCliente.value = `${cliente.name} - ${cliente.cpf}`;

            selectCliente.value = cliente.id;

            listaClientes.style.display = "none";
        });

        listaClientes.appendChild(opcao);
    });

    listaClientes.style.display =
        resultado.length > 0 ? "block" : "none";

    console.log("ELEMENTOS CRIADOS:", listaClientes.innerHTML);
    console.log("ESTILO DA LISTA:", getComputedStyle(listaClientes).display);
    console.log("CLIENTES ENCONTRADOS:", resultado.length);
}

// ABRIR LISTA AO CLICAR NO CAMPO
buscaCliente.addEventListener("focus", () => {
    mostrarClientes(buscaCliente.value);
});

// PESQUISAR ENQUANTO DIGITA
buscaCliente.addEventListener("input", () => {

    selectCliente.value = "";

    mostrarClientes(buscaCliente.value);
});

// FECHAR LISTA AO CLICAR FORA
document.addEventListener("click", (event) => {

    if (
        !buscaCliente.contains(event.target) &&
        !listaClientes.contains(event.target)
    ) {
        listaClientes.style.display = "none";
    }
});

// CADASTRAR SERVIÇO
form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const clientId = parseInt(selectCliente.value);
    const valor = parseFloat(inputValor.value);

    if (
        !inputModelo.value.trim() ||
        !inputServico.value.trim() ||
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

            throw new Error("Erro ao cadastrar serviço");
        }

        alert("Serviço cadastrado com sucesso!");

        form.reset();

        selectCliente.value = "";
        listaClientes.style.display = "none";


    } catch (error) {

        console.error(error);

        alert("Erro ao cadastrar serviço");
    }
});

// INICIAR CARREGAMENTO DOS CLIENTES
carregarClientes();
