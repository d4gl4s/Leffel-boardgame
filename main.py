import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Programmeerimise projekt")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def start_screen():
    draw_text(WIN, "PROJEKT", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(WIN, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(WIN, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

def game_over_screen(score1, score2):
    end_text = "DRAW"
    if score1 > score2:
        end_text = "PLAYER 1 WINS"
    if score2 < score1:
        end_text = "PLAYER 2 WINS"

    draw_text(WIN, "GAME OVER", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(WIN, end_text, 64, WIDTH / 2, HEIGHT / 4)
    draw_text(WIN, "Press any key to start new game!", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

def main():
    running = True
    game_start = True
    game_over = False
    while running:
        clock.tick(FPS)
        if game_start:
            start_screen()
            game_start = False
            score1 = 0
            score2 = 300
        if game_over:
            game_over_screen(score1, score2)
            game_over = False
            score1 = 0
            score2 = 0 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        score1 += 1

        #See on tingimus, mis lõpetab mängu
        if score1 >= 300:
            game_over = True

        #See funktsioon uuendab pilti
        draw_window()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()