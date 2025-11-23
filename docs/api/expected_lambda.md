Attendance Model (`expected_lambda.py`)

- **`expected_lambda(city_weather)`**  
  Computes the expected number of guests  
  
  $\lambda = \exp(0.5 + 0.5T - 3H + 0.001P)$
   
  where:
  - `T` = temperature (°C),
  - `H` = humidity **in fraction** (converted from %),
  - `P` = pressure (hPa).

  Raises a `ValueError` if weather data is missing.