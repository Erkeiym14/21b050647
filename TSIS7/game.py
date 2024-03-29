import pygame  
from datetime import datetime  
current_datetime = datetime.now()  
sec = current_datetime.second  
min = current_datetime.minute  
print(sec)  
print(min)  
  
  
pygame.init()  
  
screen = pygame.display.set_mode((752, 760))  
background = pygame.image.load('mickey.png').convert()  
right = pygame.image.load('right_hand.png').convert()  
left = pygame.image.load('left_hand.png').convert()  
  
surf1 = pygame.Surface((752, 760))  
surf1.set_colorkey((0, 0, 0))  
surf = pygame.Surface((752, 760))  
surf.set_colorkey((0, 0, 0))  
pygame.display.flip()  
done = False 
  
cnt = sec*6  
angle = sec*6*(-1) + 60 
angle1 = min*6*(-1) + 300  
  
while not done:  
    pygame.time.delay(1000)  
    angle -= 6  
    cnt += 6 
    if cnt == 360:  
        cnt = 0  
        angle1 -= 6 
  
    screen.blit(background, (0, 0))  
    screen.blit(surf, (0, 0))  
    surf.blit(pygame.transform.rotate(right, angle), pygame.transform.rotate(right, angle).get_rect(center=(752/2, 760/2)))  
    screen.blit(surf1, (0, 0))  
    surf1.blit(pygame.transform.rotate(left, angle1), pygame.transform.rotate(left, angle1).get_rect(center=(752/2, 760/2)))
  
      

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()   
  
pygame.quit()