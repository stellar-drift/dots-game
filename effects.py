
# --- effects -- #

import pygame
import random
from settings import COLLECTIBLE_COLOR, WIDTH, HEIGHT

class Fireworks:
    def __init__(self, x, y, color, lifespan = 60):
        self.x = x
        self.y = y
        self.color = color
        self.lifespan = lifespan
        self.particles = []
        self._create_particles()


    def _create_particles(self):
        for _ in range(20):
            angle = random.uniform(0, 2 * 3.14159)
            speed = random.uniform(1, 4)
            dx = speed * random.uniform(-1, 1)
            dy = speed * random.uniform(-1, 1)
            self.particles.append({
                'pos': [self.x, self.y],
                'vel': [dx, dy],
                'timer': self.lifespan
            })

    def update(self):
        for p in self.particles:
            p['pos'][0] += p['vel'][0]
            p['pos'][1] += p['vel'][1]
            p['timer'] -= 1

        self.particles = [p for p in self.particles if p['timer'] > 0]


    def draw(self, screen):
        for p in self.particles:
            alpha = max(0, int(255 * (p['timer'] / self.lifespan)))
            surface = pygame.Surface((4,4), pygame.SRCALPHA)
            surface.fill((*self.color, alpha))
            screen.blit(surface, p['pos'])

    def is_alive(self):
        return len(self.particles) > 0




## HELPER FXN ##

def create_fireworks(num=20):
    fireworks = []
    for _ in range(num):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        color = COLLECTIBLE_COLOR
        fireworks.append(Fireworks(x, y, color))
    return fireworks