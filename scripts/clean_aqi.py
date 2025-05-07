# scripts/clean_aqi.py

import pandas as pd

def clean_air_quality(input_path, output_path):
    print("Reading data from:", input_path)
    df = pd.read_csv(input_path)
    print("Initial rows:", len(df))

    df = df[['Date Local', 'NO2 Mean', 'O3 Mean', 'SO2 Mean', 'CO Mean']].dropna()
    print("After dropna rows:", len(df))

    df = df.groupby('Date Local').mean().reset_index()
    df.columns = ['date', 'no2', 'o3', 'so2', 'co']
    df['date'] = pd.to_datetime(df['date']).dt.date

    df.to_csv(output_path, index=False)
    print("Saved cleaned data to:", output_path)

if __name__ == "__main__":
    print("This script will clean the air quality data.")
    clean_air_quality("data/pollution_us_2000_2016.csv", "data/air_quality_clean.csv")
