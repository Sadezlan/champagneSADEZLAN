Glass Profile & Volume (`glass.py`)

- **`GlassProfile`**  
  Class representing the geometric profile of a champagne glass.

  **Main methods:**
  - `radius_cone(t)` → returns the radius at height `t`.
  - `volume_between(a, b)` → computes the volume of champagne between levels `t = a` and `t = b` using the disk method  
    
    $V = \pi \int_a^b [r(t)]^2 dt$
    
    The result is in cubic centimeters (cm³). By default the lower limit is $x2$ (fill level) and the upper limit is $x4$ (rim).