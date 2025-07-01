
# --- player --- #

import pygame
from settings import WIDTH, HEIGHT, DOT_RADIUS, PLAYER_SPEED, TOP_MARGIN, PLAYER_COLOR


class Player:

    # initialize self, set class variables
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = DOT_RADIUS
        self.color = PLAYER_COLOR
        self.speed = PLAYER_SPEED

    # get key states / move player
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed


        # keep player on screen
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius + TOP_MARGIN, min(HEIGHT - self.radius, self.y))


    # create player rect for collision
    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)


    # draw the player dot
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)