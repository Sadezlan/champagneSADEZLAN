from dataclasses import dataclass
from math import pi
from typing import Optional
from scipy.integrate import quad
from .radius_fun import f

@dataclass
class GlassProfile:
    """Geometric profile of a champagne glass.

    Attributes:
        x1, x2, x3, x4: Breakpoints along the horizontal axis t (cm).
        r_foot: Radius of the foot.
        r_stem: Radius of the stem.
        r_bowl: Radius of the bowl.
        r_rim: Radius at the rim.
    """

    x1: float
    x2: float
    x3: float
    x4: float
    r_foot: float
    r_stem: float
    r_bowl: float
    r_rim: float

    def radius_cone(self, t: float) -> float:
        """Return the radius at level t.

        Args:
            t: Position along the horizontal axis (cm).

        Returns:
            Radius r(t) at position t (cm).
        """
        return f(
            t,
            self.x1,
            self.x2,
            self.x3,
            self.x4,
            self.r_foot,
            self.r_stem,
            self.r_bowl,
            self.r_rim,
        )

    def volume_between(self, a: Optional[float] = None, b: Optional[float] = None) -> float:
        """Compute the champagne volume between levels t = a and t = b.

        Uses the disk method: V = pi ∫_a^b [r(t)]^2 dt.

        If a or b are not provided, they default to:
        - a = x2 (champagne does not go below t = x2)
        - b = x4 (rim of the glass)

        Args:
            a: Lower integration limit (cm).
            b: Upper integration limit (cm).

        Returns:
            Volume in cubic centimeters (cm^3).

        Raises:
            ValueError: If b < a.
        """
        if a is None:
            a = self.x2
        if b is None:
            b = self.x4

        if b < a:
            raise ValueError("Upper limit b must be >= lower limit a.")

        def integrand(t: float) -> float:
            r_t = self.radius_cone(t)
            return r_t * r_t

        integral_value, _ = quad(integrand, a, b)
        return pi * integral_value