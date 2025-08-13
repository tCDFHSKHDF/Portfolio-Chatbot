from flask import Flask, request, jsonify, send_from_directory
import os
from bot_engine import get_bot_response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    static_url_path="/static",   # so /static/... works
)

@app.route("/")
def home():
    # Serve your main portfolio page
    return send_from_directory(STATIC_DIR, "index.html")

@app.post("/chat")
def chat():
    try:
        data = request.get_json(force=True) or {}
        user_message = (data.get("message") or "").strip()
        if not user_message:
            return jsonify({"reply": "Please type a message."})
        reply = get_bot_response(user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"}), 200

@app.get("/download_resume")
def download_resume():
    filename = "Tariq_Ahmad_Resume.pdf"  # keep this exact name in /static
    file_path = os.path.join(STATIC_DIR, filename)
    if not os.path.exists(file_path):
        return f"File '{filename}' not found in /static.", 404
    # as_attachment forces browser to download
    return send_from_directory(STATIC_DIR, filename, as_attachment=True)

# Optional: serve any other static files safely
@app.route("/<path:filename>")
def static_passthrough(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == "__main__":
    # Run on 127.0.0.1:5000 (Flask dev server)
    app.run(debug=True)
