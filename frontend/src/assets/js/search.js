export default function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault(); // フォームのデフォルトの送信を停止
  
        // 検索キーワードを取得
        var keyword = document.getElementById('searchInput').value;
  
        // 検索結果に応じてページを開く
        var pageUrl = keyword + '.html'; // 入力された値に.htmlを追加してページURLを生成
  
        // ページが存在するかチェック
        fetch(pageUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Page not found');
                }
                // ページが存在する場合は遷移
                window.location.href = pageUrl;
            })
            .catch(() => { // unused variable警告を回避するために _ を使用
                // ページが存在しない場合はアラートを表示
                alert('該当するページが見つかりません。');
            });
    });
  }
  