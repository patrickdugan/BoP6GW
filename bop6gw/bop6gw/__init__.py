"""Balance‑of‑Power 6th‑Generation Warfare Sandbox (BoP‑6GW).

High‑level entrypoints:
    from bop6gw import Game
    Game().gui()           # run interactive GUI
    Game().simulate(n=100) # headless Monte‑Carlo
"""
from importlib import import_module

_modules = ["core", "actors", "economy", "warfare", "crises", "gui"]
for _m in _modules:
    globals()[_m] = import_module(f"bop6gw.{_m}")

def Game():
    """Convenience façade."""
    return core.Game()
