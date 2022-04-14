import pygame
import time
import random
pygame.init()

display_width = 360
display_height = 600
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

floor_width = 90
floor_height = 20

rfloor_width = 90
rfloor_height = 20

person_width = 30
person_height = 30
pole1_width = 20
pole1_height = 600
pole2_width = 20
pole2_height = 600
blade_width = 360
blade_height = 38

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Jump Jump Jump')
clock = pygame.time.Clock()

personImg = pygame.image.load('person.png')#load the image source
personImg = pygame.transform.scale(personImg, (person_width, person_height))

pole1Img = pygame.image.load('pole1.png')#load the image source
pole1Img = pygame.transform.scale(pole1Img, (pole1_width, pole1_height))

pole2Img = pygame.image.load('pole2.png')#load the image source
pole2Img = pygame.transform.scale(pole2Img, (pole2_width, pole2_height))

bladeImg = pygame.image.load('blade.png')#load the image source
bladeImg = pygame.transform.scale(bladeImg, (blade_width, blade_height))

def floor_score(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score:"+ str(count), True, black)
    gameDisplay.blit(text, (10,10))



foo_list = []
for i in range (4):
    floor_startx = random.randrange(0+20, display_width - floor_width - 20)
    floor_starty = random.randrange(-200,800)
    foo_list.append([floor_startx, floor_starty, floor_width, floor_height])

rfoo_list = []
for i in range (2):
    rfloor_startx = random.randrange(0+20, display_width - floor_width - 20)
    rfloor_starty = random.randrange(-200,800)
    rfoo_list.append([rfloor_startx, rfloor_starty, rfloor_width, rfloor_height])

        #floor_starty = display_height + 100
        #floor_speed = -4
        #floor_width = 70
        #floor_height = 20
        #floor_startx = random.randrange(0+20, display_width - floor_width - 20)

#def floors(floorx, floory, floorw, floorh, color):
    #pygame.draw.rect(gameDisplay, color, [floorx, floory, floorw, floorh])

def blood_bar(barx, bary, barw, barh, color):
    pygame.draw.rect(gameDisplay, color, [barx, bary, barw, barh])

def pole1(px,py):
    gameDisplay.blit(pole1Img,(px,py))

def pole2(ppx,ppy):
    gameDisplay.blit(pole2Img,(ppx,ppy))

def blade(bx,by):
    gameDisplay.blit(bladeImg,(bx,by))

def person(x,y):  #creat function-put the person in the display window
    gameDisplay.blit(personImg,(x,y))

def text_objects(text, font):  #create function of an text surface/info setting of the surface
    textSurface = font.render(text, True, black) #creat var for the text surface, inside the rendered surface, we need to define the text and color
    return textSurface, textSurface.get_rect() #since the function have two represet var(text,font), we need to return two info for this two var in order to give it a value

def message_display(text): #create function in order to display it
    largeText = pygame.font.Font('CutPixel.TTF',30)
    TextSurf, TextRect = text_objects(text, largeText) #create var for the text_object()function and give a value for the "font" in the text_object()function
    TextRect.center = ((display_width/2),(display_height/2 - 20)) #local the textSurface
    gameDisplay.blit(TextSurf, TextRect) #run the display
    pygame.display.update() #keep update/run the display in the animation(text loop)

    time.sleep(2) #run the display for 2 second

    game_loop() #turn back to the game/draw back to gameloop

def die():
    gameDisplay.fill(red)
    message_display('You died')




def game_loop():
    bx = 0
    by = 0
    px = 0
    py = 0
    ppx = 340
    ppy = 0

    x = (display_width * 0.45)
    y = (display_height * 0.1)

    x_change = 0
    y_change = 5

    #floor_starty = display_height + 100
    floor_speed = -4
    rfloor_speed = -4
    #floor_width = 70
    #floor_height = 20
    #floor_startx = random.randrange(0+20, display_width - floor_width - 20)

    #platsx, platsy, platsw, platsh


    bar_x = 50
    bar_y = 580
    bar_width = 260
    bar_height = 10

    marks = 0

    gameExit = False

    while not gameExit:  #crashed still equal false/when it is not crash

        for event in pygame.event.get(): #looping/keep update ur info time by time
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        person(x,y)

        if y  > display_height:
            die()

        if x  > display_width - person_width-20:
            x = display_width - person_width-20

        if x < 0+20:
            x = 20

        #things(thingx, thingy, thingw, thingh, color)
        #floors(floor_startx, floor_starty, floor_width, floor_height, black)

        for item in foo_list:
            item[1] += floor_speed
            pygame.draw.rect(gameDisplay, black, item)


            if item[1] < 0:
                item[1] = random.randrange(display_height, display_height + 600)
                item[0] = random.randrange(0 + 20, display_width -20 - floor_width)

            if y + person_height >= item[1] - 10 and y + person_height <= item[1] - 1:
                if x > item[0] and x < item[0] + floor_width or x + person_width > item[0] and x + person_width < item[0] + floor_width:
                    marks += 1
                    if y + person_height == item[1]:
                        marks += 0

            if  y + person_height > item[1] and y < item[1]:
                print('touch the floor')

                if x > item[0] and x < item[0] + floor_width or x + person_width > item[0] and x + person_width < item[0] + floor_width:
                    print('touch two floor2')
                    y = item[1] - person_height
                    y +=  floor_speed

        for ritem in rfoo_list:
            ritem[1] += rfloor_speed
            pygame.draw.rect(gameDisplay, red, ritem)


            if ritem[1] < 0:
                ritem[1] = random.randrange(display_height, display_height + 600)
                ritem[0] = random.randrange(0 + 20, display_width -20 - rfloor_width)



            if  y + person_height > ritem[1] and y < ritem[1]:
                print('touch the floor')

                if x > ritem[0] and x < ritem[0] + rfloor_width or x + person_width > ritem[0] and x + person_width < ritem[0] + rfloor_width:
                    print('touch two floor2')
                    y = ritem[1] - person_height
                    y +=  rfloor_speed
                    bar_width += -1
                    if bar_width <=0:
                        bar_width = 0
                        die()




        #if floor_starty < 40:
            #floor_starty = display_height + floor_height
            #floor_startx = random.randrange(0+20, display_width - floor_width - 20)

        #if y + person_height >= floor_starty - 10 and y + person_height < floor_starty - 1:
            #marks += 1

        #if  y + person_height > floor_starty and y < floor_starty:
            #print('touch the floor')

            #if x > floor_startx and x < floor_startx + floor_width or x + person_width > floor_startx and x + person_width < floor_startx + floor_width:
                #print('touch two floor2')
                #y = floor_starty - person_height
                #y +=  floor_speed

        blood_bar(bar_x, bar_y, bar_width, bar_height, red)

        if y < 40:
            bar_width += -1

            if bar_width <=0:
                bar_width = 0
                die()

        blade(bx,by)
        pole1(px,py)
        pole2(ppx,ppy)
        floor_score(marks)

        if marks > 5:
            floor_speed += -0.001
            if marks > 25:
                y_change += 0.001




        pygame.display.update()#tell computer to scan the code consetinly so the display keep appear frame by frame according to the code
        clock.tick(60)# how many flames per second

game_loop()
pygame.quit()
quit()
