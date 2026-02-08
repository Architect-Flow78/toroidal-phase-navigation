from .space import PhasePoint, wrap
from .gradient import phase_gradient

def propagate(start, bodies, dt=0.01, steps=1000):
    path = []
    p = start

    for _ in range(steps):
        g = phase_gradient(p, bodies)

        p = PhasePoint(
            wrap(p.theta - g[0] * dt),
            wrap(p.phi - g[1] * dt),
            p.s + dt
        )

        path.append(p)

    return path
  
