# 🤖 AI Knowledge Buddy — Flask Web App
### Data Scientist Edition · Powered by Google Gemini (Free)

A clean, dark web interface for the AI Knowledge Buddy. Built with Flask + vanilla JS.

## 🚀 Quick Start

### 1. Install dependencies
```cmd
pip install -r requirements.txt
```

### 2. Create your `.env` file
paste your key:
```
GEMINI_API_KEY=AIzaSy...your-key-here...
```
Get a free key (no card needed) → https://aistudio.google.com/apikey

### 3. Run the app
```cmd
python app.py
```
Open your browser → **http://localhost:5000**

---

## 📁 Project Structure

```
ai-buddy-flask/
├── app.py              ← Flask backend + Gemini API
├── data.py             ← Quiz questions & lesson content
├── templates/
│   └── index.html      ← Main UI template
├── static/
│   ├── style.css       ← Dark editorial design
│   └── app.js          ← Chat, quiz & lessons logic
├── requirements.txt
├── .env.example        ← Copy to .env and add your key
└── README.md
```
