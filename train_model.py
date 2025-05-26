#train_model.py                                                   
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from preprocessing import preprocess_data
from data_fusion import fuse_data

# Sample fused data (should be list of dicts or a DataFrame)
sample_data = [
    {
        "temperature": 30.2,
        "humidity": 70,
        "wind_speed": 1.2,
        "sensor_no2": 42,
        "api_no2": 40,
        "fused_no2": 41,
        "location": "Theni"
    },
    {
        "temperature": 29.5,
        "humidity": 65,
        "wind_speed": 1.0,
        "sensor_no2": 38,
        "api_no2": 39,
        "fused_no2": 38.5,
        "location": "Theni"
    }
]

# Fix: Pass directly to preprocessing
X, y = preprocess_data(sample_data)

# Split for evaluation (optional)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.joblib')
print("✅ Model trained and saved successfully!")