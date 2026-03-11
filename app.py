import json
import re
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Paste your Groq API key here
client = Groq(api_key="YOUR_GROQ_API_KEY_HERE")

LANGUAGES = [
    "Auto Detect", "English", "Spanish", "French", "German", "Italian",
    "Portuguese", "Russian", "Japanese", "Chinese (Simplified)",
    "Chinese (Traditional)", "Korean", "Arabic", "Hindi", "Bengali",
    "Urdu", "Turkish", "Dutch", "Polish", "Swedish", "Greek",
    "Hebrew", "Thai", "Vietnamese", "Indonesian"
]

@app.route("/")
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    source_text = data.get("text", "").strip()
    source_lang = data.get("source_lang", "Auto Detect")
    target_lang = data.get("target_lang", "Spanish")

    if not source_text:
        return jsonify({"error": "No text provided"}), 400

    if source_lang == "Auto Detect":
        # Ask for two separate lines instead of JSON to avoid parse issues
        prompt = f"""You are a professional translator.
Detect the language of the text below and translate it to {target_lang}.

Reply in EXACTLY this format with nothing else:
DETECTED: <language name>
TRANSLATION: <translated text>

Text:
{source_text}"""
    else:
        prompt = f"""You are a professional translator. Translate the following text from {source_lang} to {target_lang}.

Reply with ONLY the translated text. No explanations, no quotes, no extra words.

Text:
{source_text}"""

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )

    result_text = chat_completion.choices[0].message.content.strip()

    if source_lang == "Auto Detect":
        # Parse the DETECTED / TRANSLATION format
        detected = "Unknown"
        translation = result_text  # fallback

        detected_match = re.search(r"DETECTED:\s*(.+)", result_text)
        translation_match = re.search(r"TRANSLATION:\s*([\s\S]+)", result_text)

        if detected_match:
            detected = detected_match.group(1).strip()
        if translation_match:
            translation = translation_match.group(1).strip()

        return jsonify({"translation": translation, "detected": detected})
    else:
        return jsonify({"translation": result_text})

if __name__ == "__main__":
    app.run(debug=True)