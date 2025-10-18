import pygame
import random

# Initialize Pygame
pygame.init()

# Define custom events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define color constants
BLUE = pygame.Color('blue')
LIGHT_BLUE = pygame.Color('lightblue')
DARK_BLUE = pygame.Color('darkblue')
WHITE = pygame.Color('white')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        # Bounce off the sides
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        # Bounce off the top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([BLUE, LIGHT_BLUE, DARK_BLUE, YELLOW, MAGENTA, ORANGE]))

# Function to change background color
def change_background_color():
    return random.choice([BLUE, LIGHT_BLUE, DARK_BLUE, YELLOW, MAGENTA, ORANGE])

# Create sprite group and add one sprite
all_sprites = pygame.sprite.Group()
sp1 = Sprite(BLUE, 50, 50)
sp1.rect.x = random.randint(0, 750)
sp1.rect.y = random.randint(0, 550)
all_sprites.add(sp1)

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Colorful Sprite")

# Set initial background color
bg_color = BLUE

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            bg_color = change_background_color()

    # Update sprite positions
    all_sprites.update()

    # Fill screen with current background color
    screen.fill(bg_color)

    # Draw sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(240)

# Quit pygame
pygame.quit()
