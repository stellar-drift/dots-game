
# --- enemy --- #


import pygame
import random
from settings import WIDTH, HEIGHT, TOP_MARGIN, ENEMY_COLOR, ENEMY_CHASE_COLOR


class Enemy:
    def __init__(self, radius=10, speed=2, chase_range=200):
        self.radius = radius
        self.speed = speed
        self.chase_range = chase_range
        self.x, self.y = self._random_edge_position()
        self.wander_target = self._random_target()
        self.wander_cooldown = 0
        self.is_chasing = False
        self.color = ENEMY_COLOR


    def _random_edge_position(self):
        edges = ["top", "bottom", "left", "right"]
        edge = random.choice(edges)

        if edge == "top":
            x = random.randint(self.radius, WIDTH - self.radius)
            y = TOP_MARGIN + self.radius    # just below the score bar
        elif edge == "bottom":
            x = random.randint(self.radius, WIDTH - self.radius)
            y = HEIGHT - self.radius
        elif edge == "left":
            x = self.radius
            y = random.randint(TOP_MARGIN + self.radius, HEIGHT - self.radius)
        else:   # "right" edge
            x = WIDTH - self.radius
            y = random.randint(TOP_MARGIN + self.radius, HEIGHT - self.radius)

        return x, y



    def wander(self):
        # recalculate target if cooldown expired or reached target
        if self.wander_cooldown <= 0 or self._at_target(self.wander_target):
            self.wander_target = self._random_target()
            self.wander_cooldown = random.randint(60, 180)      # 1 to 3 seconds at 60fps

        # move toward target
        dx = self.wander_target[0] - self.x
        dy = self.wander_target[1] - self.y
        distance = (dx**2 + dy**2)**0.5
        if distance > 0:
            self.x += self.speed * dx / distance
            self.y += self.speed * dy / distance

        self.wander_cooldown -= 1
        self._stay_on_screen()

    def chase_player(self, player, chase_sound=None):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = (dx**2 + dy**2)**0.5

        if distance < self.chase_range:
            if not self.is_chasing:
                if chase_sound:
                    chase_sound.play()
            self.is_chasing = True
            chase_speed = self.speed * 2  # speed boost for chase
            if distance != 0:
                self.x += chase_speed * dx / distance
                self.y += chase_speed * dy / distance
            self._stay_on_screen()
        else:
            self.is_chasing = False
            self.wander()


    def _random_target(self):   # helper fxn
        margin = 20
        return (
            random.randint(self.radius, WIDTH - self.radius - margin),
            random.randint(TOP_MARGIN + self.radius, HEIGHT - self.radius - margin)
        )

    def _at_target(self, target, threshold=5):      # helper fxn
        return abs(self.x - target[0]) < threshold and abs(self.y - target[1]) < threshold


    def draw(self, screen):
        self.color = ENEMY_CHASE_COLOR if self.is_chasing else ENEMY_COLOR
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)


    def _stay_on_screen(self):
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(TOP_MARGIN + self.radius, min(HEIGHT - self.radius, self.y))
