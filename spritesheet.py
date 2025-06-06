import math
import pygame
import sys
from pygame.locals import QUIT

class sprite:
    def __init__(self,spritesheet,spriteheight,spritewidth,emptyunits,speed):
        self.spritesheet = pygame.image.load(spritesheet)
        self.sprtiesheetsize = self.spritesheet.get_rect()
        
        self.spritesheetx, self.spritesheety = self.spritesheet.get_rect().size
        
        self.spriteheight = spriteheight
        self.spritewidth = spritewidth

        self.emptyunits = emptyunits
        self.index = 0
        self.speed = speed
        #.4=24 frames per second times number by 60 (only works with number below or equal to 1 but not 0)

        self.separatesprites = []

        

    def unpack(self,height,length):
        for r in range(self.spritesheety//self.spriteheight):
            for c in range(self.spritesheetx//self.spritewidth):
                sprite = pygame.Surface((self.spritewidth,self.spriteheight),pygame.SRCALPHA,32)
                tempheight = height / self.spriteheight
                templength = length / self.spritewidth
                sprite.blit(self.spritesheet,(0,0),(self.spritewidth*c,self.spriteheight*r,self.spritewidth,self.spriteheight))
                sprite = pygame.transform.scale(sprite,(int(tempheight * self.spriteheight),int(templength*self.spritewidth)))
                self.separatesprites.append(sprite)
    
    def draw(self,surface,x,y):
        #print(self.index)
        surface.blit(self.separatesprites[int(self.index)],(x,y))
        self.index += self.speed
        if self.index >= (self.spritesheetx / self.spritewidth) * (self.spritesheety / self.spriteheight) - self.emptyunits:
            self.index = 0
        
        #if self.index <= len(self.separatesprites) - self.emptyunits:
        #    pass

                



if __name__ == "__main__":
    
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('pygame game')
    DISPLAYSURF = pygame.display.set_mode((500,500))
    invis2 = sprite("./sprites/Icons/invis/invisicon2.png",128,128,6)
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
        invis2.unpack(100,100)
        invis2.draw(DISPLAYSURF,100,100)


        pygame.display.update()
