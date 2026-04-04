document.querySelector("form").addEventListener("submit", function(e) {
    e.preventDefault();

    // Marca como logado
    localStorage.setItem("logado", "true");

    // Redireciona pro dashboard
    window.location.href = "/dashboard.html";
});