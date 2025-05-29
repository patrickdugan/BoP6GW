"""Simple Pygame globe visualisation."""
import pygame, math
from . import core
WIDTH, HEIGHT = 1000, 600
BG = (25, 25, 35)

def run(game: core.Game, years: int = 50):
    pygame.init()
    scr = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("consolas", 14)
    clk = pygame.time.Clock()
    paused = False
    while game.year < 2030 + years:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                paused = not paused
        if not paused:
            game.step()
        scr.fill(BG)
        for i, (k, c) in enumerate(game.world.countries.items()):
            x = int(100 + i * (WIDTH - 200) / 4)
            y = int(HEIGHT / 2 + math.sin(i) * 150)
            r = int(10 + math.log1p(c.gdp))
            pygame.draw.circle(scr, (100, 200, 255), (x, y), r)
            lbl = font.render(f"{k} ${int(c.gdp)}", True, (200, 200, 200))
            scr.blit(lbl, (x - 30, y - r - 12))
        pygame.display.flip()
        clk.tick(30)
