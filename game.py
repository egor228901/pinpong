
from time import sleep
from time import time as TIME
from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed
        

class Ball(GameSprite):
    def update(self):
        #логика тудр-сюда
        ...
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("шутер")
background = transform.scale(image.load("пинпонг.jpg"),(win_width,win_height))
clock = time.Clock()    
FPS = 60 

mixer.init()
mixer.music.load("FRIENDLY_THUG_52_NGG_-_Lost_Angeles_76929092.mp3")
mixer.music.play()

font.init()
font = font.Font(None,20)


player  = Player('ракетка пинпонг.png',50,400,10)
player2 = Player("рвуетка.png", 550,400,10)
game = True
while game:
    
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            ...
    player.reset()        
    player.update()
    player2.reset()        
    player2.update()
    clock.tick(FPS)
    display.update()




   