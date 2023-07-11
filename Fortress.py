import pygame
import random

pygame.init()

width = 800
height = 600

# Thanks Mun

game_display = pygame.display.set_mode((width, height))

black = (0, 0, 0)

white = (255, 255, 255)

clock = pygame.time.Clock()
pygame.display.set_caption("Fortress v.s. BETA")

# All sprite loads
crashed = False
char_1 = pygame.image.load('New Merv-veed-remove-background (2).png')
i_vert = pygame.image.load('I-Vertical-veed-remove-background (1).png')
o = pygame.image.load('O-veed-remove-background (1).png')

#Sprite functions and game_display.blit()
def char(x, y):
    game_display.blit(char_1, (x, y))


x = (width * 0.45)
y = (height * 0.8)
x_change = 0

y_change = 0

obx_rand = random.uniform(0.01, 1)
oby_rand = random.uniform(-0.01, -0.10)


def random_ivert(obx, oby):
    game_display.blit(i_vert, (obx, oby))


obx = (width * obx_rand)
oby = (height * oby_rand)


def random_o(obx_2, oby_2):
    game_display.blit(o, (obx_2, oby_2))

obx_rand_2 = random.uniform(0.01, 0.80)
oby_rand_2 = random.uniform(-0.01, -0.10)

obx_2 = (width * obx_rand_2)
oby_2 = (height * oby_rand_2)


# MAIN LOOP
while not crashed:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            crashed = True
    # Main Controls
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -0.5
        elif event.key == pygame.K_RIGHT:
            x_change = 0.5
        elif event.key == pygame.K_UP:
            y_change = -0.5
        elif event.key == pygame.K_DOWN:
            y_change = 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
        if event.key == pygame.K_DOWN:
            y_change = 0
        if event.key == pygame.K_UP:
            if y_change == -0.5:
                y_change += 0.7

    # Update and quit function below, along with final move function.
    x += x_change
    y += y_change
    char(x, y)
    random_ivert(obx, oby)
    random_o(obx_2, oby_2)
    pygame.display.update()

pygame.quit()