"""Balance‑of‑Power crisis ladder & brinkmanship."""
import random
from . import actors

class CrisisManager:
    def __init__(self, world: actors.World, rng):
        self.w = world
        self.rng = rng
        self.tension = 0.2

    def step(self, year: int):
        if any(c.doctrine == "frontier" for c in self.w.countries.values()):
            self.tension += 0.01
        if self.tension > 0.8 and self.rng.random() < 0.02:
            offender = self.rng.choice(list(self.w.countries))
            self.w.countries[offender].stability *= 0.5
