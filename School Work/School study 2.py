import pygame

def main():
    pygame.init()
    screen_width, screen_height = 800, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Prince Color")
    colors = {
        'blue': pygame.Color('blue'),
        'green': pygame.Color('cyan'),
        'gray': pygame.Color('gray'),
        'white': pygame.Color('white'),
        'dark blue': pygame.Color('dark blue'),
        'purple': pygame.Color('black'),
        'dark brown': pygame.Color('brown'),
        'orange': pygame.Color('orange')
        }
    
    cc = colors['blue']
    x, y = 15, 15
    sw, sh = 50, 50
    c = pygame.time.Clock()
    d = False
    while not d:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                d = True
            p = pygame.key.get_pressed()
        if p[pygame.K_UP]:
            y -= 1
        if p[pygame.K_DOWN]:
            y += 1
        if p[pygame.K_LEFT]:
            x -= 1
        if p[pygame.K_RIGHT]:
            x += 1
        x = min(max(0, x), screen_width - sw)
        y = min(max(0, y), screen_height - sh)
        screen.fill(colors['orange'])
        pygame.draw.rect(screen, cc, (x, y, sw, sh))
        pygame.display.flip()
        c.tick(60)

    pygame.quit()
if __name__ == "__main__":
    main()