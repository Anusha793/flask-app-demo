from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a simple counter metric
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests count")

@app.route('/')
def home():
    REQUEST_COUNT.inc()  # Increment the counter for each request
    return "Hello from Azure Web App with Flask + Prometheus!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)