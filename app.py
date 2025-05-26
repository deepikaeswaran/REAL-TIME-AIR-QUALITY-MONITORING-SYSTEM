from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    lat = data.get('lat', 10.0153)
    lon = data.get('lon', 77.4745)

    # Simulated prediction data
    no2 = round(random.uniform(20, 80), 2)
    temp = round(random.uniform(25, 40), 2)
    humidity = round(random.uniform(50, 90), 2)
    wind = round(random.uniform(1, 5), 2)

    alert = "✅ Safe" if no2 < 50 else "⚠️ Unhealthy"

    return jsonify({
        "lat": lat,
        "lon": lon,
        "no2": no2,
        "temperature": temp,
        "humidity": humidity,
        "wind_speed": wind,
        "alert": alert
    })

if __name__ == '__main__':
    app.run(debug=True)
