from phase.nullzones import find_null_zones
from phase.trajectory import propagate

class PhaseSimulator:
    def __init__(self, bodies):
        self.bodies = bodies

    def analyze(self, start_point):
        nulls = find_null_zones(self.bodies)
        traj = propagate(start_point, self.bodies)
        return nulls, traj
      
