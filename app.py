from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from joblib import load

app = Flask(__name__)

# Load pre-trained models
model1 = load('model.pkl')  # Occupancy prediction model
model2 = load('model2.pkl')  # Resource usage prediction model

# User data (replace with actual user authentication mechanism)
user_data = {'user_id': '12345', 'course': 'Data Science'}  # Placeholder for authenticated user

@app.route('/')
def index():
    return render_template('index.html', user_data=user_data)

@app.route("/", methods=["GET", "POST"])
def optimize():
    if request.method == "POST":
        occupancy_data = float(request.form["occupancy"])  # Get user input
        recommendation = model.optimize_resources(occupancy_data)
        return render_template("index.html", recommendation=recommendation)
    else:
        return render_template("prediction.html")

@app.route('/monitor_resources')
def monitor_resources():
    # Simulate retrieving live resource data (replace with actual data retrieval logic)
    data = {'time_stamp': ['2024-05-03 14:30:00'], 'lab_ID': ['LAB1'], 'CPU_usage': [72],
            'memory_usage': [85], 'disk_usage': [68]}  # Sample data
    df = pd.DataFrame(data)

    return render_template('monitor.html', resource_data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production

