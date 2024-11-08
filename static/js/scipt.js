function redirectToUserPage() {
    const userInput = document.getElementById("user-input").value;
    window.location.href = `/user/${userInput}`;
}

function getFolderTree(dirPath) {
    const folderList = [];

    const dirs = fs.readdirSync(dirPath);
    dirs.forEach((dir) => {
        const dirPath = path.join(dirPath, dir);
        const stats = fs.statSync(dirPath);
        if (stats.isDirectory()) {
            folderList.push(dirPath);
            const subDirs = getFolderTree(dirPath);
            folderList.push(...subDirs);
        }
    });

    return folderList;
}