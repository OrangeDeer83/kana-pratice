# 🇯🇵 五十音練習 (Kana Flashcards)

一個簡單易用的日文五十音（假名）練習桌面應用程式，支援平假名與片假名的學習與測驗。

## ✨ 功能特色

- 📝 **完整假名支援**：涵蓋平假名與片假名的清音、濁音/半濁音、拗音
- 🎯 **自訂練習範圍**：可自由選擇要練習的假名類型
- 🪟 **浮動視窗**：透明背景、置頂顯示，方便隨時練習
- 🔍 **縮放功能**：使用滑鼠滾輪調整字體大小
- 📊 **錯誤追蹤**：自動記錄答錯的假名，方便複習
- 🎨 **自訂外觀**：可切換文字顏色（黑/白）

## � 下載使用

### 方式一：直接下載執行檔（推薦）

前往 [Releases 頁面](../../releases) 下載最新版本的 `五十音練習.exe`，雙擊即可執行，無需安裝 Python。

### 方式二：從原始碼執行

## �🚀 快速開始

### 環境需求

- Python 3.8 或更高版本
- [uv](https://github.com/astral-sh/uv)（推薦）或 pip

### 安裝步驟

#### 方式 A：使用 uv（推薦）⚡

1. **安裝 uv**
   ```bash
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **克隆專案**
   ```bash
   git clone <repository-url>
   cd kana-pratice
   ```

3. **安裝依賴並執行**
   ```bash
   # uv 會自動建立虛擬環境並安裝依賴
   uv run python kana_quiz.py
   ```

#### 方式 B：使用傳統 pip

1. **克隆專案**
   ```bash
   git clone <repository-url>
   cd kana-pratice
   ```

2. **建立虛擬環境**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **安裝依賴**
   ```bash
   pip install -e .
   ```

4. **執行程式**
   ```bash
   python kana_quiz.py
   ```

## 🎮 使用說明

### 基本操作

1. **答題**：在輸入框中輸入假名的羅馬拼音，按 Enter 確認
2. **移動視窗**：左鍵拖曳視窗任意位置
3. **縮放**：使用滑鼠滾輪放大或縮小字體
4. **右鍵選單**：右鍵點擊開啟功能選單

### 右鍵選單功能

- **查看錯誤列表**：顯示所有答錯的假名記錄
- **選擇練習範圍**：勾選要練習的假名類型
  - 平假名_清音
  - 平假名_濁音/半濁音
  - 平假名_拗音
  - 片假名_清音
  - 片假名_濁音/半濁音
  - 片假名_拗音
- **文字顏色**：切換白色或黑色文字
- **關閉程式**：退出應用程式

### 答題反饋

- ✓ **綠色勾號**：答對，自動進入下一題
- ❌ **紅色錯誤訊息**：顯示正確答案與你的輸入對比

## 🛠️ 打包為執行檔

使用 PyInstaller 將程式打包為獨立執行檔：

```bash
# 安裝 PyInstaller（使用 uv）
uv pip install pyinstaller

# 或使用傳統 pip
pip install pyinstaller

# 打包（使用圖示）
pyinstaller --onefile --windowed --icon=kana.ico --name="五十音練習" kana_quiz.py

# 執行檔位於 dist/ 資料夾
```

## 📁 專案結構

```
kana-pratice/
├── kana_quiz.py          # 主程式
├── kana.ico              # 應用程式圖示
├── pyproject.toml        # 專案設定檔
├── README.md             # 說明文件
├── .gitignore            # Git 忽略清單
├── .python-version       # Python 版本指定
└── uv.lock               # UV 套件管理鎖定檔
```

## 🎯 假名涵蓋範圍

### 平假名
- **清音**：あ行、か行、さ行、た行、な行、は行、ま行、や行、ら行、わ行、ん
- **濁音/半濁音**：が行、ざ行、だ行、ば行、ぱ行
- **拗音**：きゃ、しゃ、ちゃ、にゃ、ひゃ、みゃ、りゃ、ぎゃ、じゃ、びゃ、ぴゃ 等

### 片假名
- **清音**：ア行、カ行、サ行、タ行、ナ行、ハ行、マ行、ヤ行、ラ行、ワ行、ン
- **濁音/半濁音**：ガ行、ザ行、ダ行、バ行、パ行
- **拗音**：キャ、シャ、チャ、ニャ、ヒャ、ミャ、リャ、ギャ、ジャ、ビャ、ピャ 等

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request 來改進這個專案！

## 📄 授權

本專案採用 MIT 授權條款。

## 💡 提示

- 建議從平假名清音開始練習，逐步增加難度
- 定期查看錯誤列表，針對弱項加強練習
- 可以調整視窗大小和位置，配合其他學習資源使用
