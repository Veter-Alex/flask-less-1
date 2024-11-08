function redirectToUserPage() {
    const userInput = document.getElementById("user-input").value;
    window.location.href = `/user/${userInput}`;
}

function getfoldertree() {
    const folderPath = document.getElementById("folder-path").value;
    window.location.href = `/tree/${folderPath}`;
}