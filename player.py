import pygame
import powers
import spritesheet
import wall


hyperimage = pygame.image.load("./sprites/Icons/hypericon.png")
hyperimage = pygame.transform.scale(hyperimage,(100,100))
hyperrect = hyperimage.get_rect()

hammer = pygame.image.load("./sprites/hammer.png")
hammer = pygame.transform.scale(hammer,(42,42))
hammerrect = hammer.get_rect()


walls = []
class player():

    def __init__(self, x, y, imagePath, scale,speed,id,skills):
        self.x = x
        self.y = y
        self.speed = speed
        self.scale = scale
        self.id = id
        self.originalImage = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.originalImage,scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x+self.rect.width/2,self.y+self.rect.height/2)
        #self.rect = self.rect.inflate(-197,-145)
        self.pressedKeys = {"up":False,"down":False,"left":False,"right":False}
        self.skillsDict = skills
        self.start = False
        self.numofwalls = 0
        self.uhhh = False
        
        
        self.direction = "left"
    def start2(self):
        if self.start == False:
            self.start = True
            for s in self.skillsDict:
                    self.skillsDict[s].startup()
            
        

    def movement(self):
        
        if "hyper" in self.skillsDict.keys():
            if not self.skillsDict["hyper"].active:
                if self.pressedKeys ["up"]:
                    self.direction = "up"
                    self.y -= self.speed
                if self.pressedKeys ["down"]:
                    self.direction = "down"
                    self.y += self.speed
                if self.pressedKeys ["right"]:
                    self.direction = "right"
                    self.x += self.speed
                if self.pressedKeys ["left"]:
                    self.direction = "left"
                    self.x -= self.speed
                if self.pressedKeys ["up"] and self.pressedKeys ["left"]:
                    self.direction = "upleft"
                if self.pressedKeys ["up"] and self.pressedKeys ["right"]:
                    self.direction = "upright"
                if self.pressedKeys ["down"] and self.pressedKeys ["left"]:
                    self.direction = "downleft"
                if self.pressedKeys ["down"] and self.pressedKeys ["right"]:
                    self.direction = "downright"
                
                
        else:
            if self.pressedKeys ["up"]:
                self.direction = "up"
                self.y -= self.speed
            if self.pressedKeys ["down"]:
                self.direction = "down"
                self.y += self.speed
            if self.pressedKeys ["right"]:
                self.direction = "right"
                self.x += self.speed
            if self.pressedKeys ["left"]:
                self.direction = "left"
                self.x -= self.speed
            if self.pressedKeys ["up"] and self.pressedKeys ["left"]:
                self.direction = "upleft"
            if self.pressedKeys ["up"] and self.pressedKeys ["right"]:
                self.direction = "upright"
            if self.pressedKeys ["down"] and self.pressedKeys ["left"]:
                self.direction = "downleft"
            if self.pressedKeys ["down"] and self.pressedKeys ["right"]:
                self.direction = "downright"
        if self.id == 1:
            if self.direction == "up":
                self.originalImage = pygame.image.load("./sprites/player/playerup.png")
            elif self.direction == "left":
                self.originalImage = pygame.image.load("./sprites/player/playerleft.png")
            elif self.direction == "down":
                self.originalImage = pygame.image.load("./sprites/player/playerdown.png")
            elif self.direction == "right":
                self.originalImage = pygame.image.load("./sprites/player/playerright.png")
            if self.direction == "upleft":
                self.originalImage = pygame.image.load("./sprites/player/playerupleft.png")
            if self.direction == "upright":
                self.originalImage = pygame.image.load("./sprites/player/playerupright.png")
            if self.direction == "downleft":
                self.originalImage = pygame.image.load("./sprites/player/playerdownleft.png")
            if self.direction == "downright":
                self.originalImage = pygame.image.load("./sprites/player/playerdownright.png")
        if self.id == 2:
            if self.direction == "up":
                self.originalImage = pygame.image.load("./sprites/player2/badboyup.png")
            elif self.direction == "left":
                self.originalImage = pygame.image.load("./sprites/player2/badboyleft.png")
            elif self.direction == "down":
                self.originalImage = pygame.image.load("./sprites/player2/badboydown.png")
            elif self.direction == "right":
                self.originalImage = pygame.image.load("./sprites/player2/badboyright.png")
            if self.direction == "upleft":
                self.originalImage = pygame.image.load("./sprites/player/playerupleft.png")
            if self.direction == "upright":
                self.originalImage = pygame.image.load("./sprites/player/playerupright.png")
            if self.direction == "downleft":
                self.originalImage = pygame.image.load("./sprites/player/playerdownleft.png")
            if self.direction == "downright":
                self.originalImage = pygame.image.load("./sprites/player/playerdownright.png")


    def keyPresses(self,event):
        if self.id == 1:
            #print("1")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and self.skillsDict["invis"].cooldown == self.skillsDict["invis"].cooldownTime:
                    self.skillsDict["invis"].active = True
                if event.key == pygame.K_2 and self.skillsDict["speed"].cooldown == self.skillsDict["speed"].cooldownTime:
                    self.skillsDict["speed"].active = True
                if event.key == pygame.K_5 and self.skillsDict["hyper"].cooldown == self.skillsDict["hyper"].cooldownTime:
                    self.skillsDict["hyper"].active = True
                if event.key == pygame.K_4 and self.skillsDict["wall"].cooldown == self.skillsDict["wall"].cooldownTime:
                    self.skillsDict["wall"].active = True
                if self.direction == "upleft":
                    self.originalImage = pygame.image.load("./sprites/player/playerupleft.png")
                if self.direction == "upright":
                    self.originalImage = pygame.image.load("./sprites/player/playerupright.png")
                if self.direction == "downleft":
                    self.originalImage = pygame.image.load("./sprites/player/playerdownleft.png")
                if self.direction == "downright":
                    self.originalImage = pygame.image.load("./sprites/player/playerdownright.png")
                    
                if event.key == pygame.K_w:
                    self.pressedKeys ["up"] = True
                if event.key == pygame.K_s:
                    self.pressedKeys ["down"] = True
                if event.key == pygame.K_d:
                    self.pressedKeys ["right"] = True
                if event.key == pygame.K_a:
                    self.pressedKeys ["left"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.pressedKeys ["up"] = False
                if event.key == pygame.K_s:
                    self.pressedKeys ["down"] = False
                if event.key == pygame.K_d:
                    self.pressedKeys ["right"] = False
                if event.key == pygame.K_a:
                    self.pressedKeys ["left"] = False
        if self.id == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 and self.skillsDict["grow"].cooldown == self.skillsDict["grow"].cooldownTime:
                    self.skillsDict["grow"].active = True
                if event.key == pygame.K_9 and self.skillsDict["wall"].cooldown == self.skillsDict["wall"].cooldownTime:
                    self.skillsDict["wall"].active = True
                if event.key == pygame.K_8 and self.skillsDict["hammer"].cooldown == self.skillsDict["hammer"].cooldownTime:
                    self.skillsDict["hammer"].active = True
                    powers.hammer.unpack(66,54)
                    self.uhhh = True
                if event.key == pygame.K_UP:
                    self.pressedKeys ["up"] = True
                if event.key == pygame.K_DOWN:
                    self.pressedKeys ["down"] = True
                if event.key == pygame.K_RIGHT:
                    self.pressedKeys ["right"] = True
                if event.key == pygame.K_LEFT:
                    self.pressedKeys ["left"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.pressedKeys ["up"] = False
                if event.key == pygame.K_DOWN:
                    self.pressedKeys ["down"] = False
                if event.key == pygame.K_RIGHT:
                    self.pressedKeys ["right"] = False
                if event.key == pygame.K_LEFT:
                    self.pressedKeys ["left"] = False

    def boundaries(self):
        if self.x < -self.scale[0] + 2:
            self.x = 1918
        if self.x > 1918:
            self.x = -self.scale[0] + 2
        if self.y < -self.scale[1] + 2:
            self.y = 1078
        if self.y > 1078:
            self.y = -self.scale[1] + 2

    def draw(self, surface):
        print(f'len of walls list: {len(walls)}')
        print(f'{self.id} : {self.numofwalls}')
        for i in walls:
            i.draw(surface)
        # hitbox
        #pygame.draw.rect(surface,(213,34,196),self.rect)
        if "invis" in self.skillsDict.keys():
            if not self.skillsDict["invis"].active:
                surface.blit(self.image,(self.x,self.y))
            if "hyper" in self.skillsDict.keys():
                if self.skillsDict["hyper"].active:
                    hyperrect.center =(self.x+35,self.y-10)
                    surface.blit(hyperimage,hyperrect)
        else:
            surface.blit(self.image,(self.x,self.y))
        if "hammer" in self.skillsDict.keys():
            if self.skillsDict["hammer"].active:
                if self.direction == "up":
                    powers.hammer.draw(surface,self.x+2,self.y-57)
                    hammerrect.center = (self.x+35,self.y-30)
                elif self.direction == "down":
                    powers.hammer.draw(surface,self.x+2,self.y+146)
                    hammerrect.center = (self.x+35,self.y+173)
                elif self.direction == "left":
                    powers.hammer.draw(surface,self.x-63,self.y+45)
                    hammerrect.center = (self.x-30,self.y+72)
                else:
                    powers.hammer.draw(surface,self.x+73,self.y+45)
                    hammerrect.center = (self.x+100,self.y+72)
                for i in walls:
                    if hammerrect.colliderect(i.rect) and self.uhhh == True:
                        i.hp -= 1
                        self.uhhh = False
                        
                
                
            
            
        for s in self.skillsDict:
            self.skillsDict[s].draw(surface)
        
        #print(self.rect)

    def hitbox(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x+self.rect.width/2,self.y+self.rect.height/2)
    def skillreset(self):
        for s in self.skillsDict:
            self.skillsDict[s].reset()
        walls.clear()
        self.numofwalls = 0

    def skills(self):
        #for the grow function to change the side
        self.image = pygame.transform.scale(self.originalImage,self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x+self.rect.width/2,self.y+self.rect.height/2)
        #self.rect = self.rect.inflate(-197,-145)
        
        for i in walls:
            if i.hp == 0 and i.id == self.id:
                walls.remove(i)
                self.numofwalls -= 1
                print(self.numofwalls)
                
        
                    
        if "hammer" in self.skillsDict.keys():
            if self.skillsDict["hammer"].active == False:
                self.uhhh = False
            

        

        if "speed" in self.skillsDict.keys():
            if self.skillsDict["speed"].active:
                self.speed = 10
            else:
                self.speed = 5
        
        if "hyper" in self.skillsDict.keys():
            if self.skillsDict["hyper"].active:
                for s in self.skillsDict:
                    if self.skillsDict[s].id != 5:
                        self.skillsDict[s].reset()

        if "grow" in self.skillsDict.keys():
            if self.skillsDict["grow"].active:
                self.scale = (54 * 1.7,110 * 1.7)
                self.rect = self.rect.inflate(-197,-145)
            else:
                self.scale = (54 * 1.3, 110 * 1.3)
        if "wall" in self.skillsDict.keys():
            
            if self.skillsDict["wall"].active:
                walls.append(wall.wall(self.x,self.y,self.direction,self.id))
                self.numofwalls += 1
        
            
                
    
        
        for s in self.skillsDict:
            self.skillsDict[s].activated()
            self.skillsDict[s].coolingDown()
            self.skillsDict[s].finish()
            self.skillsDict[s].update()
    def box(self):
        for i in walls:
            if self.rect.colliderect(i.rect):
                #print("collisiopn")
                
                if i.id != self.id:
                    if self.direction == "left":
                        self.x += self.speed
                    if self.direction == "right":
                        self.x -= self.speed
                    if self.direction == "up":
                        self.y += self.speed
                    if self.direction == "down":
                        self.y -= self.speed
                    if self.direction == "upleft":
                        self.y += self.speed
                        self.x += self.speed
                    if self.direction == "upright":
                        self.y += self.speed
                        self.x -= self.speed
                    if self.direction == "downleft":
                        self.y -= self.speed
                        self.x += self.speed
                    if self.direction == "downright":
                        self.y -= self.speed
                        self.x -= self.speed
        
        if self.numofwalls == 5:
            for i in walls:
                if i.id == self.id:
                    walls.remove(i) 
                    self.numofwalls -= 1
                    
                    break
                
                


            
            
           
