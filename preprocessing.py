import pandas as pd

def preprocess_data(data):
    # If data is a list of dicts, convert to DataFrame
    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, pd.DataFrame):
        df = data
    else:
        raise ValueError("Input data must be a DataFrame or list of dictionaries")

    df = df.dropna()
    
    # Encode categorical variables
    if 'location' in df.columns:
        df['location'] = df['location'].astype('category').cat.codes

    # Define features and target
    features = ['temperature', 'humidity', 'wind_speed', 'sensor_no2', 'api_no2', 'location']
    target = 'fused_no2'

    X = df[features]
    y = df[target]
    return X, y
