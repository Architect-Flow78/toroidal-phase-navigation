from .constants import PI

def wrap(x):
    return x % PI


class PhasePoint:
    def __init__(self, theta, phi, s=0.0):
        self.theta = wrap(theta)
        self.phi = wrap(phi)
        self.s = s

    def as_tuple(self):
        return (self.theta, self.phi, self.s)

