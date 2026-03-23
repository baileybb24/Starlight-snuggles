from flask import Flask, Response
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Starlight Snuggles Radio is live ✨"

@app.route("/stream")
def stream():
    def generate():
        while True:
            # silent stream (keeps connection alive)
            yield b"\0" * 1024
            time.sleep(0.1)

    return Response(generate(), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
