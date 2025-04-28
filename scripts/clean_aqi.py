import pandas as pd

def clean_air_quality(file_path):
    """Loads air quality CSV and performs basic cleaning."""
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    print("This script will clean the air quality data.")
