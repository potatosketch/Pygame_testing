import pygame
import time
import random

####################
#<global variable define session>#

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
lightred = (255,102,102)
lightblue = (102, 153, 255)
lightyellow = (240, 230, 104)

#pygame display window width and height
display_width = 360  
display_height = 600  

#first page backgound width and height(the night galaxy picture)
BGimg_width = 960 
BGimg_height = 600

#second page world map width and height(the land and sea picture)
ww = 1440
wh = 960

#width and height of blade element in the let_jump() page 
blade_width = 360
blade_height = 38

#width and height of those 2 green and orange pole in the let_jump() page 
pole_width = 20
pole_height = 600

#width and height of the pikachu image in the gameover() page
s_width = 1055
s_height = 600

mwb = 50
mhb = 50

#global var pause use for menu page and unpause function
pause = False

#width and height of the floor of thr let_jump() page
floor_width = 90
floor_height = 20

#width and height of the red floor of thr let_jump() page
rfloor_width = 90
rfloor_height = 20







####################
#<pygame setting session>#
pygame.init()  #run the pygame library
gameDisplay = pygame.display.set_mode((display_width,display_height)) #run the window
pygame.display.set_caption('Let Explore!')  #set the window title
clock = pygame.time.Clock() #import time with pygame

iconimg = pygame.image.load("logo.png")  #load icon image
pygame.display.set_icon(iconimg)  #set the icon image as the pygame window icon

####################
#***What is build-in function?***#
#Create a custom function that can recall in a loop. Since property and value in a function is different, even the same function can execute in different property which defined by programmer,
#Therefore, recall a build-in function means you can call up many "same-type" of function but run in different properties.

#create build-in function: music loading and playing
def bgm1(event):  #define music playing function(with the defined name "bgm1")
    mapbgmusic = pygame.mixer.music.load("mapmusic.mp3")  #load the music from the same directory file
    pygame.mixer.music.play()  #build-in pygame library function of playing the music you have loaded

def bgm2(event):
    mapbgmusic = pygame.mixer.music.load("floorintrobgm.mp3")
    pygame.mixer.music.play()

def bgm3(event):
    mapbgmusic = pygame.mixer.music.load("letjump.mp3")
    pygame.mixer.music.play()

def bgm4(event):
    mapbgmusic = pygame.mixer.music.load("youdie.mp3")
    pygame.mixer.music.play()

def bgm5(event):
    mapbgmusic = pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play()

##########    
#create build-in function: stop and unstop music playing
def musicpause():  #define stop music playing function(with the defined name "musicpause")
    pygame.mixer.music.pause()  #build-in pygame library function of stop the music

def musicunpause():  #define unstop music playing function
    pygame.mixer.music.unpause()  #build-in pygame library function of unstop the music

####################   
#sound load in by build-in pygame library function
buttonsound1 = pygame.mixer.Sound('k.wav')
buttonsound2 = pygame.mixer.Sound('m.wav')
buttonsound3 = pygame.mixer.Sound('p.wav')
buttonsound4 = pygame.mixer.Sound('t.wav')
buttonsound5 = pygame.mixer.Sound('l.wav')
buttonsound6 = pygame.mixer.Sound('d.wav')
buttonsound6.set_volume(1.0) #set the volume of buttonsound6("d.wav") to loudest (0 is silent and 1 is loudest)

####################
#image loading session
BGImg = pygame.image.load('intro_bg.jpg')  #load the image source for the backgound(the night galaxy) of the first page /global variable define for the loaded image 
BGImg = pygame.transform.scale(BGImg, (BGimg_width, BGimg_height))  #transform the the size of the image to new width and height

worldimg = pygame.image.load("worldmap.png") #load the image source for the backgound(the night galaxy) of the first page /global variable define for the loaded image
worldimg =  pygame.transform.scale(worldimg, (ww, wh))

bladeImg = pygame.image.load('blade.png')  #load the image source of the blade in the let_jump() loop page /global variable define for the loaded image
bladeImg = pygame.transform.scale(bladeImg, (blade_width, blade_height))

pole1Img = pygame.image.load('pole1.png')  #load the image source of the pole in the let_jump() loop page (green and orange pole) /global variable define for the loaded image
pole1Img = pygame.transform.scale(pole1Img, (pole_width, pole_height))

pole2Img = pygame.image.load('pole2.png')  #load the image source of the pole in the let_jump() loop page (green and orange pole) /global variable define for the loaded image
pole2Img = pygame.transform.scale(pole2Img, (pole_width, pole_height))

jumpImg = pygame.image.load('jumpbg.png') #load the background image source for the let_jump() loop page (the blue sky with cloud) /global variable define for the loaded image
jumpImg = pygame.transform.scale(jumpImg, (display_width, display_height))  #size is same as the pygame display window

gameoverImg = pygame.image.load('gameoverbg.gif') #load the background image source for the gameover() loop page (the crying pikachu) /global variable define for the loaded image
gameoverImg = pygame.transform.scale(gameoverImg, (s_width, s_height))

#create image display build-in function
def BGIMG(bgx,bgy):  #define build-in function
    gameDisplay.blit(BGImg,(bgx,bgy))   #bilt the image so it can keep update into new slice(keep looping and updating-create turning machine)/ insert coordination x and y by named it bgx and bgy

def world(wx,wy):
    gameDisplay.blit(worldimg,(wx,wy))

def menubutton(mx,my,mw,mh):  #define build-in function
    menubu1 = pygame.image.load("menu.png").convert_alpha()  #load-in the image of a menu icon 
    menubu1 =  pygame.transform.scale(menubu1, (mw, mh))  #transform the image size to new width and height(mw,mh)
    gameDisplay.blit(menubu1,(mx,my)) #bilt the image/ insert coordination x and y by named it mx and my

def blade(bx,by):
    gameDisplay.blit(bladeImg,(bx,by))

def pole1(px,py):  
    gameDisplay.blit(pole1Img,(px,py)) 

def pole2(ppx,ppy):
    gameDisplay.blit(pole2Img,(ppx,ppy))

def jumpbg(jbgx,jbgy):
    gameDisplay.blit(jumpImg,(jbgx,jbgy))

def pikachi(sx,sy):
    gameDisplay.blit(gameoverImg,(sx,sy))    

####################
#create text-box display build-in function
def text_objects(text, font):  #define text-box load-in build-in function
    textSurface = font.render(text, True, black)  #render the text-box and named this acion as textSurface, and define the color of the font in this text-box
    return textSurface, textSurface.get_rect()  #get_rect() means get all 2 of the datas textSurface have rendered out and return it to the function variable (text and font)

#create button build-in function
def button(msg, bx, by, bw, bh, bic, bac, action=None):  #define button build-in function
    mouse = pygame.mouse.get_pos()  #pygame library function: get the position of your mouse in the display window (2 datas array = [x, y])
    click = pygame.mouse.get_pressed()  #pygame library function: when mouse is unpress = 0, when mouse is press = 1 (1 data array = [0 or 1])
    #print(click) #to test are the datas being executed and run at click

    #mouse[0] = mouse pointer x coordinate/ mouse[1] = mouse pointer y coordinate
    #if mouse pointer is in the rectangle button, run some actions, or else just only display the rectangle button without action
    if bx + bw > mouse[0] >  bx and by + bh > mouse[1] > by:  #define the constrain of the rectangle with the four x and y location points of the rectangle and interact with the mouse coordination
        pygame.draw.rect(gameDisplay, bac, [bx, by, bw, bh])  #draw rectangle to represent the button

        if click[0] == 1 and action != None:  #if array 0 is equal 1, means the click is running and run the following action
            buttonsound1.play() #play the buttonsound1 (k.wav)
            action()  #action set as "None" originally, here action() = 1, which meaning there is action to executed 

    else:
        pygame.draw.rect(gameDisplay, bic, [bx, by, bw, bh])

    #load-in text on the button to indicate different button function
    largeText = pygame.font.Font('CutPixel.TTF',10)  #give the text property: font type & font size
    TextSurf, TextRect = text_objects(msg, largeText)  #load-in text into the text-box build-in function I defined before
    TextRect.center = ((bx + bw/2),(by + bh/2))  #location of the text/ .center means the text x, y is not base on top-left corner but x, y on the center of the text-box
    gameDisplay.blit(TextSurf, TextRect)  #bilt the text content, keep update into new slice(keep looping and updating-create turning machine)

####################
#***What is class function?***#
#class function can create a object which is defined by you, in the class function, programmer needs to define what element contain inside a class in order to make a class and an object.
#Once the class elements are well defined, we can draw an object with same property or even function with just only one line, the properties can be change with just type in data but not recall many other line to make it very clumpy coding style
#Therefore, use this class can build up object as many time as you want and represent different object with sam function but different properties and without repeat long clumpy codeline again and again.

#-<character movement>-#    
#using class function
class spritesheet:
    def __init__(self,filename,cols,rows,imgwidth, imgheight):
        self.sheet = pygame.image.load(filename).convert_alpha()  #class properties contain defined: load spritesheet picture
        self.sheet =  pygame.transform.scale(self.sheet, (imgwidth, imgheight))  #class properties contain defined: transform image size by imgwidth, imgheight

        self.cols = cols  #class properties contain defined: how many columes in one spritesheet
        self.rows = rows  #class properties contain defined: how many rows in one spritesheet
        self.totalCellCount = cols*rows  #class properties contain defined: how many movement images in one spritesheet by cols times rows

        self.rect = self.sheet.get_rect()  #get data from the loaded spritesheet picture
        w = self.cellWidth = int(self.rect.width / cols)  #spritesheet's width divide with the number of columes and get the width of each small movement image within the spritesheet
        h = self.cellHeight = int(self.rect.height / rows)  #spritesheet's height divide with the number of rows and get the height of each small movement image within the spritesheet
        hw,hh = self.CellCenter = (int(w/2),int(h/2))  #define the center location of each spritesheet image

        #making an array so it can recall muiltiple time
        #columes times width of each sub-image = each sub-image's x location, rows times height of each sub-image = each sub-image's y location),width of subimage, height of sub-image>>>>>using all this four data to create for-loop and loop happen when it run all sub-images(totalcellcount)
        self.cells = list([(int(index % cols)*w, int(index/cols)*h ,w ,h)for index in range(self.totalCellCount)]) 
    
    def ani(self,surface,cellIndex,x,y):  #define a working spritesheet build-in function
        surface.blit(self.sheet,(x , y ),self.cells[cellIndex]) #bilt the spritesheet that have loaded in/ bilt is in a loop way (cellindex)=show image at the same time bilt it sub-image by looping


s = spritesheet("tom.png",4,4,120,180)  #load image first(load image property:filename), then call up class properties contain defined function(call up the 4 properties:cols, rows, imgwidth, imgheight)

####################
#create score counting build-in function
def floor_score(count):
    font = pygame.font.SysFont(None, 40)  #properties of the font: font type and font size
    text = font.render("Score:"+ str(count), True, black)  #how the score is represented >> e.g. score:10 / also render the text-box and define font as black color
    gameDisplay.blit(text, (10,10))  #bilt the text content, keep update into new slice(keep looping and updating-create turning machine)

#create array list for the black and red floor in the let_jump() page
foo_list = []
for i in range (4):  #range (4) means there is four elements in an array which means four black floor will generated
    floor_startx = random.randrange(0+20, display_width - floor_width - 20)  #floor x location generated constrain
    floor_starty = random.randrange(-200,800)  #floor y location generated constrain
    foo_list.append([floor_startx, floor_starty, floor_width, floor_height])  #appeal the property into every elements in the list

rfoo_list = []
for i in range (2):
    rfloor_startx = random.randrange(0+20, display_width - floor_width - 20)
    rfloor_starty = random.randrange(-200,800)
    rfoo_list.append([rfloor_startx, rfloor_starty, rfloor_width, rfloor_height])

#create blood bar build-in function
def blood_bar(barx, bary, barw, barh, color):
    pygame.draw.rect(gameDisplay, color, [barx, bary, barw, barh]) #draw a red long rectangle to represented as a blood bar


####################
def message_display(text): #define build-in function>> give property to the text and text-box
    largeText = pygame.font.Font('CutPixel.TTF',30)   #give the text property: font type & font size
    TextSurf, TextRect = text_objects(text, largeText)  #load-in text into the text-box build-in function I defined before
    TextRect.center = ((display_width/2),(display_height/2 - 20)) #location of the text/ .center means the text x, y is not base on top-left corner but x, y on the center of the text-box
    gameDisplay.blit(TextSurf, TextRect)  #bilt the text content, keep update into new slice(keep looping and updating-create turning machine)
    pygame.display.update()  #keep update/run the display in the animation(text loop)

    time.sleep(2)  #run the display for 2 second


def die():  #define build-in function: display you died
    #gameDisplay.fill(red)  
    message_display('You died')  #call up the build-in function I have define (message_text() function)


####################
#-<gameloop page: the world map page: character walking around page>-#
def game_loop():
    global pause #one global variable is defined in this page/for the opening the menu function:when menu is open, this page is pause running, not stop and closed. It make sure when menu is closed, the game remind it running but not restart to run the page again.

    bgm1(-1)  #call up music playing build-in function I have defined before and play the music(mapmusic.map3)
    #pygame.mixer.music.play(-1)

    #main character(red shirt kid) fixed location
    x=180  
    y=300

    #character x, y move and change
    x_change=0
    y_change=0

    index = 0  #fixed index of the spritesheet(current running sub-image in a spritesheet)
    index_change=0  #running sub-image: change subimage in a spritesheet
    bb = 0  #change subimage in a spritesheet
    mm = 0  #index looping starting point- change subimage in a spritesheet

    #worldmap fixed location 
    wx = 0
    wy = 0
    #worldmap x, y move and change
    wx_change = 0
    wy_change = 0
 
    #menu icon image fixed location
    mx = 20
    my = 20
    #menu icon image's width & height
    mw =40
    mh=40
    
    #get into floor_intro page location: red rectangle: fixed x & y location
    locax = 310
    locay = 560
    #get into floor_intro page location: width and height of the red rectangle
    locaw = 60
    locah = 120
    
    #create while loop: page created>>> loop forever
    gameExit = False
    while not gameExit: #when the game is not closed:

        for event in pygame.event.get():  #the for-loop will get the data from the window page
            if event.type == pygame.QUIT:  #if the event get the quit signal, pygame will quit by pygame.quit()
                pygame.quit()  #closed window
                quit()  #closed script

            print(event)
            
            #if keyboard key pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  #left key press down in keyboard, it will do the following:
                    x_change = -8  #x_change move to left, because x is decreasing
                    index_change = 1  #index start run, spritesheet for-loop begin
                    mm = 8 #sub-image in spritesheet run at the index 8 picture  (red shirt kid walking and facing left movement)


                elif event.key == pygame.K_RIGHT:  #right key press down in keyboard, it will do the following:
                    x_change = 8  #x_change move to right, because x is increasing
                    index_change = 1  #index start run, spritesheet for-loop begin
                    mm = 12 #sub-image in spritesheet run at the index 12 picture (red shirt kid walking and facing right movement)

                elif event.key == pygame.K_UP:
                    y_change = -8
                    index_change = 1
                    mm = 4


                elif event.key == pygame.K_DOWN:
                    y_change = 8
                    index_change = 1
                    mm = 0

            if event.type == pygame.KEYUP:  #keyup = no kep is being pressed, it will do the following:
                if event.key == pygame.K_LEFT:
                    x_change = 0  #no movement left or right, because no x increasing or decreasing
                    index_change = 0  #spritesheet for-loop stop looping, 0 = no signal
                    bb=0  #no index increasing, therefore, red-shirt kid is a still image
                    mm=0  #sub-image stay at index1 , red shirt kid facing front 
                elif event.key == pygame.K_RIGHT:
                    x_change = 0
                    index_change = 0
                    bb=0
                    mm=0
                elif event.key == pygame.K_UP:
                    y_change = 0
                    index_change = 0
                    bb=0
                    mm=0
                elif event.key == pygame.K_DOWN:
                    y_change = 0
                    index_change = 0
                    bb=0
                    mm=0


        #x location is change since the x data is add up the data from x_change, same as y location
        x += x_change
        y += y_change

        #bb change to keep increasing number as index_change is 1, and bb will be 0,1,2,3,4,5,6......increase forever
        bb += index_change
        #bb loop is certain number e.g.= 0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3.......loop forever
        #bb add with mm(the sub-image loop starting point)>>>>e.g. mm=8 then, bb+mm will be 0+8, 1+8, 2+8, 3+8, final index outcome = 8,9,10,11,8,9,10,11,8,9,10,11.......loopforever
        index = bb %4 + mm  #index loop means spritesheet's sub-image is also looping and create movement
        
        #fill in loop page background with color
        gameDisplay.fill(white)

        #draw a rectangle which located behind the worldmap, so player wont see the rect. however this red rect is a indicated location where player cross it, player will get into floor_intro() page loop
        pygame.draw.rect(gameDisplay, red, (locax,locay,locaw,locah))

        #call in load image build-in function that I defined before
        world(wx,wy)
        #load in the class function spritesheet character and run the character 
        s.ani(gameDisplay,index  % s.totalCellCount,x, y)  #index is increasing, red-shirt kid will have movement 


        #if the red-shirt kid walk to 1/3 of the display window, red-shirt kid's body will still move and worldmap will also move, but the x or y of red-shirt kid won't change 
        if x > display_width/4*3:
            x = display_width/4*3
            wx_change = -8

        if x_change == 0:
            wx_change = 0

        if x >= display_width/4*3 and wx+ww < 361:
            wx_change = 0
            x = display_width/4*3

        if x < display_width/4:
            x = display_width/4
            wx_change = 8
        if bb == 0:
            wx_change = 0

        if x <= display_width/4 and wx > -1:
            wx_change = 0
            x = display_width/4


        if y > display_height/4*3:
            y = display_height/4*3
            wy_change = -8
        if bb == 0:
            wy_change = 0

        if y >= display_height/4*3 and wy+wh < 601:
            wy_change = 0
            y = display_height/4*3

        if y < display_height/4:
            y = display_height/4
            wy_change = 8
        if bb == 0:
            wy_change = 0

        if y <= display_height/4 and wy > -1:
            wy_change = 0
            y = display_height/4


        #if player cross it, player will get into floor_intro() page loop
        if x + 30 > locax and x < locax + locaw and y + 45 > locay and y < locay + locah:
            buttonsound2.play()  #button sound will be played/call-up the build-in function that I have already defined before
            floor_intro() #get into floor_intro() page loop

        
        #wouldmap x and y will change will player walk around on the map, also the red rectangle will move as well in order to stick-in with the map and not be de-located.
        wx += wx_change
        wy += wy_change
        locax += wx_change
        locay += wy_change

        #menu location and width and height/ call-up image loading build-in function that I have already defined before
        menubutton(mx,my,mw,mh)

        mouse = pygame.mouse.get_pos()  #pygame library function: get the position of your mouse in the display window (2 datas array = [x, y])
        click = pygame.mouse.get_pressed()  #pygame library function: when mouse is unpress = 0, when mouse is press = 1 (1 data array = [0 or 1])

        #when mouse pointer get into the menu icon, the icon image will change a little bit bigger, else, it remains same size
        if  mx + mw > mouse[0] > mx and my + mh > mouse[1] > my:
            mw = 45
            mh = 45
            if click[0] == 1:  #if the icon is clicked, following things will happen:
                buttonsound3.play()  #button sound playing/ call-up build-in function
                pause = True 
                paused()  #get into other page: paused page / the game_loop()page won't restart but pause

        else:
            mw = 40
            mh = 40

        pygame.display.update()  #update all the display elements within the window
        clock.tick(15)  #updated frame will be 15 frames per second
####################

def quitgame():  #quit game build-in function, can be draw from other loop page for closing the game
    pygame.quit()  #pygame library function: quit the game
    quit() 

####################
#-<game intro page: first page>-#
def game_intro():  
    bgm5(-1) #call-out build-in function: background music 5 (intro.mp3)/-1 means loop the music forever

    #background image x,y location
    bgx = -350 
    bgy = 0

    #create while loop: page created>>> loop forever
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #fill the background with white color
        gameDisplay.fill(white)
        
        BGIMG(bgx,bgy) #call-up build-in function to load picture in/ a function I defined in the early script before

        #give font property for the game title name
        largeText = pygame.font.Font('CutPixel.TTF',30)
        TextSurf, TextRect = text_objects('Let explore!', largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 150))
        gameDisplay.blit(TextSurf, TextRect)
        
        #call-up build-in function to load rectangle and font in along with location x, y, color and function(action()) property
        button("let play it!",display_width/2-60,display_height/2-90,120,40,red,lightred,game_loop)  #action() = game_loop page >>>>> get into game_loop page 
        button("just quit it :(",display_width/2-60,display_height/2,120,40,blue,lightblue,quitgame)   #action() = quitgame page >>>>> quit the game

        #end of this page 
        pygame.display.update()
        clock.tick(60)
####################
#build-in function to unpause the game_loop() page and player keeps continous playing
def unpause():
    global pause  #insert global variable pause
    musicunpause()  #music remind playing
    pause = False  #variable pause = 0 >>>> no action, therefore unpause
####################


#-<pause page: load-in menu page>-#
def paused():
    musicpause() #music is paused

    #create while loop: page created>>> loop forever
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #give font property for the menu title name
        largeText = pygame.font.Font('CutPixel.TTF',30)
        TextSurf, TextRect = text_objects('Menu', largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 150))
        gameDisplay.blit(TextSurf, TextRect)

        #call-up build-in function to load rectangle and font in along with location x, y, color and function(action()) property
        button("continous",display_width/2-60,display_height/2-90,120,40,red,lightred,unpause)
        button("quit",display_width/2-60,display_height/2,120,40,blue,lightblue,quitgame)
        button("to main page",display_width/2-60,display_height/2+90,120,40,yellow,lightyellow,game_intro)

        #end of this page 
        pygame.display.update()
        clock.tick(60)
####################
#-<floor intro page , the page before you get into the let_jump()loop page>-#
def floor_intro():
    
    #x, y location of cloud and blue sky image
    jbgx = 0
    jbgy = 0
    bgm2(-1)  #call-out build-in function: background music 2 (floorintrobgm.mp3)/ -1 means loop the music forever
    
    #create while loop: page created>>> loop forever
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #fill up background color into yellow
        gameDisplay.fill(yellow)
        jumpbg(jbgx,jbgy) #call-up build-in function to load picture in/ a function I defined in the early script before

        #give font property for the game "let jump" a title name
        largeText = pygame.font.Font('CutPixel.TTF',30)
        TextSurf, TextRect = text_objects('Let Jump!', largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 150))
        gameDisplay.blit(TextSurf, TextRect)
        
        #call-up build-in function to load rectangle and font in along with location x, y, color and function(action()) property
        button("let play it!",display_width/2-60,display_height/2-90,120,40,red,lightred,let_jump)
        button("Back to map",display_width/2-60,display_height/2,120,40,blue,lightblue,game_loop)

        #end of this page
        pygame.display.update()
        clock.tick(60)
####################
#-<let jump gaming interaction page, let jump>-#
def let_jump():
    bgm3(-1)  #call-out build-in function: background music 3 (letjump.mp3)/ -1 means loop the music forever

    bx = 0
    by = 0

    #main character(red shirt kid) fixed location
    x=180
    y=300
    
    #character x, y move and change
    x_change=0
    y_change=5

    index = 0  #fixed index of the spritesheet(current running sub-image in a spritesheet), representing the cells in a spritesheet
    index_change=0  #running sub-image: change subimage in a spritesheet
    bb = 0  #change subimage in a spritesheet
    mm = 0  #index looping starting point- change subimage in a spritesheet

    #floor's y location move and change
    floor_speed = -4
    #floor's y location move and change
    rfloor_speed = -4

    #score at first the game is run, player have zero score at the begining game
    marks = 0
    
    #the blood bar location x and y/ width and height
    bar_x = 50
    bar_y = 580
    bar_width = 260
    bar_height = 10

    px = 0
    py = 0
    ppx = 340
    ppy = 0
    
    #x, y location of cloud and blue sky image
    jbgx = 0
    jbgy = 0

    #create while loop: page created>>> loop forever
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                    index_change = 1
                    mm = 8
                elif event.key == pygame.K_RIGHT:
                    x_change = 8
                    index_change = 1
                    mm = 12

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    index_change = 0
                    bb=0
                    mm=0
                elif event.key == pygame.K_RIGHT:
                    x_change = 0
                    index_change = 0
                    bb=0
                    mm=0

        x += x_change
        y += y_change
        bb += index_change
        index = bb %4 + mm


        gameDisplay.fill(white)
        jumpbg(jbgx,jbgy)   #call-up build-in function to load picture in/ a function I defined in the early script before

        s.ani(gameDisplay,index  % s.totalCellCount,x, y)
        
        #if the red-shirt kid fall out the window, jump to the gameover() loop page
        if y  > display_height:
            gameover()
        
        #set contrain of the left side and right side of the window
        if x  > display_width - 30-20:
            x = display_width - 30-20
        if x < 0+20:
            x = 20

        #create foo_list array
        #item is the element in the array
        #item[1] = floor's y location, item[0] = floor's x location
        for item in foo_list:
            item[1] += floor_speed
            pygame.draw.rect(gameDisplay, black, item)

            if item[1] < 0:
                item[1] = random.randrange(display_height, display_height + 600)  #at y location, floors generated randamly outside the window to create more random floor running effect
                item[0] = random.randrange(0 + 20, display_width -20 - floor_width)  #constain floor not to generated outside the left and right side of the window

            #when the player touch 1 floor, player get one marks and one sound effect generated
            if y + 45 >= item[1] - 10 and y + 45 <= item[1] - 1:  #setting constain of the floor and the player
                if x > item[0] and x < item[0] + floor_width or x + 30 > item[0] and x + 30 < item[0] + floor_width: #setting constain of the floor and the player
                    marks += 1
                    buttonsound4.play()
                    if y + 45 == item[1]:
                        marks += 0

            if  y + 40 > item[1] and y < item[1]:
                if x > item[0] and x < item[0] + floor_width or x + 30> item[0] and x + 30 < item[0] + floor_width:
                    y = item[1] - 40
                    y +=  floor_speed

        for ritem in rfoo_list:
            ritem[1] += rfloor_speed
            pygame.draw.rect(gameDisplay, red, ritem)

            if ritem[1] < 0:
                ritem[1] = random.randrange(display_height, display_height + 600)
                ritem[0] = random.randrange(0 + 20, display_width -20 - rfloor_width)

            if  y + 40 > ritem[1] and y < ritem[1]:
                if x > ritem[0] and x < ritem[0] + rfloor_width or x + 30 > ritem[0] and x + 30 < ritem[0] + rfloor_width:
                    y = ritem[1] - 40
                    y +=  rfloor_speed
                    bar_width += -1
                    buttonsound5.play()
                    #if the blood bar is empty, player will get to gameover() loop page
                    if bar_width <=0:
                        bar_width = 0
                        gameover()
        
        #call-up build-in function to load rectangle bar/ a function I defined in the early script before
        blood_bar(bar_x, bar_y, bar_width, bar_height, red)

        #player cut by the blade at the top of the window will lost blood
        if y < 40:
            bar_width += -1
            buttonsound5.play()
            #if the blood bar is empty, player will get to gameover() loop page
            if bar_width <=0:
                bar_width = 0
                gameover()
        
        #call-up build-in function to load 3 images and the text which represent the score/ a function I defined in the early script before
        blade(bx,by)
        pole1(px,py)
        pole2(ppx,ppy)
        floor_score(marks)

        #if the marks is higher than 5, speed for floor moving upward will be increase 
        #if the marks is higher than 25, speed for player falling downward will be increase 
        if marks > 5:
            floor_speed += -0.001
            if marks > 25:
                y_change += 0.001



        pygame.display.update()
        clock.tick(60)
####################
#-<gameover page>-#
def gameover():
    buttonsound6.play(0)
    bgm4(-1)

    #x and y location of the pikachu background image
    sx = -350
    sy = 0

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(red)
        pikachi(sx,sy)

        largeText = pygame.font.Font('CutPixel.TTF',30)
        TextSurf, TextRect = text_objects('you died', largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 150))
        gameDisplay.blit(TextSurf, TextRect)

        button("try again",display_width/2-60,display_height/2-90,120,40,red,lightred,let_jump)
        button("back to map",display_width/2-60,display_height/2,120,40,yellow,lightyellow,game_loop)
        button("quit",display_width/2-60,display_height/2+90,120,40,blue,lightblue,quitgame)

        pygame.display.update()
        clock.tick(60)

####################
game_intro()
game_loop()
floor_intro()
let_jump()
gameover()
pygame.quit()
quit()
