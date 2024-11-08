function redirectToUserPage() {
    const userInput = document.getElementById("user-input").value;
    window.location.href = `/user/${userInput}`;
}