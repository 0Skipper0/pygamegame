import pygame
import player
import random
import sys
from pygame.locals import QUIT


class wall():

    def __init__(self,x,y,derection,id):
        self.x = x
        self.y = y

        self.id = id
        self.hp = 3

        

        
        # true = horizontal, false vertical
        self.derection = derection
        
        if derection == "left" or derection == "right":
            self.size = (random.randint(20,75),random.randint(150,250))

        else:
            self.size = (random.randint(150,250),random.randint(25,75))
            
        
        self.rect = pygame.Rect((0,0),self.size)
        if self.derection == "up":
            self.rect.center = (self.x,self.y-100)
        if self.derection == "down":
            self.rect.center = (self.x,self.y+100)
        if self.derection == "left":
            self.rect.center = (self.x-100,self.y)
        if self.derection == "right":
            self.rect.center = (self.x + 100,self.y)
        
        self.breaking1 = pygame.image.load("./sprites/breaking/breaking1.png")
        self.breaking1 = pygame.transform.scale(self.breaking1,self.size)

        self.breaking2 = pygame.image.load("./sprites/breaking/breaking2.png")
        self.breaking2 = pygame.transform.scale(self.breaking2,self.size)
        
    
    def draw(self,surface):
        if self.id == 1:
            pygame.draw.rect(surface,(3, 227, 252),self.rect)
        elif self.id == 2:
            pygame.draw.rect(surface,(252, 3, 3),self.rect)
        if self.derection == "left" or self.derection == "right":
            if self.hp == 2:
                temp = pygame.transform.scale(self.breaking1, self.size)
                
                surface.blit(temp,self.rect)
            if self.hp == 1:
                
                temp = pygame.transform.scale(self.breaking2, self.size)
                
                surface.blit(temp,self.rect)
        else:
            if self.hp == 2:
                
                temp = pygame.transform.scale(self.breaking1, (self.size[1],self.size[0]))
                temp = pygame.transform.rotate(temp,90)
                
                
                
                surface.blit(temp,self.rect)
            if self.hp == 1:
                temp = pygame.transform.scale(self.breaking2, (self.size[1],self.size[0]))
                temp = pygame.transform.rotate(temp,90)

                
                
                
                surface.blit(temp,self.rect)


    
    # def collide(self,player):
    #     pass

    # def block(self):
    #     pass


if __name__ == "__main__":
    
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('pygame game')
    DISPLAYSURF = pygame.display.set_mode((500,500))
    wall1 = wall(100,100,False)
    clock = pygame.time.Clock()
    running = True
    fps = 60
    frames = 0

    seconds = 1 * 60
    while running:
        
        clock.tick(fps)
        frames += 1
        if frames % 60 == 0:
            seconds -= 1


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        DISPLAYSURF.fill((0,0,0))
        wall1.draw(DISPLAYSURF)
        pygame.display.update()