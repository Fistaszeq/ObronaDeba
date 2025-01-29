# 1.[Strona główna / Postac]
import pygame as pg
import random as rand

pg.init()


x_res = 400
y_res = 200
a = 0

screen = pg.display.set_mode((x_res,y_res))
# screen.fill((255,255,255))
# pg.display.set_caption("Obrona Dęba. version 0.1")
# pg.display.set_caption("Obrona Dęba. version 0.2")
pg.display.set_caption("Obrona Dęba. version 0.3")
#    # Zmienne
# Twoja pozycja x,y
x = x_res/2
y = 0


bg = pg.image.load("bg1.gif")
bg = pg.transform.scale(bg,(x_res,y_res))

# Animacja chodzenia
move = [
 pg.image.load("mc_run_0.png"),
 pg.image.load("mc_run_1.png"),
 pg.image.load("mc_run_2.png"),
 pg.image.load("mc_run_3.png"),
 pg.image.load("mc_run_4.png"),
 pg.image.load("mc_run_5.png"),
 pg.image.load("mc_run_6.png"),
 pg.image.load("mc_run_7.png")
    ]


# Skalowanie 
xImg = 64
yImg = 64
def scaling(x):
    return pg.transform.scale(x, (xImg, yImg))

move[0] = scaling(move[0])
move[1] = scaling(move[1])
move[2] = scaling(move[2])
move[3] = scaling(move[3])
move[4] = scaling(move[4])
move[5] = scaling(move[5])
move[6] = scaling(move[6])
move[7] = scaling(move[7])

move_p = move[0]


clock = pg.time.Clock()

scena = 0
speed = 3

# NPC
npc_1_x = x_res/2
npc_1_y = 0
npc_image = move[0]

runing = True
while runing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
    if scena == 0 :
        screen.fill((255,255,255))
    elif scena == 1:
        screen.blit(bg,(0,0))
    else:
        screen.fill((0,0,0))


    # Losowy NPC na scenie 3
    if scena == 3:
        npc_1_y = y
        screen.blit(npc_image,(npc_1_x,npc_1_y))
        if x > npc_1_x:
            npc_image = move[0]
    #     if x < npc_1_x:
    #         npc_image = move1r



    screen.blit(move_p,(x,y))
    pg.draw.rect(screen,(70,70,70),(0,y_res-30, 400,y_res))




    # Poruszanie się kalwiszy
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        x += speed
        if x%5 == 0:
            a += 1
        
        if a %2 == 0:
            if a >= 7:
                a = 0
            move_p = move[a]



    if keys[pg.K_a]:
        x -= speed
        if x%5 == 0:
            a += 1
        # [x] Zrób odwrotne grafiki
        if a %2 == 0:
            if a >= 7:
                a = 0
            move_p = move[a]

        
        
        # if a %2 == 0:
        #     move = move2r
        # if a %2 != 0:
        #     move = move1r
        

        

    


    # Przemieszczanie sie po srkaju mapy
    if x > x_res-30:
        x = 40
        scena += 1

    if x < 0 + 30:
        x = x_res - 40
        scena -= 1 


    # Grawitacja 
    if y < y_res-yImg-35: # - 35 bo trawa
        y += 5



    pg.display.flip()




    clock.tick(60)

    
pg.quit()

# 1.Nie interesi bo kici kici
# 2.[Poruszanie postacią] (zrobione)
# 3.[NPC] (primitywnie na scenie 3) (nawet reaguje na to gdzie jesteś)
# 4.[Funkcje na chodzenie każdego obietku NPC też z animacją chodzenia]
# 5.[Zaimportuj grafiki Marka]

