import math # Import math module
from typing import Iterable, Sequence, List

def S(z: float) -> float:
    """Easing function S(z) = 0.5 - 0.5 * cos(pi * z)."""
    return 0.5 - 0.5 * math.cos(math.pi * z)


def f(
    t: float,
    x1: float,
    x2: float,
    x3: float,
    x4: float,
    r_foot: float,
    r_stem: float,
    r_bowl: float,
    r_rim: float,
) -> float:
    """Scalar radius profile r(t) for a champagne glass."""
    if t < 0:
        return 0.0

    if t < x1:
        return r_foot

    if t < x2:
        return r_stem

    if t < x3:
        z = (t - x2) / (x3 - x2)
        s = S(z)
        return r_stem * (1.0 - s) + r_bowl * s

    if t <= x4:
        z = (t - x3) / (x4 - x3)
        s = S(z)
        s2 = s * s
        return r_bowl * (1.0 - s2) + r_rim * s2

    return 0.0


def f_vec_for_integrate(
    t_values: Sequence[float],
    x1: float,
    x2: float,
    x3: float,
    x4: float,
    r_foot: float,
    r_stem: float,
    r_bowl: float,
    r_rim: float,
) -> List[float]:
    """Vectorized wrapper for f(), for numerical integration."""
    return [f(t, x1, x2, x3, x4, r_foot, r_stem, r_bowl, r_rim) for t in t_values]