Geometry & radius (`radius_fun.py`)

S(z)
Smooth easing function

$S(z) = 0.5 - 0.5 \cos(\pi z)$

Used to make smooth transitions between different parts of the glass profile.

`f(t, x1, x2, x3, x4, r_foot, r_stem, r_bowl, r_rim)`
Scalar radius profile of the glass.
Given a position $t$ along the horizontal axis and the breakpoints $x1..x4$ with corresponding radius $(r_foot, r_stem, r_bowl, r_rim)$, this function returns the radius $r(t)$ in centimeters using a piecewise definition with easing.

`f_vec_for_integrate(t_values, ...)`
Vectorized wrapper around $f()$.
Takes a sequence of $t$ values and returns a list of radii.
This is mainly used by numerical integration routines that expect vector inputs.