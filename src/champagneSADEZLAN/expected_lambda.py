from math import exp
from .weather import CityWeather


def expected_lambda(city_weather: CityWeather) -> float:
    """Compute expected number of guests from weather conditions.

    Uses the link function:
        lambda = exp(0.5 + 0.5*T - 3*H + 0.001*P)

    where:
        T = temperature
        H = humidity
        P = pressure

    Args:
        city_weather: CityWeather instance with temperature, humidity, pressure.

    Returns:
        Expected guest count lambda (float).

    Raises:
        ValueError: If any of T, H or P is missing.
    """
    T = city_weather.temperature
    H = city_weather.humidity / 100.0  # convert percentage to fraction
    P = city_weather.pressure

    if T is None or H is None or P is None:
        raise ValueError(
            f"Cannot compute expected_lambda: missing weather data for {city_weather.city!r}."
        )

    return float(exp(0.5 + 0.5 * T - 3.0 * H + 0.001 * P))