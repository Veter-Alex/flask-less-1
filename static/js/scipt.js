function redirectToUserPage() {
    const userInput = document.getElementById("other-page").value;
    window.location.href = userInput;
}

function enter_with_username() {
    const username = document.getElementById("username").value;
    window.location.href = `/?name=${username}`;
}
function getFolderTree() {
    const folderList = [];
    const rootDir = document.getElementById("folder-path").value;

    // получаем список директорий
    const dirs = fs.readdirSync(rootDir);
    // dirs.forEach((dir) => {
    //     const dirPath = path.join(rootDir, dir);
    //     const stats = fs.statSync(dirPath);
    //     if (stats.isDirectory()) {
    //         folderList.push(dirPath);
    //     }
    // });
    
    document.body.style.backgroundColor = "green"; // тест - меняем цвет фона на зеленый
    document.getElementById("tree-folder-list").innerHTML = dirs;
    // document.getElementById("tree-folder-list").innerHTML = folderList.join("<br>");
}