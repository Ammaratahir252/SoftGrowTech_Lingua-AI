# LINGUA.AI — Language Translation Tool
## SoftGrowTech Internship · Task 1

---

## Project Structure

```
task1_translation/
├── app.py                  ← Flask backend (Python)
├── requirements.txt        ← Python dependencies
├── templates/
│   └── index.html          ← HTML template (Jinja2)
└── static/
    ├── css/
    │   └── style.css       ← All styles (black/white theme)
    └── js/
        └── main.js         ← Frontend JavaScript logic
```

---

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your Anthropic API key
**Windows (CMD):**
```cmd
set ANTHROPIC_API_KEY=your_api_key_here
```
**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="your_api_key_here"
```
**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## Features
- 25 supported languages
- Auto language detection
- Swap source ↔ target languages
- Copy translated text
- Text-to-speech playback
- Ctrl+Enter keyboard shortcut to translate
- Character counter (max 2000)
- Clean black & white theme
