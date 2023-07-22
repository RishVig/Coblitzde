import pygame
import random

pygame.init()

window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width,window_height))
o_block = pygame.image.load('O-veed-remove-background (1).png')
i_block = pygame.image.load('I-Vertical-veed-remove-background (1).png')
merv = pygame.image.load('merv_official.png')
logo = pygame.image.load('logo.png')
characters = [o_block,i_block]
choice = random.choice(characters)
random_block_x = random.randint(0,300)
random_block_y = random.randint(0,5)
death = False
black = (0,0,0)
counter = 1
class block_transfer:
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
    def blit(self):
        game_window.blit(choice,(self.x,self.y))
    def update(self):
        self.y += 3
        if self.y in range(600, 800):
            game_window.blit(choice, (0,0))
                       
y_change = 0

def character_load(xc,yc):
    game_window.blit(merv, (xc,yc))
block_x = 0
block_y = 0
xc = window_width * 0.5
yc = window_height * 0.5
xc_change =0
yc_change = 0
block_load = block_transfer(random_block_x,random_block_y)

clock = pygame.time.Clock()
while not death:
    game_window.fill(black)
    
    block_load.update()
    block_load.blit()
    

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            death = True
        if event.type == pygame.KEYDOWN:
            block_y -= 10

            if event.key == pygame.K_UP:
                yc_change -= 10
            if event.key == pygame.K_DOWN:
                yc_change += 10

            if event.key == pygame.K_LEFT:
                xc_change -= 10
            if event.key == pygame.K_RIGHT:
                xc_change += 10
        if event.type == pygame.KEYUP:
                xc_change = 0
                yc_change = 0
                   
           
    yc += yc_change
    xc += xc_change    
    character_load(xc, yc)
    pygame.display.update()
    
    clock.tick(60)
pygame.quit()
