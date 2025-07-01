
# --- collectible --- #

import pygame
import random
from settings import WIDTH, HEIGHT, COLLECTIBLE_RADIUS, TOP_MARGIN, COLLECTIBLE_COLOR


# add collectible dots to the screen
def generate_collectibles():
    num = random.randint(10, 100)
    collectibles = []
    for _ in range(num):
        x = random.randint(COLLECTIBLE_RADIUS, WIDTH - COLLECTIBLE_RADIUS)
        y = random.randint(TOP_MARGIN + COLLECTIBLE_RADIUS, HEIGHT - COLLECTIBLE_RADIUS)
        rect = pygame.Rect(x, y, COLLECTIBLE_RADIUS * 2, COLLECTIBLE_RADIUS * 2)
        collectibles.append(rect)
    return collectibles


# draw the collectibles
def draw_collectibles(screen, collectibles):
    for c in collectibles:
        pygame.draw.circle(screen, COLLECTIBLE_COLOR, c.center, COLLECTIBLE_RADIUS)


# check for collision and increase score
def check_collisions(player_rect, collectibles):
    score = 0
    for c in collectibles[:]:
        if player_rect.colliderect(c):
            collectibles.remove(c)
            score += 1
    return score