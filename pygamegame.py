import sys
import player
import pygame
import powers
import button
from pygame.locals import QUIT

pygame.init()
pygame.font.init()
pygame.display.set_caption('pygame game')
DISPLAYSURF = pygame.display.set_mode((1920,1080))




characterW = 54 *1.3
characterL = 110*1.3
invis = powers.powers(720, 300, 0,["./sprites/Icons/invisicon2.png"])
speed = powers.powers(480, 180, 1,["./sprites/Icons/speedicon2.png"])
hyper = powers.powers(1200, 30, 4,["./sprites/Icons/hypericon.png"])
wall1 = powers.powers(180,0,3,[])
#growAnimation = ["./sprites/Icons/grow/1.png","./sprites/Icons/grow/2.png","./sprites/Icons/grow/3.png","./sprites/Icons/grow/4.png","./sprites/Icons/grow/5.png","./sprites/Icons/grow/6.png","./sprites/Icons/grow/7.png"]
growAnimation = []
# for i in range(7):
#     growAnimation.append(f'./sprites/Icons/grow/{i+1}.png')
    
grow = powers.powers(100,200,10,["./sprites\Icons\growicon.png"])
wall2 = powers.powers(180,0,9,[])
hammer = powers.powers(5,30,8,[])

p1skills = {"invis":invis,"speed":speed,"hyper":hyper,"wall":wall1}
p2skills = {"grow":grow,"wall":wall2,"hammer":hammer}

player1 = player.player(100,100,"./sprites/player.png",(characterW,characterL),5,1, p1skills)

badboyX = 1700
badboyY = 800


player2 = player.player(1700,800,"./sprites/badboy.png",(characterW,characterL),6,2, p2skills)

fonty = pygame.font.Font("./Daydream.ttf",128)
timerFont = pygame.font.Font("./Daydream.ttf",128)
activeFont = pygame.font.Font("./Daydream.ttf",32)
cooldownFont = pygame.font.Font("./Daydream.ttf",32)


clock = pygame.time.Clock()
running = True
fps = 60
frames = 0

menu = True
paused = False



seconds = 1 * 60




startbutton = button.button("./sprites/buttons/start/startbutton1.png","./sprites/buttons/start/startbutton2.png",(220,100),(1920/2,1080/2-100))

exitbutton = button.button("./sprites/buttons/exit/exitbutton1.png","./sprites/buttons/exit/exitbutton2.png",(50,50),(1920-50,50))

leavebutton = button.button("./sprites/buttons/leave/leave1.png","./sprites/buttons/leave/leave2.png",(220,100),(1920/2,1080/2+20))


def reset():
    global seconds
    seconds = 1 * 60
    player1.x = 100
    player1.y = 100
    player2.x = 1700
    player2.y = 800
    player1.skillreset()
    player2.skillreset()

while True:
    while menu: 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            player1.keyPresses(event)
            player2.keyPresses(event)
            if event.type == pygame.MOUSEBUTTONDOWN and startbutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
                menu = False
                running = True
            if event.type == pygame.MOUSEBUTTONDOWN and leavebutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN and exitbuttonrect.collidepoint(pygame.mouse.get_pos()):
            #     pygame.quit()
            #     sys.exit()
                
            # #______________________________________key dection
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         pygame.quit()
            #         sys.exit()
        
        
        DISPLAYSURF.fill((243, 239, 245))
        if startbutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
            startbutton.draw(DISPLAYSURF,True)
        else:
            startbutton.draw(DISPLAYSURF,False)        
            # if exitbuttonrect.collidepoint(pygame.mouse.get_pos()):
        #     DISPLAYSURF.blit(exitbutton2,exitbuttonrect)
        # else:
        #     DISPLAYSURF.blit(exitbutton1,exitbuttonrect)
        if leavebutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
            leavebutton.draw(DISPLAYSURF,True)
        else:
            leavebutton.draw(DISPLAYSURF,False)


        
        pygame.display.update()
    menu = True
    while running:
        clock.tick(fps)
        frames += 1
        if frames % 60 == 0:
            seconds -= 1
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            player1.keyPresses(event)
            player2.keyPresses(event)
            #______________________________________key dection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
        
        
        player1.start2()
        player1.movement()
        player1.boundaries()
        player1.hitbox()
        player1.skills()
        player1.box()
        
        
        player2.start2()
        player2.movement()
        player2.boundaries()
        player2.hitbox()
        player2.skills()
        player2.box()
        

        DISPLAYSURF.fill((243, 239, 245))
        timer = timerFont.render(f"{seconds}",False,(191, 191, 255))
        timerRect = timer.get_rect(center = (1920/2,1080/2))
        DISPLAYSURF.blit(timer,timerRect)
        
        player1.draw(DISPLAYSURF)
        player2.draw(DISPLAYSURF)

        #pygame.draw.rect(DISPLAYSURF,(213,34,196),playerRect)
        #pygame.draw.rect(DISPLAYSURF,(123,255,255),badboyRect)

        ### ADD TO SKILL CLASS
        
        # if not invis:
            
        #     cooldownInvis -= 1
        # else:
        #     Invisduration += 1
            
        #     if Invisduration >= 300:
                
        #         invis = False
        #         Invisduration = 0
        #         cooldownInvis = 720

        
        # if not speedAbilty:
        #     speed = 5
        #     cooldownSpeed -= 1
        # else:
        #     Speedduration += 1
        #     speed = 10
        #     if Speedduration >= 600:
                
        #         speedAbilty = False
        #         Speedduration = 0
        #         cooldownSpeed = 720
            

        #DISPLAYSURF.blit(badboy,(badboyX,badboyY))
        # active = activeFont.render(str(p1skills["invis"].active),False,(0,0,0))
        # activeRect = active.get_rect(center = (1920/2,1080/2))
        # DISPLAYSURF.blit(active,activeRect)

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                if event.type == pygame.MOUSEBUTTONDOWN and exitbutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                if event.type == pygame.MOUSEBUTTONDOWN and leavebutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                    
            alpha = 120
            menusurf = pygame.Surface(pygame.display.get_surface().get_size())
            menusurf.fill((0,0,0))
            menusurf.set_alpha(200)
            DISPLAYSURF.fill((243, 239, 245))
            player1.draw(DISPLAYSURF)
            player2.draw(DISPLAYSURF)
            DISPLAYSURF.blit(menusurf,(0,0))
            if exitbutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
                exitbutton.draw(DISPLAYSURF,True)
            else:
                exitbutton.draw(DISPLAYSURF,False)
            if leavebutton.buttonrect.collidepoint(pygame.mouse.get_pos()):
                leavebutton.draw(DISPLAYSURF,True)
            else:
                leavebutton.draw(DISPLAYSURF,False)
            pygame.display.update()


        


        
        if seconds == 0:
            p1win = fonty.render("Player  1  wins!",False,(0,0,0))
            p1winRect = p1win.get_rect(center = (1920/2,1080/2))
            DISPLAYSURF.blit(p1win,p1winRect)
            running = False
            reset()

        if player1.rect.colliderect(player2.rect):
            p2win = fonty.render("Player  2  wins!",False,(0,0,0))
            p2winRect = p2win.get_rect(center = (1920/2,1080/2))
            DISPLAYSURF.blit(p2win,p2winRect)
            running = False
            reset()

        pygame.display.update()
    temp = 0
    while True:
        clock.tick(fps)
        temp += 1
        if temp >= 180:
            break
        
        
        
        
    
    

    
# asd = 1
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 pygame.quit()
#                 sys.exit() 