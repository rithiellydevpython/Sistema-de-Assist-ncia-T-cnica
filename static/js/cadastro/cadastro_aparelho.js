const form = document.getElementById("form-aparelho");

let devices = JSON.parse(localStorage.getItem("devices")) || [];

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const device = {
        code: document.getElementById("codigo-aparelho").value,
        marca: document.getElementById("marca-aparelho").value,
        modelo: document.getElementById("modelo-aparelho").value // 🔹 usar modelo
    };

    devices.push(device);
    localStorage.setItem("devices", JSON.stringify(devices));

    try {
        const res = await fetch("http://127.0.0.1:8000/devices/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(device)
        });

        if (!res.ok) {
            throw new Error(`Erro na requisição: ${res.status}`);
        }

        alert("Aparelho cadastrado com sucesso!");
        form.reset();

    } catch (error) {
        console.error("Erro ao cadastrar aparelho:", error);
    }
});


























