let temaBloqueado = false;
let usuario_id = 1;

// usuarios

async function carregarUsuarios() {
    try {
        const container = document.getElementById("lista-usuarios");
        
        // 1. Se não existir o container na página atual, para aqui mesmo em silêncio
        if (!container) return; 

        // 2. Agora sim faz a requisição
        const res = await fetch("/configuracoes/usuarios");

        if (!res.ok) {
            console.error("Erro HTTP usuários:", res.status);
            return;
        }

        const usuarios = await res.json();

        // 3. Limpa e preenche o container
        container.innerHTML = "";

        if (!usuarios || usuarios.length === 0) {
            container.innerHTML = "<p>Nenhum usuário encontrado</p>";
            return;
        }

        usuarios.forEach(u => {
            const card = document.createElement("div");
            card.classList.add("card");

            card.innerHTML = `
                <p><strong>${u.nome}</strong></p>
                <p>${u.email}</p>
                <p>${u.tipo_acesso}</p>

                <div class="card-actions">
                    <button class="btn-editar" onclick="editarUsuario(${u.id})">
                        Editar
                    </button>

                    <button class="btn-excluir" onclick="deletarUsuario(${u.id})">
                        Excluir
                    </button>
                </div>
            `;

            container.appendChild(card);
        });

    } catch (err) {
        console.error("Erro usuários:", err);
    }
}


async function editarUsuario(id) {
    const novoNome = prompt("Novo nome:");
    const novoEmail = prompt("Novo email:");
    const novoTipo = prompt("Tipo de acesso:");

    if (!novoNome || !novoEmail || !novoTipo) return;

    try {
        const res = await fetch(`/configuracoes/usuarios/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nome: novoNome,
                email: novoEmail,
                tipo_acesso: novoTipo
            })
        });

        if (!res.ok) {
            console.error("Erro ao editar usuário:", res.status);
            return;
        }

        carregarUsuarios();

    } catch (err) {
        console.error("Erro ao editar usuário:", err);
    }
}


async function deletarUsuario(id) {
    if (!confirm("Tem certeza que deseja excluir este usuário?")) return;

    try {
        const res = await fetch(`/configuracoes/usuarios/${id}`, {
            method: "DELETE"
        });

        if (!res.ok) {
            console.error("Erro ao deletar usuário:", res.status);
            return;
        }

        // recarrega lista
        carregarUsuarios();

    } catch (err) {
        console.error("Erro ao deletar usuário:", err);
    }
}

// Procure este bloco no seu usuario.js e adicione o "if"
const formUsuario = document.getElementById("form-usuario");

if (formUsuario) {
    formUsuario.addEventListener("submit", async function (e) {
        e.preventDefault();
        
        const nome = document.getElementById("nome").value;
        const email = document.getElementById("email").value;
        const senha = document.getElementById("senha").value;
        const tipo_acesso = document.getElementById("tipo_acesso").value;

        const res = await fetch("/configuracoes/usuarios", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nome, email, senha, tipo_acesso })
        });

        if (res.ok) {
            alert("Usuário criado com sucesso!");
            carregarUsuarios();
        } else {
            const err = await res.json();
            alert(err.detail || "Erro ao criar usuário");
        }
    });
}

// inicialização

document.addEventListener("DOMContentLoaded", async () => {
    await init();

    const formPref = document.getElementById("form-preferencias");
    if (formPref) {
        formPref.addEventListener("submit", async (e) => {
            e.preventDefault();
            await salvarPreferencias();
        });
    }
});

async function init() {
    await carregarUsuarios(); // agora espera carregar
    inicializarBackup();
    await inicializarPreferencias();
}

async function inicializarPreferencias() {
    await aplicarTemaGlobal();
    await carregarPreferenciasUI();
}

    
// fim


// =============================
// 🔥 PREFERÊNCIAS / TEMA
// =============================

async function aplicarTemaGlobal() {
    // 1. Tenta aplicar o tema IMEDIATAMENTE usando o que está gravado no navegador
    const temaSalvo = localStorage.getItem("tema_cache");
    if (temaSalvo) {
        document.body.classList.toggle("dark", temaSalvo === "escuro");
    }

    try {
        // 2. Busca no servidor para garantir que está atualizado
        const res = await fetch(`/configuracoes/preferencias/${usuario_id}`);
        if (res.ok) {
            const pref = await res.json();
            const novoTema = pref.tema.toLowerCase();

            // 3. Se o tema do servidor for diferente do cache, atualiza
            if (novoTema !== temaSalvo) {
                document.body.classList.toggle("dark", novoTema === "escuro");
                localStorage.setItem("tema_cache", novoTema);
            }
        }
    } catch (err) {
        console.error("Erro ao sincronizar tema:", err);
    }
}



async function carregarPreferenciasUI() {

    try {
        const res = await fetch(`/configuracoes/preferencias/${usuario_id}`);
        if (!res.ok) return;

        const pref = await res.json();

        const temaSelect = document.getElementById("tema");
        if (temaSelect) temaSelect.value = pref.tema;

        const notif = document.getElementById("notificacoes");
        if (notif) notif.checked = !!pref.notificacoes;

    } catch (err) {
        console.error("Erro ao carregar UI:", err);
    }
}

async function salvarPreferencias() {

    const dados = {
        tema: document.getElementById("tema").value,
        notificacoes: document.getElementById("notificacoes").checked
    };

    try {
        const res = await fetch(`/configuracoes/preferencias/${usuario_id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });

        if (!res.ok) {
            console.error("Erro salvar preferências:", res.status);
            throw new Error();
        }

        await aplicarTemaGlobal();

        showToast("Preferências salvas!", "success");

    } catch (err) {
        console.error(err);
        showToast("Erro ao salvar preferências", "error");
    }
}

// =============================
// 💾 BACKUP
// =============================

function inicializarBackup() {

    const btnBackup = document.getElementById("btnBackup");
    const btnRestaurar = document.getElementById("btnRestaurar");
    const inputBackup = document.getElementById("inputBackup");

    if (btnBackup) {
        btnBackup.addEventListener("click", () => {
            window.location.href = "/configuracoes/backup";
        });
    }

    if (btnRestaurar) {
        btnRestaurar.addEventListener("click", async () => {

            if (!inputBackup?.files?.length) {
                showToast("Selecione um backup!", "error");
                return;
            }

            const formData = new FormData();
            formData.append("file", inputBackup.files[0]);

            try {
                const res = await fetch("/configuracoes/restaurar", {
                    method: "POST",
                    body: formData
                });

                if (!res.ok) throw new Error();

                showToast("Backup restaurado!", "success");

                setTimeout(() => location.reload(), 1000);

            } catch (err) {
                console.error(err);
                showToast("Erro ao restaurar backup", "error");
            }
        });
    }
}

// =============================
// 🔔 TOAST
// =============================

function showToast(message, type = "info") {

    const toast = document.createElement("div");

    toast.textContent = message;

    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.padding = "12px 18px";
    toast.style.borderRadius = "8px";
    toast.style.color = "#fff";
    toast.style.zIndex = "9999";
    toast.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";

    toast.style.background =
        type === "success" ? "#2ecc71" :
        type === "error" ? "#e74c3c" :
        "#3498db";

    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 3000);
}