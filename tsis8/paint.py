import random 
 
import pygame 
 
def main(): 
    screen = pygame.display.set_mode((700, 700)) 
    mode = 'random' 
    draw_on = False 
    last_pos = (0, 0) 
    color = (255, 128, 0) 
    radius = 1 
 
    colors = { 
        'red': (255, 0, 0), 
        'blue': (0, 0, 255), 
        'green': (0, 255, 0), 
        'black' : (0,0,0) 
    } 
    # x1 = random.randint(0,700) 
    # y1 = random.randint(0,700) 
    
    def rec(x1,y1,z1,w1): 
        pygame.draw.rect(screen,(255,255,255),[x1,y1,z1,w1],radius) 
    def elo(x1,y1,z1,w1): 
        pygame.draw.ellipse(screen,(255,255,255),[x1,y1,z1,w1],radius) 
    def tr(x1,y1,z1,w1): 
        pygame.draw.lines(screen, (255,255,255), [x1,y1],[z1, w1], radius) 
        # pygame.draw.line(screen, (255,255,255), [x1,y1],[300, 300], radius) 
    done = False 
    while not done: 
        pressed = pygame.key.get_pressed() 
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT] 
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL] 
 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_w and ctrl_held: 
                    pass 
                if event.key == pygame.K_F4 and alt_held: 
                    pass 
                if event.key == pygame.K_r: 
                    mode = 'red' 
                if event.key == pygame.K_b: 
                    mode = 'blue' 
                if event.key == pygame.K_g: 
                    mode = 'green' 
                if event.key == pygame.K_w: 
                    mode = 'black' 
                    radius = 20 
                if event.key == pygame.K_q: 
                    mode = 'random' 
                    radius = 1 
                if event.key == pygame.K_DOWN: 
                    radius -= 1 
                if event.key == pygame.K_UP: 
                    radius += 1 
                if event.key == pygame.K_a: 
                    x1 = int(input()) 
                    y1 = int(input()) 
                    z1 = int(input()) 
                    w1 = int(input()) 
                    rec(x1,y1,z1,w1) 
                if event.key == pygame.K_s: 
                    x1 = int(input()) 
                    y1 = int(input()) 
                    z1 = int(input()) 
                    w1 = int(input()) 
                    elo(x1,y1,z1,w1) 
                if event.key == pygame.K_p: 
                    x1 = int(input()) 
                    y1 = int(input()) 
                    z1 = int(input()) 
                    w1 = int(input()) 
                    tr(x1,y1,z1,w1) 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if mode == 'random': 
                    color = (random.randrange(256), random.randrange(256), random.randrange(256)) 
                else: 
                    color = colors[mode] 
 
                pygame.draw.circle(screen, color, event.pos, radius) 
                draw_on = True 
            if event.type == pygame.MOUSEBUTTONUP: 
                draw_on = False 
            if event.type == pygame.MOUSEMOTION: 
                if draw_on: 
                    pygame.draw.line(screen, color, last_pos, event.pos, radius) 
                last_pos = event.pos 
        pygame.display.flip() 
 
    pygame.quit() 
 
main() 
