import os
import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/images"
DATA_FILE = "memories.json"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------- LOAD MEMORIES FROM JSON --------
def load_memories():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# -------- ROUTES --------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/memories")
def memories():
    memories = load_memories()
    memories.reverse()  # latest first
    return render_template("view_memories.html", memories=memories)

@app.route("/uploads/images/<filename>")
def uploaded_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
