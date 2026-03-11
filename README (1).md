# 🌐 LINGUA.AI — Language Translation Tool

A clean, AI-powered language translation web app built with **Python**, **Flask**, and **Groq (LLaMA 3.3)**. Supports 25 languages with auto-detection, text-to-speech, and a minimal black & white UI.

---

## 📸 Preview

> Run the app locally and open `http://127.0.0.1:5000` to see it in action.

---

## ✨ Features

- 🌍 Translate between **25 languages**
- 🔍 **Auto-detect** source language
- 🔁 **Swap** source and target languages instantly
- 📋 **Copy** translated text with one click
- 🔊 **Text-to-speech** for translated output
- ⌨️ **Ctrl+Enter** shortcut to translate
- ⚡ Fast responses powered by **Groq + LLaMA 3.3 70B**

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Python, Flask           |
| AI Model  | LLaMA 3.3 70B via Groq  |
| Frontend  | HTML, CSS, JavaScript   |
| Styling   | IBM Plex Mono font      |

---

## 📁 Project Structure

```
translation/
├── app.py                  ← Flask backend + Groq API
├── requirements.txt        ← Python dependencies
├── README.md               ← You are here
├── templates/
│   └── index.html          ← Frontend (HTML + CSS + JS)
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/lingua-ai.git
cd lingua-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a free Groq API key
- Go to 👉 https://console.groq.com
- Sign up → **API Keys** → **Create API Key**
- Copy the key

### 4. Add your API key
Open `app.py` and replace line 8:
```python
client = Groq(api_key="YOUR_GROQ_API_KEY_HERE")
```

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 🌐 Supported Languages

`English` `Spanish` `French` `German` `Italian` `Portuguese` `Russian`
`Japanese` `Chinese (Simplified)` `Chinese (Traditional)` `Korean`
`Arabic` `Hindi` `Bengali` `Urdu` `Turkish` `Dutch` `Polish`
`Swedish` `Greek` `Hebrew` `Thai` `Vietnamese` `Indonesian`

---

## ⚠️ Important

- Never commit your API key to GitHub
- The Groq free tier is generous — no credit card required
- For production use, store the key in an environment variable

---

## 📄 License

This project was built as part of the **SoftGrowTech AI Internship Program**.

---

<p align="center">Built with ❤️ for SoftGrowTech Internship</p>
