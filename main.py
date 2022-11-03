from pickle import GLOBAL
import pygame
import sys
import math
import time  
pygame.init()

WIDTH, HEIGHT = 1000,600     #Akna suurus
FIELD_DIMENSION = 400    #Mänguvälja suurus
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Programmeerimise projekt")
font_name = pygame.font.match_font('arial')
FPS = 60
clock = pygame.time.Clock()

#Laen pildid ja salvestan nad muutujatesse
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
turn = 1
score1 = 0
score2 = 0
kujusid_mänguväljal = 0
selected = square_blue
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

def reset_game():   #Funktsioon, mis seab muutujad tagasi algsetele väärtustele
    global turn, score1, score2, kujusid_mänguväljal, selected, field
    turn = 1
    score1 = 0
    score2 = 0
    kujusid_mänguväljal = 0
    selected = square_blue
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

def loogika_ring(row, col):     #Funktsioon, mis paneb paika, kas ringi saab ette antud ruudule paigutada
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

def loogika_kolmnurk(row, col):     #Funktsioon, mis paneb paika, kas kolmnurka saab ette antud ruudule paigutada
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

def shape(x,y,dimension,name):  #Funktsioon, mis joonistab ekraanile kujundi
    image_resized = pygame.transform.scale(name, (dimension, dimension))    #Muudab laetava pildi suurust
    WIN.blit(image_resized, (x,y))  #Laeb pildi vastavatele koordinaatidele
def draw_text(surf, text, size, x, y, color):   #Funktsioon, mis joonistab ekraanile teksti
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)
def draw_text_center(surf, text, size, x, y, color):    #Funktsioon, mis joonistab ekraanile teksti, joondusega keskele
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_window():  #Funktsioon, mis uuendab mängu pilti. Kutsutakse iga kindla aja tagant (FPS korda sekundis)
    global field, score1, score2, turn, selected
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
    #Joonistab skoori ja selle, kumma kord on
    draw_text(WIN,f"Player 1:   {score1}", 18, 50, 500, BLACK)
    draw_text(WIN,f"Player 2:   {score2}", 18, 200, 500, BLACK )

    
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

    if turn%2:
        draw_text(WIN, "PLAYER 1 TURN", 25, 500, 50, BLUE)
    else: 
        draw_text(WIN, "PLAYER 2 TURN", 25, 500, 50, RED)
    pygame.display.update()

def game_over_screen(score1, score2):   #Pilt, mida näitatakse kui mäng lõppeb
    end_text = "DRAW"
    winner_color = BLACK
    if score1 > score2:
        end_text = "PLAYER 2 WINS"
        winner_color = RED
    if score2 < score1:
        end_text = "PLAYER 1 WINS"
        winner_color = BLUE

    WIN.fill(WHITE)
    draw_text_center(WIN, "GAME OVER", 22, WIDTH / 2, HEIGHT / 2, BLACK)
    draw_text_center(WIN, end_text, 64, WIDTH / 2, HEIGHT / 4, winner_color)
    draw_text_center(WIN, "Press any key to start new game!", 18, WIDTH / 2, HEIGHT * 3 / 4, BLACK)
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

def user_click(x,y):    #Funktsioon kutsutakse,kui mängija vajutab ekraanile
    global FIELD_WIDTH, FIELD_HEIGHT, turn, selected, field, score1, score2, kujusid_mänguväljal

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
            kujusid_mänguväljal += 1
            if turn%2:
                selected = square_blue
            else:
                selected = square_red
            print("turn canged")

def main():
    global turn, selected, score1, score2, kujusid_mänguväljal
    running = True
    game_over = False
    while running:
        clock.tick(FPS)
        if game_over:
            game_over_screen(score1, score2)
            reset_game()    #Seab muutujad tagasi mängualgsetele väärtustele
            game_over = False

        draw_window()    #funktsioon, mis uuendab pilti
        if kujusid_mänguväljal >= 2:    #See on tingimus, mis lõpetab mängu
            time.sleep(1.5)
            game_over = True

        waiting = True
        while waiting:  #Ootab mängija sisendit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #Kui mängija paneb akna kinni
                    running = False
                    waiting = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:    #Kui mängija teeb hiirel vajutuse
                    if event.button == 1:   #Kontrollib, kas vajutab vasakut hiireklahvi
                        x, y = event.pos    #Võtab kliki koordinaadid
                        user_click(x,y)
                        waiting = False
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()