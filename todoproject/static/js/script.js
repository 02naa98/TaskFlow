// main.js
document.addEventListener("DOMContentLoaded", () => {
    const displayElement = document.querySelector(".display-a");

    if (displayElement) {
        displayElement.addEventListener("click", () => {
            // ランダムな色に変更
            displayElement.style.color = getRandomColor();
        });
    }
});

// ランダムな色を生成する関数
function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}


                                        //base.html//
// モーダル関連の要素
var modal = document.getElementById("imageModal");
var modalImg = document.getElementById("modalImage");
var captionText = document.getElementById("caption");
var closeModal = document.getElementById("closeModal");

// 画像をクリックしたときにモーダルを表示
document.getElementById("image-1").onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;  // クリックした画像のsrcをモーダル内に表示
    captionText.innerHTML = this.alt;  // 画像のaltテキストをキャプションとして表示
}

// モーダルを閉じる
closeModal.onclick = function() {
    modal.style.display = "none";
}

// モーダルの外をクリックした場合にも閉じる
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
                                        //base.html//
                                        //profile.html//
function togglePassword() {
    var passwordField = document.getElementById("password");
    var button = document.querySelector('.password-container button');
    if (passwordField.type === "password") {
        passwordField.type = "text"; // パスワードを表示
        button.textContent = "Hide"; // ボタンのテキストを変更
    } else {
        passwordField.type = "password"; // パスワードを隠す
        button.textContent = "Show"; // ボタンのテキストを変更
    }
}
                                        //profile.html//
                                        //task_list.html//
// タスク削除確認
function confirmDeleteTask() {
    return confirm("本当に削除しますか？");
}

// リスト削除確認
function confirmDeleteList() {
    return confirm("このリストを削除しますか？ このリスト上のすべてのタスクが完全に削除されます。");
}

// マウスオーバー時にボーダーを表示
function showBorder(element) {
    const allContainers = document.querySelectorAll('.list-container','.Sortable');
    allContainers.forEach(container => {
        container.style.border = 'none'; // すべてのボーダーを削除
    });

    // 選択された要素にボーダーを追加
    element.style.boxShadow = "0 2px 5px rgba(0, 123, 255, 0.5)"; // 青色の影を追加
}

// マウスアウト時にボーダーを非表示
function hideBorder(element) {
    element.style.border = "none"; // 元の枠線の色
    element.style.boxShadow = 'none'; // 影を削除
}


                                        //task_list.html//
                                        //task_create.html//
// セッションストレージからメッセージを取得
const message = sessionStorage.getItem('message');

// メッセージが存在する場合、アラートを表示
if (message) {
    alert(message);
    sessionStorage.removeItem('message'); // メッセージを表示後に削除
}
                                        //task_create.html//