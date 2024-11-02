import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pokemon battle game')

font = pygame.font.Font(None, 40)
print(pygame.display.get_surface().get_size())

while True:
    print('Running...')
    screen.fill('white')
    welcome_text = font.render('Welcome to the battle', True, 'black')
    screen.blit(welcome_text, (300, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

pygame.display.flip()
