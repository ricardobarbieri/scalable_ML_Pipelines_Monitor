# ML Pipeline Monitor - Code Overview

A simple Flask-based web application designed to simulate and monitor machine learning (ML) pipeline metrics in real-time.

---

## Brief Description

This code creates a lightweight web application using Flask to simulate and monitor key metrics of a machine learning pipeline. It provides a user-friendly dashboard displaying real-time data such as:

- **Data Processed**
- **Throughput**
- **Model Accuracy**
- **Latency**
- **Active Pipelines**

The metrics update every second and are visualized through interactive charts powered by Chart.js.

---

## Detailed Description

This project implements a Flask-based web application tailored to simulate and track the performance metrics of an ML pipeline. Below is a detailed breakdown of its components and functionality:

### 1. Flask Application Setup
- **Framework**: Built with [Flask](https://flask.palletsprojects.com/), a lightweight Python web framework.
- **Routes**:
  - `/`: Serves the main dashboard page (`index.html`).
  - `/api/metrics`: API endpoint returning current metrics in JSON format.
- **Simulation Class**: Features a `PipelineMonitor` class to generate real-time metric simulations.

### 2. Monitoring Simulation
- **Metrics Tracked**:
  - **Data Processed**: Total records processed, incremented randomly by 100–1000 per second.
  - **Throughput**: Processing rate, a random float between 50–200 records/second.
  - **Model Accuracy**: Ranges from 75% to 99%, adjusted by ±0.02 each second.
  - **Latency**: Processing delay, randomly set between 0.1–2.0 seconds.
  - **Active Pipelines**: Number of active pipelines, randomly set between 1–5.
- **Update Mechanism**: The `update_metrics` method runs in a loop, refreshing metrics every second with random values to simulate real-world variability.

### 3. Web Interface
- **Dashboard Layout**:
  - The `index.html` page displays metrics in a grid of styled cards.
  - CSS provides a modern design with shadows, responsive layouts, and hover effects.
- **Visualization**:
  - A dynamic line chart (via [Chart.js](https://www.chartjs.org/)) tracks throughput, accuracy, and latency over the last 20 seconds.
  - Updates occur in real-time as new data is fetched.

### 4. API Endpoint
- **Endpoint**: `/api/metrics` delivers a JSON object with the latest metric values:
  ```json
  {
    "data_processed": 12345,
    "throughput": 150.23,
    "accuracy": 87.50,
    "latency": 0.45,
    "pipelines": 3
  }
Usage: The frontend consumes this data to refresh the dashboard and chart.

### 5. Threading
Background Process: The update_metrics method runs in a separate thread, ensuring continuous updates without blocking Flask.
Implementation: A daemon Thread starts with the app and stops when the program ends.

### 6. HTML and JavaScript

**Structure:**
HTML includes a title, dashboard grid, and chart canvas within a responsive container.
CSS ensures adaptability, stacking cards vertically on screens <600px wide.
Dynamic Updates:
JavaScript uses the fetch API to retrieve /api/metrics data every second.
Updates card values and maintains a 20-point chart window, showing time relative to now (e.g., -19 to 0 seconds ago).
Chart.js displays three datasets (throughput, accuracy, latency) in distinct colors.

**Execution**
Startup: The Flask app launches a monitoring thread and runs the server on 0.0.0.0:5000 in debug mode, accessible locally or on a network.
Interactivity: Open a browser to view the dashboard, where metrics update live, simulating an ML pipeline’s performance.

**Purpose**
This code offers a foundational example for monitoring ML pipeline metrics in a simulated environment. It can be extended to connect with real ML systems by replacing the random simulation with actual pipeline data.
