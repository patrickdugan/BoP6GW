"""6GW combat: swarms, EW, narrative strikes."""
import random
from . import actors

class WarManager:
    def __init__(self, world: actors.World, rng):
        self.w = world
        self.rng = rng
        self.active_conflicts: list[tuple[str, str]] = []

    def step(self, year: int):
        for name, c in self.w.countries.items():
            if c.stability < 0.5 and self.rng.random() < 0.1:
                target = self.rng.choice(list(self.w.countries))
                if (name, target) not in self.active_conflicts:
                    self.active_conflicts.append((name, target))
