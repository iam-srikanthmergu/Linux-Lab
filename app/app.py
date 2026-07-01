from flask import Flask
import logging
import os
import time
from datetime import datetime

app = Flask(__name__)

# Create logs directory
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@app.route("/")
def home():
    logging.info("Home page accessed")
    return f"""
    <h1>Linux Production Demo Application</h1>
    <h3>Status : Running ✅</h3>
    <p>Time : {datetime.now()}</p>
    """

@app.route("/health")
def health():
    logging.info("Health Check")
    return {
        "status": "UP",
        "application": "Linux Demo",
        "time": str(datetime.now())
    }

@app.route("/slow")
def slow():
    logging.warning("Slow endpoint called")
    time.sleep(10)
    return "Response after 10 seconds"

@app.route("/error")
def error():
    logging.error("Application Error Generated")
    return "Error Logged"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)