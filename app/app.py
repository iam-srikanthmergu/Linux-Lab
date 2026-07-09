from flask import Flask, jsonify
import logging
import os
import time
import socket
import random
import platform
from datetime import datetime

app = Flask(__name__)

START_TIME = time.time()

# -----------------------------
# Logging Configuration
# -----------------------------
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

HOSTNAME = socket.gethostname()


@app.before_request
def log_request():
    logging.info("New request received")


# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    logging.info("Home page accessed")

    uptime = int(time.time() - START_TIME)

    return f"""
    <html>
    <head>
        <title>Linux Production Demo</title>
    </head>

    <body style="font-family:Arial;padding:30px;background:#f4f4f4;">

        <h1>🚀 Linux Production Demo Application</h1>

        <h3 style="color:green;">
            Status : RUNNING ✅
        </h3>

        <hr>

        <h2>Application Information</h2>

        <table border="1" cellpadding="8">

        <tr>
            <td><b>Application</b></td>
            <td>Linux Production Demo</td>
        </tr>

        <tr>
            <td><b>Server</b></td>
            <td>{HOSTNAME}</td>
        </tr>

        <tr>
            <td><b>Platform</b></td>
            <td>{platform.system()} {platform.release()}</td>
        </tr>

        <tr>
            <td><b>Current Time</b></td>
            <td>{datetime.now()}</td>
        </tr>

        <tr>
            <td><b>Uptime</b></td>
            <td>{uptime} Seconds</td>
        </tr>

        </table>

        <br>

        <p>
        Created by <b>Srikanth Mergu</b> to practice
        Linux Administration, DevOps,
        Production Support,
        Troubleshooting,
        Monitoring,
        and Incident Management.
        </p>

        <hr>

        <h2>Available Endpoints</h2>

        <ul>
            <li>/health</li>
            <li>/info</li>
            <li>/metrics</li>
            <li>/slow</li>
            <li>/error</li>
            <li>/random</li>
        </ul>

    </body>
    </html>
    """


# -----------------------------
# Health Check
# -----------------------------
@app.route("/health")
def health():
    logging.info("Health endpoint called")

    return jsonify({
        "status": "UP",
        "application": "Linux Demo",
        "hostname": HOSTNAME
    })


# -----------------------------
# System Information
# -----------------------------
@app.route("/info")
def info():
    logging.info("System info requested")

    return jsonify({
        "hostname": HOSTNAME,
        "os": platform.system(),
        "release": platform.release(),
        "python_version": platform.python_version()
    })


# -----------------------------
# Metrics
# -----------------------------
@app.route("/metrics")
def metrics():

    uptime = int(time.time() - START_TIME)

    logging.info("Metrics requested")

    return jsonify({
        "uptime_seconds": uptime,
        "hostname": HOSTNAME,
        "status": "Healthy"
    })


# -----------------------------
# Slow API
# -----------------------------
@app.route("/slow")
def slow():

    logging.warning("Slow endpoint invoked")

    time.sleep(10)

    return "Response received after 10 seconds"


# -----------------------------
# Error Endpoint
# -----------------------------
@app.route("/error")
def error():

    logging.error("Simulated application error")

    return "Application Error Logged", 500


# -----------------------------
# Random Failure
# -----------------------------
@app.route("/random")
def random_error():

    if random.randint(1, 2) == 1:
        logging.error("Random failure occurred")
        return "Internal Server Error", 500

    logging.info("Random endpoint succeeded")

    return "Application Working Successfully"


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
