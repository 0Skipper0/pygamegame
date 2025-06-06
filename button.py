
import pygame
import sys
from pygame.locals import QUIT


class button:
    def __init__(self,png1,png2,size,pos):
        self.size = size
        self.pos = pos
        self.png1 = pygame.image.load(png1)
        self.png1 = pygame.transform.scale(self.png1,self.size)
        self.buttonrect = self.png1.get_rect(center = pos)
        self.png2 = pygame.image.load(png2)
        self.png2 = pygame.transform.scale(self.png2,self.size)
        
    def draw(self,surface,hoverd):
        if hoverd:
            surface.blit(self.png2,self.buttonrect)
        else:
            surface.blit(self.png1,self.buttonrect)

class slider:
    def __init__(self,max,min,pos,initvaule):
        self.max = max
        self.min = min
        self.pos = pos
        self.value = initvaule

        self.width = 25
        self.circlewidth = self.width*(4/5)
        self.outlinethic = 10
        self.length = self.max + (2*self.circlewidth)
        
    
        self.outline = pygame.Rect(self.pos[0],self.pos[1],self.length,self.width)
        self.fill = pygame.Rect(self.pos[0]+5,self.pos[1]+5,self.length-10,self.width-self.outlinethic)

        self.circlerect = pygame.Rect(self.pos[0],self.pos[1],self.circlewidth,self.circlewidth)

        self.circlex = self.pos[0]
        
    def draw(self,surface):
        
        
        self.circlerect.center = (self.circlex,self.pos[1]+(self.width/2))
        
        pygame.draw.rect(surface,(0,0,0),self.outline,width=5)
        pygame.draw.rect(surface,(124, 158, 178),self.fill)

        
        pygame.draw.circle(surface,(100,200,255),self.circlerect.center,self.circlewidth)
        pygame.draw.circle(surface,(0,0,0),self.circlerect.center,self.circlewidth,width= 5)

        
    def update(self,event):
        
        mousepos = pygame.mouse.get_pos()
        if self.outline.collidepoint(mousepos) and event.type == pygame.MOUSEBUTTONDOWN:
            print("collide")
            if mousepos[0] < (self.pos[0]+self.circlewidth):
                self.circlex = self.pos[0]+self.circlewidth
                self.value = self.min
            elif mousepos[0] > ((self.pos[0]+self.length) - self.circlewidth):
                self.circlex = self.pos[0]+self.length - self.circlewidth
                self.value = self.max
            else:
                self.circlex = mousepos[0]
                self.value = self.circlex - self.pos[0]
            print(self.value)

        

        

        
        
    









if __name__ == "__main__":
    
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('pygame game')
    DISPLAYSURF = pygame.display.set_mode((800,500))
    slider2 = slider(600,10,(100,100),600)
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

        DISPLAYSURF.fill((200,200,200))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            slider2.update(event)
            
            
        slider2.draw(DISPLAYSURF)

        


        pygame.display.update()
