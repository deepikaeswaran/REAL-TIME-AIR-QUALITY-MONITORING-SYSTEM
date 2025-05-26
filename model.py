#model.py                                                                                                                     from sklearn.linear_model import LinearRegression
from statistics import LinearRegression
from preprocessing import preprocess_data

def predict_no2():
    X, y, scaler = preprocess_data()
    if X is None or y is None:
        return None, "Error in preprocessing."

    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([X[-1]])[0]

    if prediction > 80:
        alert = "⚠ High pollution level!"
    elif prediction > 50:
        alert = "Moderate pollution."
    else:
        alert = "✅ Air quality is good."

    return round(prediction, 2), alert