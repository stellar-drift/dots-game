
# --- sound manager --- #

import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS         # used when bundled by pyinstaller, ok to ignore
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'collect': pygame.mixer.Sound(resource_path("sounds/collect.mp3")),
            'enemy_alert': pygame.mixer.Sound(resource_path("sounds/enemy_alert.mp3")),
            'game_over': pygame.mixer.Sound(resource_path("sounds/game_over.mp3")),
            'game_win': pygame.mixer.Sound(resource_path("sounds/game_win.mp3")),
            'background_music': pygame.mixer.Sound(resource_path("sounds/spiritual_evolution_dance.mp3"))
        }

    def play(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def set_volume(self, sound_name, volume):
        if sound_name in self.sounds:
            self.sounds[sound_name].set_volume(volume)