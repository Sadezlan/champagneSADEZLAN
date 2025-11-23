# Welcome to champagneSADEZLAN's MkDocs documentation!

## Repository layout

The `champagneSADEZLAN` project is organised as a standard `src/`-based Python package:

```text
champagneSADEZLAN/
├── pyproject.toml                    # Project metadata and dependencies
├── README.md                         # Package overview
├── docs/                             # MkDocs documentation sources
│   ├── index.md                      # Main documentation page
│   ├── tutorial.md                   # Usage example / vignette (optional)
│   └── api/                          # API reference pages (mkdocstrings)
├── data_raw/
│   ├── weather_full.json             # Raw OpenWeather data
│   └── data_transformation.py        # Raw → processed data pipeline
├── src/
│   └── champagneSADEZLAN/
│       ├── __init__.py               # Public API exports
│       ├── glass.py                  # GlassProfile class and volume methods
│       ├── radius_fun.py             # S(), f(), f_vec_for_integrate()
│       ├── weather.py                # CityWeather class
│       ├── expected_lambda.py        # expected_lambda() attendance model
│       ├── simulate.py               # simulate_party(), simulate_parties()
│       └── data/
│           └── processed_data/
│               └── weather_processed.csv    
│    
│    
├──    mkdocs.yml    # The configuration file.
└──    .gitignore    # Ignore file for Git.
```

## Configuration

# Glass

::: champagneSADEZLAN.glass

# Radius function

::: champagneSADEZLAN.radius_fun

# Weather

::: champagneSADEZLAN.weather

# Expected lambda

::: champagneSADEZLAN.expected_lambda

# Simulation

::: champagneSADEZLAN.simulate