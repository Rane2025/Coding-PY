import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AGC Gaming")
background_image = pygame.transform.scale(pygame.image.load("Shooter obby.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
ACG_Gaming_Mode = pygame.transform.scale(pygame.image.load("Shooter obby.jpeg"), (400, 300))
ACG_Gaming_Mode_rect = ACG_Gaming_Mode.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
text = pygame.font.Font(None, 50).render("AGC Gaming Mode", True, (255, 255, 255))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(ACG_Gaming_Mode, ACG_Gaming_Mode_rect)
        display_surface.blit(text, text_rect)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    game_loop()