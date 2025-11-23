# champagneSADEZLAN – Champagne Party Simulation Package

This package contains all reusable functions and classes used to model a champagne glass, weather conditions, and to simulate champagne consumption at an event.

Below is a short description of the main components, in the order they are introduced in the exercises.

---

## 1. Geometry & Radius Profile (`radius_fun.py`)

- **`S(z)`**  
  Easing function  
  
  $S(z) = 0.5 - 0.5 \cos(\pi z)$
   
  used to obtain smooth transitions in the glass radius.

- **`f(t, x1, x2, x3, x4, r_foot, r_stem, r_bowl, r_rim)`**  
  Scalar radius profile $r(t)$ of the glass, defined piecewise along the horizontal axis $t$.  
  Returns the radius (in cm) at a single position $t$, given the breakpoints and section radius.

- **`f_vec_for_integrate(t_values, ...)`**  
  Vectorized wrapper around `f()` that evaluates the radius for a sequence of `t` values.  
  Intended for use with numerical integration routines.

---

## 2. Glass Profile & Volume (`glass.py`)

- **`GlassProfile`**  
  Class representing the geometric profile of a champagne glass.

  **Main methods:**
  - `radius_cone(t)` → returns the radius at height `t`.
  - `volume_between(a, b)` → computes the volume of champagne between levels `t = a` and `t = b` using the disk method  
    
    $V = \pi \int_a^b [r(t)]^2 dt$
    
    Volume is returned in cm³.

---

## 3. Weather Data Processing (`data_raw/data_transformation.py`)

- **`load_raw_weather(path)`**  
  Loads the raw `weather_full.json` file (OpenWeather API data).

- **`extract_weather_table(raw)`**  
  Extracts key fields (city, temperature, humidity, pressure) from the nested JSON and returns a flat `pandas.DataFrame`.

- **`process_and_save_weather(raw_path, out_path)`**  
  Full pipeline: loads JSON, extracts relevant fields, cleans simple structures (e.g. `[22.5]` → `22.5`), and saves  
  `weather_processed.csv` to the package’s `data/processed_data/` folder.

---

## 4. City Weather Model (`weather.py`)

- **`CityWeather`**  
  Small data class holding weather information for a single city:
  - `city`
  - `temperature` (°C)
  - `humidity` (%)
  - `pressure` (hPa)

  Implements `__str__` so that `print(city_weather)` shows a readable summary, or an informative message if no data is available.

---

## 5. Attendance Model (`expected_lambda.py`)

- **`expected_lambda(city_weather)`**  
  Computes the expected number of guests  
  
  $\lambda = \exp(0.5 + 0.5T - 3H + 0.001P)$
   
  where:
  - `T` = temperature (°C),
  - `H` = humidity **in fraction** (converted from %),
  - `P` = pressure (hPa).

  Raises a `ValueError` if weather data is missing.

---

## 6. Party Simulation (`simulate.py`)

- **`simulate_party(city_weather, glass, rng=None, bottle_L=0.75)`**  
  Simulates a single party with:
  - Number of guests $( G \sim \text{Poisson}(\lambda) )$, with $( \lambda )$ from `expected_lambda()`.
  - Each guest drinks $( D \sim \text{Poisson}(1.4) )$ glasses.
  - Each glass is filled between `a = x2` and `b ~ N(14, 0.25)` (truncated so that `b > a` and `b <= x4`).
  - Volume per glass is computed with `GlassProfile.volume_between(a, b)`.

  Returns a dictionary with:
  - `guests`, `total_glasses`,
  - `total_volume_cm3`, `total_volume_L`,
  - `bottles` (number of 0.75 L bottles needed).

- **`simulate_parties(city_weather, glass, N=1000, seed=123, bottle_L=0.75)`**  
  Runs the above process `N` times and returns a `pandas.DataFrame` with one row per simulated party.

---

## Public API

The main objects and functions are exposed at package level in `__init__.py`, so they can be imported as:

```python
from champagneSADEZLAN import (
    GlassProfile,
    CityWeather,
    expected_lambda,
    simulate_parties,
)

