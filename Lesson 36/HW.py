import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background_color = pygame.transform.scale(pygame.image.load("Guess the Brainrot.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Pixel Art", FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('darkblue'))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(12, min(SCREEN_WIDTH - self.rect.width, self.rect.x + x_change)) 
        self.rect.y = max(12, min(SCREEN_HEIGHT - self.rect.height, self.rect.y + y_change))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guess the Brainrot")
allsp = pygame.sprite.Group()
sp1 = Sprite(pygame.Color('red'), 50, 50)
sp1.rect.x = random.randint(0, SCREEN_WIDTH - sp1.rect.width)
sp1.rect.y = random.randint(0, SCREEN_HEIGHT - sp1.rect.height)
allsp.add(sp1)
sp2 = Sprite(pygame.Color('green'), 50, 50)
sp2.rect.x = random.randint(0, SCREEN_WIDTH - sp2.rect.width)
sp2.rect.y = random.randint(0, SCREEN_HEIGHT - sp2.rect.height)
allsp.add(sp2)
running, won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    x_change, y_change = 0, 0
    if keys[pygame.K_LEFT]:
        x_change = -MOVEMENT_SPEED
    elif keys[pygame.K_RIGHT]:
        x_change = MOVEMENT_SPEED
    elif keys[pygame.K_UP]:
        y_change = -MOVEMENT_SPEED
    elif keys[pygame.K_DOWN]:
        y_change = MOVEMENT_SPEED
    sp1.move(x_change, y_change)
    if pygame.sprite.collide_rect(sp1, sp2):
        won = True
        running = False
    screen.blit(background_color, (0, 0))
    allsp.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

print("Thank you for playing Guess the Brainrot!")