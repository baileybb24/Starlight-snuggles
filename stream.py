import subprocess
from flask import Flask, Response

app = Flask(__name__)

current_process = None

def generate():
    global current_process
    if current_process:
        for chunk in iter(lambda: current_process.stdout.read(1024), b''):
            yield chunk

@app.route("/stream")
def stream():
    return Response(generate(), mimetype="audio/mpeg")

def play_song(url):
    global current_process

    if current_process:
        current_process.kill()

    command = [
        "yt-dlp",
        "-o", "-",
        "-f", "bestaudio",
        url
    ]

    current_process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
