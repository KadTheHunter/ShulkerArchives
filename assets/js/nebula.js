function nebulaEntry() {
    var confirmPassword = atob("UHJhaXNlIFZlc3Blcg==");
    var password = document.getElementById("search").value;
    if (password == confirmPassword) {
         window.location="html/KædykosNebula.html";
    }
}