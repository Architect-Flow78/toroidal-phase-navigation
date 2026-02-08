import numpy as np
from .constants import PI, EPS

def phase_distance(a, b):
    d = abs(a - b)
    return min(d, PI - d)


def phase_tension(point, bodies):
    tension = 0.0
    for b in bodies:
        dθ = phase_distance(point.theta, b.theta)
        dφ = phase_distance(point.phi, b.phi)
        r2 = dθ**2 + dφ**2 + EPS
        tension += b.strength / r2
    return tension
  
