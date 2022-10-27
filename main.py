import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 900,500
FIELD_WIDTH, FIELD_HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Programmeerimise projekt")

#Laen pildid ja salvestan nad muutujates
square_red = pygame.image.load("assets/square_red.png")
circle_red = pygame.image.load("assets/circle_red.png")
triangle_red = pygame.image.load("assets/triangle_red.png")
square_blue = pygame.image.load("assets/square_blue.png")
circle_blue = pygame.image.load("assets/circle_blue.png")
triangle_blue = pygame.image.load("assets/triangle_blue.png")

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

def draw_window(score1, score2):
    WIN.fill(BLACK)
    draw_text(WIN, f"PLAYER 1: {score1}", 18, 100, 200)
    draw_text(WIN, f"PLAYER 2: {score2}", 18, 100, 300)
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

def user_click():
    global FIELD_WIDTH, FIELD_HEIGHT

    #Salvesta klicki koordinaadid muutujatesse
    x, y = pygame.mouse.get_pos()

    #if (kordinaadid ehk click on mänguväljal):
        #if x < FIELD_WIDTH / 10:
            #col = 1
        #elif x < FIELD_WIDTH / 10 * 2
            #col = 2
        #...

        #if x < FIELD_HEIGHt / 10:
            #row = 1
        #elif x < FIELD_HEIGHT / 10 * 2
            #row = 2
        #...
    #elif (koordinaadid on mõnel nupul):
        #
    #else:
        #return
  
    # Siin saaks WIDTHiks võtta mänguvälja widthi ja siis jagada columnite arvuga ehk siis meie juhul 10
    # get column of mouse click (1-3)
    """  
    if(x<WIDTH / 3):
        col = 1   
    elif (x<WIDTH / 3 * 2):
        col = 2   
    elif(x<WIDTH):
        col = 3 
    else:
        col = None """
  
    # get row of mouse click (1-3)
    """ if(y<HEIGHT / 3):
        row = 1
     
    elif (y<HEIGHT / 3 * 2):
        row = 2
     
    elif(y<HEIGHT):
        row = 3
     
    else:
        row = None """
       

    #Vaatab, kas row ja col pole none ning siis vaatab, kas järjendis vastav väli on tühi ja siis lisab sinna
    """ if(row and col and board[row-1][col-1] is None):
        global XO
 
        drawXO(row, col)
        check_win() """
    

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
            score2 = 30
        if game_over:
            game_over_screen(score1, score2)
            game_over = False
            score1 = 0
            score2 = 0 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                user_click()
 
                #Siin saaks teoorias ka mängu lõpetada ma ei tea kumb hetkel parem on
                """ if(winner or draw):
                    reset_game() """
        score1 += 1

        #See on tingimus, mis lõpetab mängu
        if score1 >= 300:
            game_over = True

        #See funktsioon uuendab pilti
        draw_window(score1, score2)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()