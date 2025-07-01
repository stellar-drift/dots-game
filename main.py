
# --- main --- #

# import libraries
import pygame
import sys

# import scripts
from settings import *
from player import Player
from collectible import generate_collectibles, draw_collectibles
from enemy import Enemy
from overlay import draw_game_over, draw_victory
from effects import create_fireworks
from sound_manager import SoundManager, resource_path


def reset_game_state():
    player = Player()  # instantiate player object
    enemy = Enemy()  # instantiate enemy object
    collectibles = generate_collectibles()  # call method
    score = 0  # initialize the score
    game_over = False
    play_again_rect = None
    quit_rect = None
    return player, enemy, collectibles, score, game_over, play_again_rect, quit_rect


def run_game():

    pygame.init()       # start game

    # sounds and music
    pygame.mixer.init()     # initialize the sound mixer
    sound_manager = SoundManager()      # instantiate sound manager object for effects

    pygame.mixer.music.load(resource_path("sounds/spiritual_evolution_dance.mp3")) # background music :)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)     # -1 means infinite loop


    # display setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))       # set the screen
    pygame.display.set_caption("DOTS!!!")       # title the game in the window
    clock = pygame.time.Clock()     # set up clock for consistent frame rate

    # score setup
    score_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE_LG, bold=True)     # set score font
    score_popup_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE_POPUP, bold = True)     # set score popup font

    # initialize game state
    player, enemy, collectibles, score, game_over, play_again_rect, quit_rect = reset_game_state()
    player_wins = False
    score_popups = []  # initialize a way to hold score popups
    fireworks = create_fireworks()    # create a list of fireworks


    running = True
    while running:
        clock.tick(FPS)


        ### EVENT HANDLING ###

        # event checking for QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # event checking for clicks when game is over or player wins
            if event.type == pygame.MOUSEBUTTONDOWN and (game_over or player_wins):
                if play_again_rect and play_again_rect.collidepoint(event.pos):
                    # reset game state
                    player, enemy, collectibles, score, game_over, play_again_rect, quit_rect = reset_game_state()
                    player_wins = False
                    score_popups.clear()
                    fireworks = create_fireworks()

                elif quit_rect and quit_rect.collidepoint(event.pos):
                    running = False


        ### GAME LOGIC ###

        # check win condition before enemy collision
        if not game_over and not player_wins and len(collectibles) == 0:
            player_wins = True
            sound_manager.play('game_win')

        # regular gameplay logic
        if not game_over and not player_wins:
            player.handle_input()
            enemy.chase_player(player, sound_manager.sounds['enemy_alert'])

            if enemy.get_rect().colliderect(player.get_rect()):
                game_over = True
                sound_manager.play('game_over')


        # collect collectibles on collision
        for c in collectibles[:]:
            if player.get_rect().colliderect(c):
                collectibles.remove(c)
                score += 1
                # add popup: position at collectible center, timer 60 frames (1 second at 60fps)
                score_popups.append({'pos': list(c.center), 'timer': 60})
                sound_manager.play('collect')


        ### DRAW THINGS ###

        # draw background & UI
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, SCORE_BAR_COLOR, (0, 0, WIDTH, TOP_MARGIN))

        # draw game objects
        draw_collectibles(screen, collectibles)
        enemy.draw(screen)
        player.draw(screen)

        # draw score popups
        for popup in score_popups[:]:
            popup['pos'][1] -= 1    # float popup upward
            popup['timer'] -= 1     # fade timer
            alpha = max(0, int(255 * (popup['timer'] / 60)))        # render text with alpha based on timer
            popup_surface = score_popup_font.render("+1", True, SCORE_COLOR)
            popup_surface.set_alpha(alpha)
            screen.blit(popup_surface, (popup['pos'][0], popup['pos'][1]))
            if popup['timer'] <= 0:
                score_popups.remove(popup)

        # draw score
        score_text = score_font.render(f"Score:{score}", True, SCORE_COLOR)
        screen.blit(score_text, (20, 15))

        # draw overlay based on game state
        if game_over:
            play_again_rect, quit_rect = draw_game_over(screen)
        elif player_wins:
            play_again_rect, quit_rect = draw_victory(screen, fireworks)


        # update display
        pygame.display.flip()


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run_game()
