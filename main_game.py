import pygame
import math

#initialize Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Draw a blue rectangle to represent the sprite
        self.image = pygame.Surface([50, 50])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.bottom = SCREEN_HEIGHT
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)

pygame.init()

clock = pygame.time.Clock()
FPS = 50

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Cowboy")

#load image
bg = pygame.image.load("assets/scroll_background.jpg").convert()
bg_width = bg.get_width()
bg_height = bg.get_height()

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

#game loop
player = Player()
run = True
while run:
    clock.tick(FPS)

    #update player
    player.speed = pygame.math.Vector2(5, 0)
    player.update()
    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    #update and reset scroll
    scroll -= 5
    if abs(scroll) > bg_width:
        scroll = 0
    #screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()