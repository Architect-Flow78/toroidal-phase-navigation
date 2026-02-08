import numpy as np
from .space import PhasePoint
from .tension import phase_tension
from .constants import EPS

def phase_gradient(point, bodies):
    base = phase_tension(point, bodies)

    pθ = PhasePoint(point.theta + EPS, point.phi, point.s)
    pφ = PhasePoint(point.theta, point.phi + EPS, point.s)

    gθ = (phase_tension(pθ, bodies) - base) / EPS
    gφ = (phase_tension(pφ, bodies) - base) / EPS

    return np.array([gθ, gφ])
  
