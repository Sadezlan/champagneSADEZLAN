import json
from pathlib import Path
import pandas as pd


# Define file paths
RAW_WEATHER_PATH = Path("data_raw/weather_full.json")
PROCESSED_WEATHER_PATH = Path("src/champagneSADEZLAN/data/processed_data/weather_processed.csv")

# Function to load raw weather data
def load_raw_weather(path: Path = RAW_WEATHER_PATH) -> dict:
    """Load the nested JSON with weather data."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

# Function to extract relevant fields into a flat table
def extract_weather_table(raw: dict) -> pd.DataFrame:
    """Extract city, temperature, humidity, pressure into a flat table."""
    rows = []
    for city_name, data in raw.items():
        main = (data or {}).get("main", {})
        rows.append(
            {
                "city": city_name,
                "temperature": main.get("temp"),
                "humidity": main.get("humidity"),
                "pressure": main.get("pressure"),
            }
        )
    return pd.DataFrame(rows)

# Main processing function
def process_and_save_weather(
    raw_path: Path = RAW_WEATHER_PATH,
    out_path: Path = PROCESSED_WEATHER_PATH,
) -> None:
    """Load raw JSON, extract key fields, and save as CSV."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    raw = load_raw_weather(raw_path)
    df = extract_weather_table(raw)
    df.to_csv(out_path, index=False)


if __name__ == "__main__":
    process_and_save_weather()