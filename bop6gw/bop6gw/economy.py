"""Trade, sanctions, black‑market compute."""
import numpy as np
from . import actors

class Economy:
    def __init__(self, world: actors.World, rng):
        self.w = world
        self.rng = rng
        self.io = np.array([[0.1, 0.2], [0.05, 0.1]])  # chips⇆goods toy matrix

    def step(self, year: int):
        self.w.tick(self.rng)
        for c in self.w.countries.values():
            produced = 0.05 * c.gdp / 1000
            c.chips += produced
        if year == 2035:
            self._sanction('CN', 'US')

    def _sanction(self, src, dst):
        self.w.countries[src].chips *= 0.8
        self.w.countries[dst].chips *= 0.95
