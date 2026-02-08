import numpy as np
from .space import PhasePoint
from .gradient import phase_gradient

def find_null_zones(bodies, resolution=80, threshold=1e-2):
    zones = []

    for i in range(resolution):
        for j in range(resolution):
            θ = i / resolution
            φ = j / resolution
            p = PhasePoint(θ, φ)

            grad = phase_gradient(p, bodies)
            norm = np.linalg.norm(grad)

            if norm < threshold:
                zones.append((θ, φ, norm))

    return zones
  
