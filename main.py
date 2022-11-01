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

def draw_window(score1, score2, turn):
    WIN.fill(BLACK)
    shape(50, 50,400,square_gray)

    #nupud
    draw_text(WIN,"Select a shape:", 20, 500, 150, WHITE )
    shape(500, 200 ,40,square_blue)
    shape(555, 200 ,40,circle_gray)
    shape(610, 200 ,40,triangle_gray)
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
    #game_start = True
    game_over = False
    turn = 1
    score1 = 0
    score2 = 30
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
        draw_window(score1, score2, turn)
        if turn%2:
            score1 += 1
        else: 
            score2 += 1
        turn += 1

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    #user_click()
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    # siin vaata iga shape'i kas click on sinna
                    #if square_blue.get_rect().collidepoint(x, y):
                        #print(x)

                    #See hard-coding esimese nupu näiteks, mis kui mõelda ongi suht parim variant, lihtsalt pane lõppu or... ja kontrolli teist kahte nuppu ka
                    if x >= 500 and x <=540 and y >= 200 and y <=240:
                        print(x)
        #See on tingimus, mis lõpetab mängu
        if score1 >= 5:
            game_over = True
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()