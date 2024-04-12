import random

#import sys

#from time import time

import pygame




pygame.init()

screen = pygame.display.set_mode((800, 800))

font2 = pygame.font.SysFont("Verdana", 15)




class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 5  # Right.
        self.dy = 0  # Left
        self.is_add = False
        self.speed = 30
        self.level = 1
        self.score = 0


    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)


    def add_to_snake(self):
        self.size += 1
        self.score += 1 #+1 to score if snace ate food
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 5 == 0: #if snake ate more than 5 food its speed increases and it goes to the next level
            self.speed += 5
            self.level += 1


    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False


class Food:
    def __init__(self):
        self.x = random.randint(15, 790)
        self.y = random.randint(15, 790)


    def gen(self):
        self.x = random.randint(15, 790)
        self.y = random.randint(15, 790)


    def draw(self):
        pygame.draw.ellipse(screen, (0, 255, 0), (self.x, self.y, 10, 10))


class Block:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 700)

    def draw(self):
        pygame.draw.rect(screen, (128, 128, 128), (self.x, self.y, 50, 100))    


snake1 = Snake(100, 100)
food = Food()
block = Block()

running = True

FPS = 30
d = 5

clock = pygame.time.Clock()

while running:
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            
    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        food.gen()   

    x = snake1.elements[0][0]
    y = snake1.elements[0][1]

    #cheking gor the snake is leaving the playing area
    if x == 790 and 0 <= y <= 790 or x ==0 and 0<=y <=790 or y == 0 and 0<=x<=790 or y == 790 and 0<=x<=790:
        pygame.quit()  

    #checking for block collusion
    if block.x-10<= x <=block.x+60 and block.y-10<=y<=block.y+110:
        pygame.quit()  

    #generating position of food, so that it doesn't fall on a wall or a snake    
    if food.x == block.x or food.y == block.y:
        food.gen()    

    snake1.move()
    screen.fill((0, 0, 0))
    snake1.draw() 
    food.draw()
    block.draw()

#shows score and level in the screen
    score = font2.render(f"Score:{snake1.score}", True, (255, 255, 255))
    level = font2.render(f'Level:{snake1.level}', True, (255, 255, 255))    
    screen.blit(score, (10, 10))
    screen.blit(level, (10, 30))

    pygame.display.flip()

pygame.quit()