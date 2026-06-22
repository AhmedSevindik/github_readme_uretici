# 🤖 GitHub README Üretici / GitHub README Generator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude%20AI-orange.svg)](https://anthropic.com)
[![GitHub API](https://img.shields.io/badge/GitHub-API%20v3-black.svg)](https://docs.github.com/en/rest)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Hakkında / About

**TR:** GitHub repolarınızı otomatik olarak analiz eden ve yapay zeka destekli profesyonel README.md dosyaları üreten bir Python uygulaması.

**EN:** A Python application that automatically analyzes your GitHub repositories and generates professional README.md files powered by Claude AI.

---

## ✨ Özellikler / Features

**TR:**
- 🔍 GitHub repo URL'sinden otomatik kod analizi
- 🧠 Anthropic Claude AI ile akıllı README üretimi
- 📂 Önemli dosyaları otomatik tespit etme
- 📝 Türkçe ve İngilizce README desteği
- 🚀 Üretilen README'yi direkt repoya push etme
- ⚡ Hızlı ve kolay kullanım

**EN:**
- 🔍 Automatic code analysis from GitHub repo URL
- 🧠 Smart README generation with Anthropic Claude AI
- 📂 Automatic detection of important files
- 📝 Turkish and English README support
- 🚀 Direct push of generated README to repository
- ⚡ Fast and easy to use

---

## 🛠️ Kullanılan Teknolojiler / Technologies Used

| Teknoloji | Açıklama / Description |
|-----------|----------------------|
| `Python 3.8+` | Ana programlama dili / Main programming language |
| `Anthropic Claude API` | README üretimi için yapay zeka / AI for README generation |
| `GitHub REST API v3` | Repo analizi ve dosya işlemleri / Repo analysis and file operations |
| `python-dotenv` | Ortam değişkeni yönetimi / Environment variable management |
| `requests` | HTTP istekleri / HTTP requests |

---

## 📋 Gereksinimler / Requirements

```
anthropic
requests
python-dotenv
```

---

## ⚙️ Kurulum / Installation

### TR: Adım Adım Kurulum

**1. Repoyu klonlayın:**
```bash
git clone https://github.com/kullanici_adi/github_readme_uretici.git
cd github_readme_uretici
```

**2. Sanal ortam oluşturun:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**3. Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

**4. Ortam değişkenlerini ayarlayın:**
```bash
cp .env.example .env
```

`.env` dosyasını düzenleyin:
```env
GITHUB_TOKEN=your_github_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

---

### EN: Step by Step Installation

**1. Clone the repository:**
```bash
git clone https://github.com/username/github_readme_uretici.git
cd github_readme_uretici
```

**2. Create virtual environment:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set environment variables:**
```bash
cp .env.example .env
```

Edit `.env` file:
```env
GITHUB_TOKEN=your_github_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

---

## 🔑 API Anahtarları / API Keys

### GitHub Token
1. GitHub → Settings → Developer Settings adresine gidin
2. **Personal access tokens** → **Tokens (classic)** seçin
3. `repo` ve `contents:write` izinlerini etkinleştirin
4. Oluşturulan token'ı `.env` dosyasına ekleyin

### Anthropic API Key
1. [console.anthropic.com](https://console.anthropic.com) adresine gidin
2. API Keys bölümünden yeni bir anahtar oluşturun
3. Oluşturulan anahtarı `.env` dosyasına ekleyin

---

## 🚀 Kullanım / Usage

### TR: Kullanım

```bash
python main.py
```

Program çalıştığında:
```
GitHub repo URL gir: https://github.com/kullanici/repo-adi
```

URL girdikten sonra:
1. ✅ Repo otomatik analiz edilir
2. ✅ Önemli dosyalar tespit edilir
3. ✅ Claude AI ile README üretilir
4. ✅ README repoya push edilir

---

### EN: Usage

```bash
python main.py
```

When the program runs:
```
GitHub repo URL gir: https://github.com/username/repo-name
```

After entering the URL:
1. ✅ Repo is automatically analyzed
2. ✅ Important files are detected
3. ✅ README is generated with Claude AI
4. ✅ README is pushed to the repository

---

## 📁 Proje Yapısı / Project Structure

```
github_readme_uretici/
│
├── 📄 main.py              # Ana uygulama / Main application
├── 📄 github_api.py        # GitHub API işlemleri / GitHub API operations
├── 📄 readme_uretici.py    # Claude AI README üretici / Claude AI README generator
├── 📄 .env                 # Ortam değişkenleri / Environment variables (git ignored)
├── 📄 .env.example         # Örnek env dosyası / Example env file
├── 📄 requirements.txt     # Python bağımlılıkları / Python dependencies
└── 📄 README.md            # Bu dosya / This file
```

---

## 🔄 Nasıl Çalışır / How It Works

```
URL Girişi          GitHub API          Claude AI           Repo
    │                   │                   │                │
    │──── URL ─────────▶│                   │                │
    │                   │── Dosya Listesi ──▶│                │
    │                   │── Dosya İçerikleri▶│                │
    │                   │                   │── README Üret ─▶│
    │                   │                   │                │
    │◀────────────────────── README.md ─────────────────────│
```

---

## ⚠️ Önemli Notlar / Important Notes

> **TR:** `.env` dosyasını asla GitHub'a push etmeyin. `.gitignore` dosyanıza `.env` eklediğinizden emin olun.

> **EN:** Never push your `.env` file to GitHub. Make sure to add `.env` to your `.gitignore` file.

```gitignore
# .gitignore
.env
__pycache__/
venv/
*.pyc
```

---

## 🤝 Katkıda Bulunma / Contributing

**TR:** Katkılarınızı bekliyoruz!
1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değiş