import pygame

def main():
    pygame.init()
    screen_width, screen_height = 800, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Legend of Python")
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'white': pygame.Color('white'),
        'black': pygame.Color('black'),
        'yellow': pygame.Color('yellow'),
        'purple': pygame.Color('purple'),
        'orange': pygame.Color('orange'),
        'pink': pygame.Color('pink'),
        'cyan': pygame.Color('cyan')
        }
    
    current_color = colors['cyan']
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 5
        if pressed[pygame.K_DOWN]:
            y += 5
        if pressed[pygame.K_LEFT]:
            x -= 5
        if pressed[pygame.K_RIGHT]:
            x += 5
        
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0: current_color = colors['purple']
        if x == screen_width - sprite_width: current_color = colors['orange']
        if y == 0: current_color = colors['pink']
        if y == screen_height - sprite_height: current_color = colors['cyan']
        else : current_color = colors['white']
        screen.fill(colors['black'])
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()

if __name__ == "__main__":
    main()