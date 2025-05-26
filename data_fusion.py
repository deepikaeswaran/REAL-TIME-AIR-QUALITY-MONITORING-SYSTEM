#data_fusion.py                      
import pandas as pd
from datetime import datetime
from data_collection import get_combined_data

API_KEY = "9a73bc025fcdaf6dbdcb5331de311af0"  # Replace with your key

def fuse_data(lat=10.0153, lon=77.4745, overwrite=False):
    data = get_combined_data(API_KEY, lat, lon)
    data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df = pd.DataFrame([data])

    if not overwrite:
        try:
            existing = pd.read_csv('fused_data.csv')
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            print("ℹ No existing data found. Creating new.")
        except Exception as e:
            print(f"⚠ Error reading CSV: {e}")

    df.to_csv('fused_data.csv', index=False)
    print("✅ Data saved to fused_data.csv")
    return df