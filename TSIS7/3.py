import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Red ball")

clock = pygame.time.Clock()
x = 0
y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 2
    if pressed[pygame.K_DOWN]:
        y += 2
    if pressed[pygame.K_LEFT]:
        x -= 2
    if pressed[pygame.K_RIGHT]:
        x += 2
    
    screen.fill(WHITE)
    if x > 450:
        x = 450
    if x < 0:
        x = 0
    if y > 450:
        y = 450
    if y < 0:
        y = 0

    pygame.draw.ellipse(screen, RED, [x, y, 50, 50])
    clock.tick(60)
    pygame.display.update()

pygame.quit()
