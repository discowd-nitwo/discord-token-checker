# 🛡️ Discord Token Type Checker

A simple Flask web app that lets developers check whether a Discord token is a **bot** or a **user** token.

## 🔍 What It Does

- Accepts a Discord token through a web form
- Automatically determines if it's a bot or user token
- Pretty-prints the `/users/@me` API response
- Helpful for debugging or inspecting leaked tokens

## 🛠️ Tech Stack

- Python 3
- Flask
- Requests
- HTML + CSS (Jinja2 templates)

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/yourusername/discord-token-checker.git
cd discord-token-checker

    Install dependencies:

pip install -r requirements.txt

    Run the app:

python app.py

    Open your browser and go to:

http://localhost:5000

📁 Project Structure

discord-token-checker/
├── app.py
├── requirements.txt
└── templates/
    └── index.html

⚠️ Disclaimer

This tool is for educational and debugging purposes only. Do not use user tokens you don't own. Misuse may violate Discord’s Terms of Service.
📄 License

MIT License
```
