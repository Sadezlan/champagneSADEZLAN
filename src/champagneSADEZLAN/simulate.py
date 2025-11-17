from math import ceil, sqrt
from typing import Optional, Dict, Any

import numpy as np
import pandas as pd

from .glass import GlassProfile
from .weather import CityWeather
from .expected_lambda import expected_lambda


def _sample_fill_height(glass: GlassProfile, rng: np.random.Generator) -> float:
    """Sample a fill height b for a single glass.

    a is fixed at glass.x2; b ~ N(14, 0.25) with constraint b > a and b <= x4.
    """
    a = glass.x2
    sd = sqrt(0.25)  # standard deviation = 0.5

    while True:
        b = rng.normal(loc=14.0, scale=sd)
        if b > a and b <= glass.x4:
            return b


def simulate_party(
    city_weather: CityWeather,
    glass: GlassProfile,
    rng: Optional[np.random.Generator] = None,
    bottle_L: float = 0.75,
) -> Dict[str, Any]:
    """Simulate a single champagne party.

    Assumptions:
        - Number of guests G ~ Poisson(lambda), lambda from expected_lambda(city_weather)
        - Each guest drinks D ~ Poisson(1.4) glasses (independent)
        - Fill level per glass: lower bound a = glass.x2,
          upper bound b ~ N(14, 0.25), truncated so that b > a and b <= x4.
        - Volume per glass computed with glass.volume_between(a, b).
        - One open bottle at most at the end ⇒ total bottles = ceil(total_L / bottle_L).

    Args:
        city_weather: CityWeather instance with T, H, P.
        glass: GlassProfile describing the glass geometry.
        rng: Optional NumPy random Generator (for reproducibility).
        bottle_L: Volume of a single bottle in liters (default 0.75 L).

    Returns:
        Dictionary with:
            - "guests": number of guests
            - "total_glasses": total number of glasses poured
            - "total_volume_cm3": total champagne volume in cm^3
            - "total_volume_L": total champagne volume in liters
            - "bottles": total number of bottles needed
    """
    if rng is None:
        rng = np.random.default_rng()

    # 1) Sample number of guests
    lam = expected_lambda(city_weather)
    guests = rng.poisson(lam)

    if guests == 0:
        return {
            "guests": 0,
            "total_glasses": 0,
            "total_volume_cm3": 0.0,
            "total_volume_L": 0.0,
            "bottles": 0,
        }

    # 2) Number of glasses per guest (independent Poisson(1.4))
    glasses_per_guest = rng.poisson(1.4, size=guests)
    total_glasses = int(glasses_per_guest.sum())

    # 3) Simulate volume per glass
    total_volume_cm3 = 0.0
    a = glass.x2  # lower level of champagne

    for _ in range(total_glasses):
        b = _sample_fill_height(glass, rng)
        vol = glass.volume_between(a=a, b=b)  # cm^3
        total_volume_cm3 += vol

    total_volume_L = total_volume_cm3 / 1000.0
    bottles = int(ceil(total_volume_L / bottle_L)) if total_volume_L > 0 else 0

    return {
        "guests": guests,
        "total_glasses": total_glasses,
        "total_volume_cm3": total_volume_cm3,
        "total_volume_L": total_volume_L,
        "bottles": bottles,
    }

def simulate_parties(
    city_weather: CityWeather,
    glass: GlassProfile,
    N: int = 1000,
    seed: Optional[int] = 123,
    bottle_L: float = 0.75,
) -> pd.DataFrame:
    """Simulate N champagne parties for a given city and glass.

    Args:
        city_weather: CityWeather instance.
        glass: GlassProfile describing the glass geometry.
        N: Number of simulated parties.
        seed: Random seed for reproducibility.
        bottle_L: Volume of one bottle in liters.

    Returns:
        A pandas DataFrame with one row per simulated party, containing:
        - guests
        - total_glasses
        - total_volume_cm3
        - total_volume_L
        - bottles
    """
    rng = np.random.default_rng(seed)
    records = []

    for _ in range(N):
        res = simulate_party(
            city_weather=city_weather,
            glass=glass,
            rng=rng,
            bottle_L=bottle_L,
        )
        records.append(res)

    return pd.DataFrame(records)