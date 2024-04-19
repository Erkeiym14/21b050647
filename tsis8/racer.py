import sys

import pygame

import random, time

from pygame.locals import * 




pygame.init()

FPS = 30 #частота кадра 

framepersec = pygame.time.Clock() #создаем обьект clock для частоты 

#colors

BLUE = (0, 0, 255)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

GREY = (128, 128, 128)


#размеры экрана

SCREEN_WIDTH = 400

SCREEN_HEIGHT = 600

SPEED = 20 #скорость игры 

SCORE = 0 #начальный счет




#создаем тексты и устанавливаем шрифты 

font = pygame.font.SysFont("Montserrat-Bold", 60)

font2 = pygame.font.SysFont("Montserrat-Bold", 15)

font_small = pygame.font.SysFont("Montserrat-Bold", 20)

game_over = font.render("GAME OVER", True, BLACK)

background = pygame.image.load("AnimatedStreet.png") #изображение фона загружаем 


#создаем окно игры

screen = pygame.display.set_mode((400, 600))

screen.fill(WHITE) #заполняет экран белым цветом 

pygame.display.set_caption("Racer")#устанавливает заголовок окна игры 



#загружаем фон
background = pygame.image.load('AnimatedStreet.png')






pygame.mixer.Sound('week10_materials_background.wav').play(-1) #воспроизводит фоновой звук и делает его бесконечным (-1 указывает)
class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("Enemy.png")

        self.rect = self.image.get_rect()

        self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0)

#движение врага
    def move(self): #перемещает спрайт вниз по экрану  если он догстигает нижней границв
        # то опять перемещает его вверх и новое случайное положение по экрану 

        self.rect.move_ip(0, 10)

        if (self.rect.bottom > 600):

            self.rect.top = 0

            self.rect.center = (random.randint(30, 370), 0)






#класс игрока
class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__() 

        self.image = pygame.image.load("Player.png")

        self.rect = self.image.get_rect()

        self.rect.center = (160, 520)

 
#движение игрока 
    def move(self):

        pressed_keys = pygame.key.get_pressed()

    

        if self.rect.left > 0:

              if pressed_keys[K_LEFT]:

                  self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:        

              if pressed_keys[K_RIGHT]:

                  self.rect.move_ip(5, 0)



#класс монеты
class Coin(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('coin.png')

        self.rect = self.image.get_rect()

            
# Движение монеты
    def move(self):

        self.rect.move_ip(0, 10)

        if (self.rect.bottom > 600):

            self.rect.top = 0

            self.rect.center = (random.randint(30, 370), 0) 
# Обновление позиции монеты и проверка столкновения с игроком
    def update(self):

        if self.rect.colliderect(Player.rect):

            Player.score += 1

            self.kill()               



#Создаем игрока, врага и монету
p1 = Player()

e1 = Enemy()

c1 = Coin()



#Группы спрайтов
enemies = pygame.sprite.Group()

enemies.add(e1)

coins = pygame.sprite.Group()

coins.add(c1)

all_sprites = pygame.sprite.Group()

all_sprites.add(p1)

all_sprites.add(e1)

all_sprites.add(c1)


#увелечение скорости 
INC_SPEED = pygame.USEREVENT + 1

pygame.time.set_timer(INC_SPEED, 1000)




while True:

    for event in pygame.event.get():

        if event.type == INC_SPEED:

            SPEED += 4

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()       




    screen.blit(background, (0, 0))#рисует фон игрового экрана в начале каждой итерации игрового цикла

     

    #в этой части кода мы двигаем и перерисовываем наши объекты

    for entity in all_sprites:

        screen.blit(entity.image, entity.rect)

        entity.move()

    #Эта часть кода отслеживает столкновения игрока p1 с монетами coins

    if pygame.sprite.spritecollideany(p1, coins):

        

        SCORE += 1 #Увеличивается счетчик SCORE на 1

        c1.rect.center = (random.randint(30, 370), 0)

        pygame.display.update()




    #показывает текущий счет игрока
    score = font2.render(f"Score:{SCORE}", True, BLACK)    

    screen.blit(score, (10, 10))




    if pygame.sprite.spritecollideany(p1, enemies):

        pygame.mixer.Sound('week10_materials_crash.wav').play(1) #проигрывается звук столкновения

        time.sleep(0.5) 




        screen.fill(RED) #экран заполняется красным цветом и выходит гэйм овер

        screen.blit(game_over, (30, 250))

        pygame.display.update()

        for entity in all_sprites:

            entity.kill() #все обьекты уничтожаются

        time.sleep(2) #программа ждет две секунды и закрывается

        pygame.quit()

        sys.exit()        

    

    pygame.display.update() 

    framepersec.tick(FPS)