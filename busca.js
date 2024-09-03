function realizarBusca() {
    var termo = document.getElementById("busca").value.toLowerCase();
    var conteudo = document.body.innerText.toLowerCase();

    if (conteudo.includes(termo)) {
        document.getElementById("mostrarResultados").innerText = "A palavra/frase foi encontrada!";
    } else {
        document.getElementById("mostrarResultados").innerText = "A palavra/frase não foi encontrada.";
    }

    document.getElementById("resultados").style.display = "block";
}