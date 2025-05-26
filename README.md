# 🌍 Real-Time Air Quality Monitoring System using IoT and Machine Learning

This project predicts **Nitrogen Dioxide (NO₂)** levels in real-time using simulated IoT sensor data and live weather parameters from the **OpenWeather API**. It integrates **data fusion, preprocessing, and ML-based predictions (XGBoost & LSTM)** to alert users about air quality status via an interactive **web dashboard** with **maps and charts**.


## 🚀 Features

- 🔄 Real-time NO₂ prediction using live and simulated sensor data  
- 🌤️ Weather data integration via OpenWeather API  
- 🔀 Data fusion and preprocessing with feature scaling  
- 🤖 ML-based prediction using XGBoost (tabular) and LSTM (time series)  
- 🗺️ Interactive map visualization using Leaflet.js  
- 📈 Dynamic multi-parameter charting using Chart.js  
- ⚠️ Smart alerts based on NO₂ levels (Safe / Unsafe)  
- 🖥️ Web dashboard interface built with Flask + HTML + JS  


## ⚙️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/deepikaeswaran/REAL-TIME-AIR-QUALITY-MONITORING-SYSTEM
   cd REAL-TIME-AIR-QUALITY-MONITORING-SYSTEM

2.**Install requirements**
```bash
   pip install -r requirements.txt
```
3.**Train the model**
```bash
   python train_model.py
```
4.**Start the server**
```bash
   python app.py
```
5.**Access in browser**
```bash
   http://127.0.0.1:5000
```

## 📊 Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Visualization: Leaflet.js, Chart.js
- ML Models: XGBoost, LSTM
- API: OpenWeather API

## 🧪 Output
![image](https://github.com/user-attachments/assets/cb5cebd4-3745-46bc-9430-2d7c70af3cc7)
![image](https://github.com/user-attachments/assets/10201aed-bcc5-4111-97fe-3f6a2cdbdc3d)

## 📜 License
This project is open-source and free to use under the MIT License.

