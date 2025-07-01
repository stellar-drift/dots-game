
# --- overlay --- #


import pygame
from settings import WIDTH, HEIGHT, FONT_NAME, FONT_SIZE_LG, FONT_SIZE_SM, SCORE_BAR_COLOR, SCORE_COLOR, BACKGROUND_COLOR


pygame.font.init()

message_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE_LG, bold = True)
button_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE_SM, bold = True)


def draw_buttons(screen, mouse_pos):
    # button dimensions
    button_width = 150
    button_height = 40
    play_again_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 20, button_width, button_height)
    quit_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50, button_width, button_height)

    # colors
    play_color = SCORE_BAR_COLOR if play_again_rect.collidepoint(mouse_pos) else BACKGROUND_COLOR
    quit_color = SCORE_BAR_COLOR if quit_rect.collidepoint(mouse_pos) else BACKGROUND_COLOR

    # draw with rounded corners
    pygame.draw.rect(screen, play_color, play_again_rect, border_radius=12)
    pygame.draw.rect(screen, quit_color, quit_rect, border_radius=12)

    # button labels
    play_text = button_font.render("play again", True, SCORE_COLOR)
    quit_text = button_font.render("quit", True, SCORE_COLOR)

    screen.blit(play_text, (play_again_rect.centerx - play_text.get_width() // 2,
                            play_again_rect.centery - play_text.get_height() // 2))
    screen.blit(quit_text, (quit_rect.centerx - quit_text.get_width() // 2,
                            quit_rect.centery - quit_text.get_height() // 2))

    return play_again_rect, quit_rect

def draw_game_over(screen):
    # draw a dark overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(SCORE_BAR_COLOR)
    screen.blit(overlay, (0, 0))

    # message
    end_text = message_font.render("IT'S OVER!", True, SCORE_COLOR)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - 100))

    # get current mouse position
    mouse_pos = pygame.mouse.get_pos()

    return draw_buttons(screen, mouse_pos)

def draw_victory(screen, fireworks):
    # draw a dark overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(SCORE_BAR_COLOR)
    screen.blit(overlay, (0, 0))

    # message
    win_text = message_font.render("YOU WIN!", True, SCORE_COLOR)
    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 100))

    # draw and update fireworks animation
    for firework in fireworks:
        firework.update()
        firework.draw(screen)


    # get current mouse position
    mouse_pos = pygame.mouse.get_pos()

    return draw_buttons(screen, mouse_pos)


