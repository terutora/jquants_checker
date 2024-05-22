document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // フォームのデフォルトの送信を停止

    // 検索キーワードを取得
    var keyword = document.getElementById('searchInput').value;

    // 検索結果に応じてページを開く
    switch(keyword) {
        case '1301':
            window.location.href = '1301.html';
            break;
        case '企業コード2':
            window.location.href = 'page2.html';
            break;
        // 他の企業コードにも対応する場合はここに追加
        default:
            alert('該当するページが見つかりません。');
    }
});
