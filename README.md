# local_repo_qrcode_fixed_github

這是一個本地可執行的小系統：

- 主頁有一個按鈕
- 按下後顯示固定 GitHub 帳號主頁的 QRCode
- GitHub 帳號可由 `.env` 或系統環境變數 `GITHUB_USERNAME` 設定

## 啟動

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set GITHUB_USERNAME=mosguo
uvicorn app:app --reload
```

開啟：
- http://127.0.0.1:8000

## 建立 local repo

```bash
git init
git add .
git commit -m "init fixed github qrcode system"
```
