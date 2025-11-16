import math # Import math module
from typing import Iterable, Sequence, List

def S(z: float) -> float:
    """Easing function S(z) = 0.5 - 0.5 * cos(pi * z).

    Arguments:
        z: Scalar value.

    Returns:
        Scalar float value of S(z).
    """
    return 0.5 - 0.5 * math.cos(math.pi * z)

def r(
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
    """Radius profile r(t) for a champagne glass.

    Piecewise definition with two smooth transitions using S(z).

    Args:
        t: Position along the horizontal axis (cm).
        x1, x2, x3, x4: Breakpoints along t (must satisfy 0 <= x1 < x2 < x3 < x4).
        r_foot: Radius of the foot section.
        r_stem: Radius of the stem section.
        r_bowl: Radius of the bowl section.
        r_rim: Radius at the rim.

    Returns:
        Radius r(t) at position t (cm).
    """
    # t < 0
    if t < 0:
        return 0.0

    # 0 <= t < x1
    if t < x1:
        return r_foot

    # x1 <= t < x2
    if t < x2:
        return r_stem

    # x2 <= t < x3 
    if t < x3:
        # normalized position between x2 and x3
        z = (t - x2) / (x3 - x2)
        s = S(z)
        return r_stem * (1.0 - s) + r_bowl * s

    # x3 <= t <= x4 
    if t <= x4:
        z = (t - x3) / (x4 - x3)
        s = S(z)
        s2 = s * s
        return r_bowl * (1.0 - s2) + r_rim * s2

    # t > x4
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
    """Vectorised wrapper around f() for integration routines.

    Args:
        t_values: Iterable of t positions.
        other parameters: forwarded to f().

    Returns:
        A list of radii for each t in t_values.
    """
    return [
        f(t, x1, x2, x3, x4, r_foot, r_stem, r_bowl, r_rim) for t in t_values
    ]