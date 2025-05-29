"""Core engine: clock, event bus, main loop."""
from __future__ import annotations
import random, collections
from . import actors, economy, warfare, crises

Event = collections.namedtuple("Event", "year type payload")

class Game:
    """Glue of all subsystems."""
    def __init__(self, seed:int|None=None):
        self.rng = random.Random(seed)
        self.year = 2030
        self.world = actors.World(self.rng)
        self.econ  = economy.Economy(self.world, self.rng)
        self.war   = warfare.WarManager(self.world, self.rng)
        self.crisis= crises.CrisisManager(self.world, self.rng)
        self.events: list[Event] = []

    def step(self):
        self.econ.step(self.year)
        self.war.step(self.year)
        self.crisis.step(self.year)
        self.year += 1

    def simulate(self, years:int=30, n:int=1):
        """Headless Monte‑Carlo — returns list of world snapshots."""
        out=[]
        for _ in range(n):
            self.__init__(seed=self.rng.randint(0,1<<32))
            for _y in range(years):
                self.step()
            out.append(self.world.snapshot())
        return out

    def gui(self):
        from . import gui
        gui.run(self)
