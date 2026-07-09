from flask import Flask
import logging
import os
import time

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
    return """
    <h1>Linux Production Demo Application</h1>
    <h3>Status : Running ✅</h3>

    <p>
        Welcome to the Demo Lab.
    </p>

    <p>
        Created by <strong>Srikanth Mergu</strong> for learning
        Linux Administration, DevOps, and real-time production troubleshooting.
    </p>

    <hr>

    <h4>Available Endpoints</h4>

    <ul>
        <li>/health</li>
        <li>/slow</li>
        <li>/error</li>
    </ul>
    """

@app.route("/health")
def health():
    logging.info("Health Check")
    return {
        "status": "UP",
        "application": "Linux Demo"
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
