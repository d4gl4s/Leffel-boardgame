from pickle import GLOBAL
import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 1000,600
FIELD_DIMENSION = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Programmeerimise projekt")

#Laen pildid ja salvestan nad muutujates
square_red = pygame.image.load("assets/square_red.png")
circle_red = pygame.image.load("assets/circle_red.png")
triangle_red = pygame.image.load("assets/triangle_red.png")
square_blue = pygame.image.load("assets/square_blue.png").convert()
circle_blue = pygame.image.load("assets/circle_blue.png")
triangle_blue = pygame.image.load("assets/triangle_blue.png")
square_gray = pygame.image.load("assets/square_gray.png")
circle_gray = pygame.image.load("assets/circle_gray.png")
triangle_gray = pygame.image.load("assets/triangle_gray.png")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def shape(x,y,dimension,name):
    #WIN.blit("square_"+color, (x,y))
    image_resized = pygame.transform.scale(name, (dimension, dimension))
    WIN.blit(image_resized, (x,y))

def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)
    #pygame.draw.text(text,lefttop=(x,y), width=360, fontname="Boogaloo", fontsize=size,
    #color=color)

def draw_window(score1, score2, turn, selected):
    WIN.fill(BLACK)
    shape(50, 50,400,square_gray)

    #nupud
    draw_text(WIN,"Select a shape:", 20, 500, 150, WHITE )
    shape(500, 200 ,40,square_gray)
    shape(555, 200 ,40,circle_gray)
    shape(610, 200 ,40,triangle_gray)
    if selected == square_blue or selected == square_red:
        shape(500, 200 ,40,selected)
    elif selected == circle_blue or selected == circle_red:
        shape(555, 200 ,40,selected)
    else:
        shape(610, 200 ,40,selected)
    #square(WIDTH * 0.45, HEIGHT * 0.8,40,square_blue)
    #square(WIDTH * 0.45, HEIGHT * 0.8,40,square_blue)
    draw_text(WIN,f"Player 1:   {score1}", 18, 50, 500, WHITE)
    draw_text(WIN,f"Player 2:   {score2}", 18, 200, 500, WHITE )
    if turn%2:
        draw_text(WIN, "PLAYER 1 TURN", 25, 500, 50, BLUE)
    else: 
        draw_text(WIN, "PLAYER 2 TURN", 25, 500, 50, RED)
    pygame.display.update()

def start_screen():
    draw_text(WIN, "PROJEKT", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(WIN, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(WIN, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

def game_over_screen(score1, score2):
    end_text = "DRAW"
    if score1 > score2:
        end_text = "PLAYER 2 WINS"
    if score2 < score1:
        end_text = "PLAYER 1 WINS"

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

def user_click(x,y):
    global FIELD_WIDTH, FIELD_HEIGHT, turn, selected

    #See selectib vastava kuju ja annab sellele värvi, vaadates, kelle kord on hetkel
    if x >= 500 and x <=540 and y >= 200 and y <=240:
        if turn%2:
            selected = square_blue
        else:
            selected = square_red
        print("ruut")
    elif x >= 555 and x <=595 and y >= 200 and y <=240:
        if turn%2:
            selected = circle_blue
        else:
            selected = circle_red
        print("ring")
    elif x >= 610 and x <=650 and y >= 200 and y <=240:
        if turn%2:
            selected = triangle_blue
        else:
            selected = triangle_red
        print("kolmnurk")
    if x >= 50 and x <=450 and y >= 50 and y <=450:
        turn += 1
        if turn%2:
            selected = square_blue
        else:
            selected = square_red
        print("turn canged")
turn = 1
score1 = 0
score2 = 30
selected = square_blue
def main():
    global turn, selected, score1, score2
    running = True
    #game_start = True
    game_over = False
    while running:
        clock.tick(FPS)
        """ if game_start:
            start_screen()
            game_start = False
            score1 = 0
            score2 = 30 """
        if game_over:
            game_over_screen(score1, score2)
            game_over = False
            score1 = 0
            score2 = 0 

        #See funktsioon uuendab pilti
        draw_window(score1, score2, turn, selected)
        if turn%2:
            score1 += 1
        else: 
            score2 += 1
        #turn += 1

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    #user_click()
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    user_click(x,y)
                    waiting = False
        #See on tingimus, mis lõpetab mängu
        """ if score1 >= 5:
            game_over = True """
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()