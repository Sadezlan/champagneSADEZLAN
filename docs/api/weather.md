City Weather Model (`weather.py`)

- **`CityWeather`**  
  Small data class holding weather information for a single city:
  - `city`
  - `temperature` (°C)
  - `humidity` (%)
  - `pressure` (hPa)

  Implements `__str__` so that `print(city_weather)` shows a readable summary, or an informative message if no data is available.