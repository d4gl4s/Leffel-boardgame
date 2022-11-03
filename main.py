from pickle import GLOBAL
import pygame
import sys
import math  
pygame.init()

WIDTH, HEIGHT = 1000,600
#Mänguvälja dimensioonid
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
väli = pygame.image.load("assets/väli.png")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

#Katsetuseks, lisasin mänguväljale alguses juba mõned kujud
field = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

def loogika_ring(row, col):
    paremale = False
    vasakule = False
    alla = False
    üles = False
    paremale_indeks = col +1
    vasakule_indeks = col -1
    üles_indeks = row -1
    alla_indeks = row +1
    
    while paremale_indeks <= 7 and paremale == False:
        if field[row][paremale_indeks] == square_red or field[row][paremale_indeks] == square_blue:
            paremale = True
        else:
            paremale_indeks +=1

    while vasakule_indeks >= 0 and vasakule == False:
        if field[row][vasakule_indeks] == square_red or field[row][vasakule_indeks] == square_blue:
            vasakule = True
        else:
            vasakule_indeks -=1

    while alla_indeks <= 7 and alla == False:
        if field[alla_indeks][col] == square_red or field[alla_indeks][col] == square_blue:
            alla = True
        else:
            alla_indeks +=1

    while üles_indeks >= 0 and üles == False:
        if field[üles_indeks][col] == square_red or field[üles_indeks][col] == square_blue:
            üles = True
        else:
            üles_indeks -=1

    if üles and alla or paremale and vasakule:
        return True
    else:
        return False

def loogika_kolmnurk(row, col):
    paremale = False
    vasakule = False
    alla = False
    üles = False
    paremale_indeks = col +1
    vasakule_indeks = col -1
    üles_indeks = row -1
    alla_indeks = row +1
    
    while paremale_indeks <= 7 and paremale == False:
        if field[row][paremale_indeks] == circle_red or field[row][paremale_indeks] == circle_blue:
            paremale = True
        else:
            paremale_indeks +=1

    while vasakule_indeks >= 0 and vasakule == False:
        if field[row][vasakule_indeks] == circle_red or field[row][vasakule_indeks] == circle_blue:
            vasakule = True
        else:
            vasakule_indeks -=1

    while alla_indeks <= 7 and alla == False:
        if field[alla_indeks][col] == circle_red or field[alla_indeks][col] == circle_blue:
            alla = True
        else:
            alla_indeks +=1

    while üles_indeks >= 0 and üles == False:
        if field[üles_indeks][col] == circle_red or field[üles_indeks][col] == circle_blue:
            üles = True
        else:
            üles_indeks -=1

    if üles and alla or paremale and vasakule:
        return True
    else:
        return False


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
    global field
    WIN.fill(WHITE)
    shape(50, 50,400,väli)

    #joonistab mänguvälja
    for row in range(8):
        for col in range(8):
            #Kui mänguvälja ruut pole tühi
            if field[row][col] != 0:
                #Leian selle ruudu koordinaadid ülemises vasakus nurgas
                x = col*50 + 50
                y = row*50 + 50
                #Joonistan vastava kuju mänguväljale
                shape(x,y,50,field[row][col])
            else:
                continue

    #buttons
    draw_text(WIN,"Select a shape:", 20, 500, 150, BLACK )
    shape(500, 200 ,40,square_gray)
    shape(555, 200 ,40,circle_gray)
    shape(610, 200 ,40,triangle_gray)

    #Joonistab valitud kuju
    if selected == square_blue or selected == square_red:
        shape(500, 200 ,40,selected)
    elif selected == circle_blue or selected == circle_red:
        shape(555, 200 ,40,selected)
    else:
        shape(610, 200 ,40,selected)
    #square(WIDTH * 0.45, HEIGHT * 0.8,40,square_blue)
    #square(WIDTH * 0.45, HEIGHT * 0.8,40,square_blue)

    #Joonistab skoori ja selle, kumma kord on
    draw_text(WIN,f"Player 1:   {score1}", 18, 50, 500, BLACK)
    draw_text(WIN,f"Player 2:   {score2}", 18, 200, 500, BLACK )
    if turn%2:
        draw_text(WIN, "PLAYER 1 TURN", 25, 500, 50, BLUE)
    else: 
        draw_text(WIN, "PLAYER 2 TURN", 25, 500, 50, RED)
    pygame.display.update()

#Hetkel pole kasutusel, kuid pilt, mida näitab mängu algul
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

#Game over ekraan
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
    global FIELD_WIDTH, FIELD_HEIGHT, turn, selected, field, score1, score2

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
    
    #Kui click on mänguväljad
    if x >= 50 and x <=450 and y >= 50 and y <=450:
        #Siin määrad ära, mis row ja col ning muudad vastava väärtuse fieldi järjendis ära selleks surfaceiks
        row = math.floor((y-50)/50)
        col = math.floor((x-50)/50)

        if field[row][col] == 0: #Vaatab, kas ruut mänuväljal on tühi
            if selected == square_blue or selected == square_red:
                field[row][col] = selected
                if turn%2:
                    score1 += 1
                else:
                    score2 += 1
            elif selected == circle_blue or selected == circle_red:
                if loogika_ring(row, col):
                    field[row][col] = selected
                    if turn%2:
                        score1 += 2
                    else:
                        score2 += 2
                else:
                    return
            elif selected == triangle_blue or selected == triangle_red:
                if loogika_kolmnurk(row, col):
                    field[row][col] = selected
                    if turn%2:
                        score1 += 3
                    else:
                        score2 += 3
                else:
                    return

            #Moodab mängijat ning paneb valitud kujuks jälle ruudu
            turn += 1
            if turn%2:
                selected = square_blue
            else:
                selected = square_red
            print("turn canged")
turn = 1
score1 = 0
score2 = 0
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
        """ if turn%2:
            score1 += 1
        else: 
            score2 += 1 """
        #turn += 1

        waiting = True
        while waiting:
            for event in pygame.event.get():
                #Kui mängija paneb akna kinni
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                    pygame.quit()
                    sys.exit()
                
                #Kui mängija teeb hiirel vajutuse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Kontrollib, kas vajutab vasakut hiireklahvi
                    if event.button == 1:
                        x, y = event.pos #Võtab kliki koordinaadid
                        user_click(x,y)
                        waiting = False
        #See on tingimus, mis lõpetab mängu
        """ if score1 >= 5:
            game_over = True """
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()