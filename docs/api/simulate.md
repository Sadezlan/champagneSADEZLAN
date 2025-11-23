Party Simulation (`simulate.py`)

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