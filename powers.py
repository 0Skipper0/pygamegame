import pygame
import player
import spritesheet

#example = spritesheet.sprite("file",sizeofsinglespriteX,SizeofSingleSpriteY)

#example.unpack(sizeYouWantTheSpriteTOBeDisplayedX,sizeYouWantTheSpriteTOBeDisplayedY)

invis2 = spritesheet.sprite("./sprites/Icons/invis/invisicon2.png",128,128,6,.4)
wip = spritesheet.sprite("./sprites/wip.png",32,32,0,.2)
hammer = spritesheet.sprite("./sprites/hammerspritesheet.png",18,22,0,.2)
class powers():
    def __init__(self,cooldownTime,durationTime,id,images):
        self.cooldownTime = cooldownTime
        self.durationTime = durationTime

        self.cooldown = cooldownTime
        self.duration = durationTime
        self.active = False
        self.cooldownSeconds = 0

        self.id = id
        self.font = pygame.font.Font("./Daydream.ttf",32)
        self.images = []
            
            
        self.bgbarcolor = (0,0,0)
        self.frame = 0
        self.imageIndex = 0

        self.start = False

        wip.unpack(100,100)
        

    
    # def time(self):
    #     if not self.active:
    #         self.cooldown -= 1
    #         self.duration = self.durationTime
    #     if self.cooldown <= 0 and self.active == True:
    #         self.duration -= 1
    #         self.active = True
    #         if self.duration <= 0:
    #             self.active = False
    #             self.cooldown = self.cooldownTime
    def startup(self):
        invis2.unpack(100,100)
        if self.start == False:
            self.start = True
            invis2.unpack(100,100)
        
    def activated(self):
        if self.active:
            self.duration -= 1
    
    def coolingDown(self):
        if not self.active and self.cooldown < self.cooldownTime:
            self.cooldown += 1
            if self.cooldown % 60 == 0:
                self.cooldownSeconds += 1
        

    #def start(self):   we can do that in player.py
                    
    def finish(self):
        if self.active and self.duration < 0:
            self.active = False
            self.duration = self.durationTime
            self.cooldown = 0
            self.cooldownSeconds = 0
    def reset(self):
        self.cooldown = self.cooldownTime
        self.duration = self.durationTime
        self.active = False
        self.cooldownSeconds = 0
    def update(self):
        self.frame += 1
        if self.frame >= 61:
            self.frame = 0
        if self.frame % 10 == 0:
            self.imageIndex += 1
            if self.imageIndex >= len(self.images):
                self.imageIndex = 0
        #self.debug


    def debug(self):
        #print(f'id: {self.id} frame: {self.frame} imageIndex: {self.imageIndex}\n')
        pass

    def draw(self, surface):
        self.BGbar = pygame.Rect(0,0,94,14)
        if self.id <=6 and self.id >=0:
            self.BGbar.center=(100*self.id+70,100)
        else:
            self.BGbar.center=(100*self.id+850,100)

        pygame.draw.rect(surface, self.bgbarcolor, self.BGbar)
        
        if self.active:
            self.bar = pygame.Rect(0,0,(self.duration / self.durationTime)*90,10)
            self.barcolor = (252, 3, 3)
        else:
            self.bar = pygame.Rect(0,0,(self.cooldown / self.cooldownTime)*90,10)
            self.barcolor = (20, 153, 255)
        self.bar.midleft=(self.BGbar.midleft[0] + 2, self.BGbar.midleft[1])
        pygame.draw.rect(surface, self.barcolor, self.bar)
        
        if self.id <=6 and self.id >=0:
            
            # invis2.draw(surface,100*self.id+70,60)
            #surface.blit(self.images[self.imageIndex],self.images[self.imageIndex].get_rect(center=(100*self.id+70,60)))
            if self.id == 0:
                invis2.draw(surface,100*self.id+20,10)
            if self.id != 0 and self.id <= 6:
                wip.draw(surface,100*self.id+20,10)
        else:
            if self.id != 0 and self.id > 6:
                wip.draw(surface,100*self.id+800,10)
            #invis2.draw(surface,100*self.id+70,60)
            #surface.blit(self.images[self.imageIndex],self.images[self.imageIndex].get_rect(center=(100*self.id+850,60)))

        
        
        