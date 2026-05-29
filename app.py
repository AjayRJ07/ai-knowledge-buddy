from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from dotenv import load_dotenv
from pathlib import Path
import os, json
from google import genai
from google.genai import types
from data import QUIZ, LESSONS

load_dotenv(Path(__file__).parent / ".env")

app = Flask(__name__)

GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL      = "gemini-3.1-flash-lite"
SYSTEM     = """You are Buddy, an AI knowledge companion for Data Scientists.
Be friendly, concise (3-5 sentences), and encouraging.
Use data science analogies. Always suggest a follow-up question.
Topics: AI/ML fundamentals, Python (Pandas, Sklearn, PyTorch), LLMs, RAG, MLOps, AI ethics."""

def get_client():
    return genai.Client(api_key=GEMINI_KEY)

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", lessons=LESSONS, quiz_count=len(QUIZ))

@app.route("/api/chat", methods=["POST"])
def chat():
    data    = request.json
    history = data.get("history", [])   # list of {role, content}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Empty message"}), 400

    client = get_client()

    # Build Gemini contents: history + new user message
    # Gemini roles: "user" or "model" only
    contents = []
    for m in history:
        role = "model" if m["role"] in ("model", "assistant") else "user"
        contents.append({"role": role, "parts": [{"text": m["content"]}]})
    contents.append({"role": "user", "parts": [{"text": message}]})

    def generate():
        try:
            stream = client.models.generate_content_stream(
                model=MODEL,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM,
                    temperature=0.7,
                    max_output_tokens=800,
                ),
            )
            for chunk in stream:
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )

@app.route("/api/quiz")
def quiz():
    return jsonify(QUIZ)

@app.route("/api/lessons")
def lessons():
    safe = [{k: v for k, v in l.items() if k != "code"} for l in LESSONS]
    return jsonify(safe)

@app.route("/api/lessons/<int:idx>")
def lesson_detail(idx):
    if 0 <= idx < len(LESSONS):
        return jsonify(LESSONS[idx])
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    if not GEMINI_KEY:
        print("\n  ✗  GEMINI_API_KEY not set!")
        print("  Create a .env file with:  GEMINI_API_KEY=AIzaSy...\n")
    else:
        print("\n  ✓  Buddy is running → http://localhost:5000\n")
    app.run(debug=True, port=5000)
