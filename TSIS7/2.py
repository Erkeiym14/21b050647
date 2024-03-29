import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Playlist Erke')


songs = ['1.wav', '2.wav', '3.wav']
order = 0
current = songs[order]
path = os.path.join('TSIS7/', current)
pygame.mixer.music.load(path)

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        _path = path.replace( '/' , os.sep).replace('\\', os.sep)
        image = pygame.image.load(_path)
        _image_library[path] = image
    return image


pygame.mixer.music.play(0) 
def next(): 
    global order 
    global current 
    global songs 
    global path 
 
    order -=1 
    current=songs[order] 
    path=os.path.join("TSIS7/",current) 
    pygame.mixer.music.load(path) 
    pygame.mixer.music.play(0) 
 

def previous(): 
        global order 
        global current 
        global songs 
        global path 
        order -=1 
        current=songs[order] 
        path=os.path.join("TSIS7/",current) 
        pygame.mixer.music.load(path) 
        pygame.mixer.music.play(0) 
done=False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:  
                pygame.mixer.music.pause() 
            else:
                pygame.mixer.music.unpause()  
            if event.key == pygame.K_LEFT:  
                previous() 
            if event.key == pygame.K_RIGHT:  
                next()    
        


    pygame.display.flip()