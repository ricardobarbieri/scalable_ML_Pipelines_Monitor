from flask import Flask, render_template, jsonify
import random
import time
from threading import Thread
import numpy as np

app = Flask(__name__)

# Simulated real-time data storage
class PipelineMonitor:
    def __init__(self):
        self.data_processed = 0
        self.current_throughput = 0
        self.model_accuracy = 0.85
        self.latency = 0
        self.active_pipelines = 1
        
    def update_metrics(self):
        while True:
            self.data_processed += random.randint(100, 1000)
            self.current_throughput = random.uniform(50, 200)
            self.model_accuracy = min(0.99, max(0.75, self.model_accuracy + random.uniform(-0.02, 0.02)))
            self.latency = random.uniform(0.1, 2.0)
            self.active_pipelines = random.randint(1, 5)
            time.sleep(1)  # Update every second

monitor = PipelineMonitor()

# Start the monitoring simulation in a separate thread
def start_monitoring():
    monitor.update_metrics()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/metrics')
def get_metrics():
    metrics = {
        'data_processed': monitor.data_processed,
        'throughput': round(monitor.current_throughput, 2),
        'accuracy': round(monitor.model_accuracy * 100, 2),
        'latency': round(monitor.latency, 2),
        'pipelines': monitor.active_pipelines
    }
    return jsonify(metrics)

if __name__ == '__main__':
    # Start monitoring thread
    monitor_thread = Thread(target=start_monitoring)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)