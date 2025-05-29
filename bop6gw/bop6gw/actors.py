"""Countries, blocs, non‑state factions."""
from __future__ import annotations
from dataclasses import dataclass
import random

@dataclass
class Country:
    name: str
    gdp: float
    chips: float
    doctrine: str
    alliance: str|None = None
    stability: float = 0.8
    morale: float = 0.7

    def tick(self, rng: random.Random):
        growth = 0.03 if self.doctrine == "frontier" else 0.015
        self.gdp *= 1 + growth
        self.stability = max(0, min(1, self.stability + rng.uniform(-0.02, 0.02)))

class World:
    """Holds all actors."""
    def __init__(self, rng: random.Random):
        self.rng = rng
        self.countries: dict[str, Country] = {
            'US': Country('US', 25000, 400, 'frontier', 'NATO'),
            'CN': Country('CN', 18000, 350, 'frontier', 'SCO'),
            'EU': Country('EU', 17000, 200, 'regulate', 'NATO'),
            'RU': Country('RU', 2100, 120, 'frontier', 'SCO'),
            'IN': Country('IN', 3200, 90, 'laissez', None),
        }

    def tick(self, rng):
        for c in self.countries.values():
            c.tick(rng)

    def snapshot(self):
        return {k: c.__dict__.copy() for k, c in self.countries.items()}
