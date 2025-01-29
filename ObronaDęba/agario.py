import pygame

# Inicjalizacja PyGame
pygame.init()

# Ustawienia okna gry
win_y = 800
win_x = 600

j = 800
aj = 0
screen = pygame.display.set_mode((win_y, win_x))
pygame.display.set_caption("agar.io")

# Kolory
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
COLOR = (145,253,136)

ground_y = 2000
ground_x = win_x

background = pygame.image.load('floppa.png')

# Współrzędne i rozmiar obiektu
x, y = 100, 100
width, height = 50, 50
velocity = 10

# Główna pętla gry
running = True
while running:

    pygame.time.delay(15)  # Opóźnienie dla płynności gry
    j =- 1
    # Przechwycenie zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Odczytywanie stanu klawiszy
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        for i in range(1,-1,-1):
            y -= 5

    # if keys[pygame.K_DOWN]:
    #     y += velocity

    if y <= 500 - 70:
        y = y + 4

    if x == 0 or x == 600:
        
        x = win_x / 2
        if aj == 0:
            WHITE = COLOR
        elif aj % 2  ==0:
            WHITE = BLACK

  


    
    # Odświeżanie ekranu
    screen.fill(WHITE)  # Wypełnienie tłeo
    pygame.draw.rect(screen, BLACK, (0,500, ground_y, ground_x)) # Ground
    screen.blit(background, (x, y))
    screen.blit(background, (300, j))
    pygame.display.update()  # Aktualizacja ekranu

# Zakończenie gry
pygame.quit()
