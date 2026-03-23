from flask import Flask, Response

app = Flask(__name__)

@app.route("/stream")
def stream():
    def generate():
        while True:
            with open("sample.mp3", "rb") as f:
                data = f.read(1024)
                if not data:
                    break
                yield data
    return Response(generate(), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
