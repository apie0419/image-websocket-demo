from flask import Flask
from streamer import Streamer
import time

app = Flask(__name__)

@app.route("/Open", methods=["POST"])
def Open():
    Streamer("localhost", 8765).start()
    
    return "success"

if __name__ == "__main__":
    app.run(host="localhost", port=5000, threaded=True, debug=True)