import sys
import os
import tkinter as tkinter
import pygame
import time
import random

wp = 200
hp = 300
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
lightred = (255,102,102)
lightblue = (102, 153, 255)
lightyellow = (240, 230, 104)
floor_width = 90
floor_height = 20
rfloor_width = 90
rfloor_height = 20

display_width = 360
display_height = 600

BGimg_width = 960
BGimg_height = 600

ww = 1440
wh = 960

pole_width = 20
pole_height = 600

blade_width = 360
blade_height = 38

s_width = 1055
s_height = 600

class Game(object):
    def __init__(self, root, w, h):
        self.root = root
        self.width = w
        self.height = h

        # Tk init
        self.frame = tkinter.Frame(root, width=w, height=h)
        self.status1 = tkinter.Label(root, text="Let explore",bd = 10)
        self.status1.grid(row=0, columnspan=2)
        self.status2 = tkinter.Label(root, text="This is an RPG map explore game where you can go to different location and challenge the game!",bd = 10)
        self.status2.grid(row=1, columnspan=2)
        self.status3 = tkinter.Label(root, text="Production:",bd = 10)
        self.status3.grid(row=2, columnspan=2)
        self.status4 = tkinter.Label(root, text="Eyes on up production",bd = 10)
        self.status4.grid(row=3, columnspan=2)
        self.status5 = tkinter.Label(root, text="created by Steven",bd = 10)
        self.status5.grid(row=4, columnspan=2)
        self.status5 = tkinter.Label(root, text="sprite sheet example:",bd = 10)
        self.status5.grid(row=5, columnspan=2)
        self.photo = tkinter.PhotoImage(file="pika.png")
        self.label = tkinter.Label(root, image=self.photo)
        self.label.grid(row=6, columnspan=2)

        self.button1 = tkinter.Button(
            root, text='-', command=lambda: self.incr_step(-1))
        self.button1.grid(row=7, column=0)
        self.button2 = tkinter.Button(
            root, text='+', command=lambda: self.incr_step(1))
        self.button2.grid(row=7, column=1)# these two button are suppout to click and move the ball in pygame window. but unsucessful:(

        # Tk init
        root.update()
        #-------------------
        #os.environ['SDL_WINDOWID'] = str(self.frame.winfo_id())
        #if sys.platform == "win32":
            #os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.display.init()
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((display_width,display_height))
        self.clock = pygame.time.Clock()
        self.fg_color = pygame.Color(255,255,255)

        self.position = 0
        self.step = 3

        self.game_intro()
        self.game_loop()
        self.floor_intro()
        self.let_jump()
        self.gameover()
        self.paused()

        #pygame.quit()
        #quit()




    def game_intro(self):
        mapbgmusic = pygame.mixer.music.load("intro.mp3")
        pygame.mixer.music.play()
        bgx = -350
        bgy = 0
        buttonsound1 = pygame.mixer.Sound('k.wav')
        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            BGImg = pygame.image.load('intro_bg.jpg')#load the image source
            BGImg = pygame.transform.scale(BGImg, (BGimg_width, BGimg_height))
            self.gameDisplay.blit(BGImg,(bgx,bgy))

            self.position = (self.position + self.step) % self.width
            coord = self.position, self.height // 2
            pygame.draw.circle(self.gameDisplay, self.fg_color, coord, 20)



            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()


            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2-90 + 40 > mouse[1] > display_height/2-90:
                pygame.draw.rect(self.gameDisplay, lightred, [display_width/2-60, display_height/2-90, 120, 40])

                if click[0] == 1:
                    #buttonsound1.play()
                    #action()

                    buttonsound1.play()
                    self.game_loop()

            else:
                pygame.draw.rect(self.gameDisplay, red, [display_width/2-60, display_height/2-90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',30)
            text = font.render("play!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-54),(display_height/2-86 )) )


            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2 + 40 > mouse[1] > display_height/2:
                pygame.draw.rect(self.gameDisplay, lightblue, [display_width/2-60, display_height/2, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    pygame.quit()
                    quit()
            else:
                pygame.draw.rect(self.gameDisplay, blue, [display_width/2-60, display_height/2, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',30)
            text = font.render("quit!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-50),(display_height/2+4 )) )

            font = pygame.font.Font('CutPixel.TTF',30)
            text = font.render("LET EXPLORE!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-155),(display_height/2-180 )) )

            #self.frame.after(5, self.game_loop)

            pygame.display.update()
            #self.clock.tick(60)





    def game_loop(self):
        mapbgmusic = pygame.mixer.music.load("mapmusic.mp3")
        pygame.mixer.music.play()

        wx = 0
        wy = 0
        x=180
        y=300
        x_change=0
        y_change=0
        bb = 0
        mm = 0
        index = 0
        index_change=0

        locax = 310
        locay = 560
        locaw = 60
        locah = 120

        mx = 20
        my = 20
        mw =40
        mh=40


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

                    elif event.key == pygame.K_UP:
                        y_change = -8
                        index_change = 1
                        mm = 4


                    elif event.key == pygame.K_DOWN:
                        y_change = 8
                        index_change = 1
                        mm = 0

                    if event.key == pygame.K_p:
                        pause = True
                        paused()

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

            x += x_change
            y += y_change
            bb += index_change
            index = bb % 4 + mm

            tom = pygame.image.load("tom.png").convert_alpha()
            tom =  pygame.transform.scale(tom, (120, 180))

            cols = 4
            rows = 4
            totalCellCount = 4*4

            rect_info = tom.get_rect()
            w = cell_Width = int(rect_info.width / 4)
            h = cell_Height = int(rect_info.height / 4)
            hw,hh = CellCenter = (int(w/2),int(h/2))


            cells = list([(int(index % 4)*w, int(index/4)*h ,w ,h)for index in range(totalCellCount)])


            pygame.draw.rect(self.gameDisplay, red, (locax,locay,locaw,locah))


            worldimg = pygame.image.load("worldmap.png").convert_alpha()
            worldimg = pygame.transform.scale(worldimg, (ww, wh))
            self.gameDisplay.blit(worldimg,(wx,wy))

            self.gameDisplay.blit(tom,(x , y ),cells[index  % totalCellCount])

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

            if x + 30 > locax and x < locax + locaw and y + 45 > locay and y < locay + locah:
                buttonsound2 = pygame.mixer.Sound('m.wav')
                buttonsound2.play()
                self.floor_intro()


            wx += wx_change
            wy += wy_change
            locax += wx_change
            locay += wy_change

            menubu1 = pygame.image.load("menu.png").convert_alpha()
            menubu1 =  pygame.transform.scale(menubu1, (mw, mh))
            self.gameDisplay.blit(menubu1,(mx,my))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            buttonsound3 = pygame.mixer.Sound('p.wav')

            if  mx + mw > mouse[0] > mx  and my + mh > mouse[1] > my:
                mw = 45
                mh = 45
                if click[0] == 1:
                    buttonsound3.play()
                    #pause = True
                    self.paused()

            else:
                mw = 40
                mh = 40




            pygame.display.update()
            self.clock.tick(60)

    def floor_intro(self):
        mapbgmusic = pygame.mixer.music.load("floorintrobgm.mp3")
        pygame.mixer.music.play()

        jbgx = 0
        jbgy = 0

        buttonsound1 = pygame.mixer.Sound('k.wav')

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #self.gameDisplay.fill(yellow)
            jumpImg = pygame.image.load('jumpbg.png')
            jumpImg = pygame.transform.scale(jumpImg, (display_width, display_height))
            self.gameDisplay.blit(jumpImg,(jbgx,jbgy))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            font = pygame.font.Font('CutPixel.TTF',30)
            text = font.render("LET JUMP!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-115),(display_height/2-180 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2-90 + 40 > mouse[1] > display_height/2-90:
                pygame.draw.rect(self.gameDisplay, lightred, [display_width/2-60, display_height/2-90, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    self.let_jump()

            else:
                pygame.draw.rect(self.gameDisplay, red, [display_width/2-60, display_height/2-90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("play!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-20),(display_height/2-75 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2 + 40 > mouse[1] > display_height/2:
                pygame.draw.rect(self.gameDisplay, lightyellow, [display_width/2-60, display_height/2, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    self.game_loop()

            else:
                pygame.draw.rect(self.gameDisplay, yellow, [display_width/2-60, display_height/2, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("back to menu", True, black)
            self.gameDisplay.blit(text, ((display_width/2-48),(display_height/2+15 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2+90 + 40 > mouse[1] > display_height/2+90:
                pygame.draw.rect(self.gameDisplay, lightblue, [display_width/2-60, display_height/2+90, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    pygame.quit()
                    quit()

            else:
                pygame.draw.rect(self.gameDisplay, blue, [display_width/2-60, display_height/2+90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("quit!", True, black)
            self.gameDisplay.blit(text,((display_width/2-20),(display_height/2+105)))



            pygame.display.update()
            self.clock.tick(60)


    def let_jump(self):
        mapbgmusic = pygame.mixer.music.load("letjump.mp3")
        pygame.mixer.music.play()

        bar_x = 50
        bar_y = 50
        bar_width = 260
        bar_height = 10
        barinfo = bar_x,bar_y,bar_width,bar_height
        #position = 0
        floor_speed = -10
        rfloor_speed = -8

        index = 0
        x=180
        y=300

        x_change=0
        y_change=15

        index_change=0

        bb = 0
        mm = 0

        marks = 0

        px = 0
        py = 0
        ppx = 340
        ppy = 0

        bx = 0
        by = 0

        jbgx = 0
        jbgy = 0

        bar_x = 50
        bar_y = 580
        bar_width = 260
        bar_height = 10

        buttonsound4 = pygame.mixer.Sound('t.wav')
        buttonsound5 = pygame.mixer.Sound('l.wav')

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

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -15
                        index_change = 1
                        mm = 8
                    elif event.key == pygame.K_RIGHT:
                        x_change = 15
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

            #self.gameDisplay.fill(white)
            jumpImg = pygame.image.load('jumpbg.png')
            jumpImg = pygame.transform.scale(jumpImg, (display_width, display_height))
            self.gameDisplay.blit(jumpImg,(jbgx,jbgy))
            #coord = position, hp // 2
            #pygame.draw.circle(self.gameDisplay, red, coord, 20)
            #pygame.draw.rect(self.gameDisplay, red, (barinfo))

            tom = pygame.image.load("tom.png").convert_alpha()
            tom =  pygame.transform.scale(tom, (120, 180))

            cols = 4
            rows = 4
            totalCellCount = 4*4

            rect_info = tom.get_rect()
            w = cell_Width = int(rect_info.width / 4)
            h = cell_Height = int(rect_info.height / 4)
            hw,hh = CellCenter = (int(w/2),int(h/2))

            cells = list([(int(index % 4)*w, int(index/4)*h ,w ,h)for index in range(totalCellCount)])

            self.gameDisplay.blit(tom,(x , y ),cells[index  % totalCellCount])

            if y  > display_height:
                self.gameover()

            if x  > display_width - 30-20:
                x = display_width - 30-20

            if x < 0+20:
                x = 20


            for item in foo_list:
                item[1] += floor_speed
                pygame.draw.rect(self.gameDisplay, black, item)

                if item[1] < 0:
                    item[1] = random.randrange(display_height, display_height + 600)
                    item[0] = random.randrange(0 + 20, display_width -20 - floor_width)

                if y + 50 >= item[1] - 20and y + 50 <= item[1] - 1:
                    if x > item[0] and x < item[0] + floor_width or x + 60 > item[0] and x + 60 < item[0] + floor_width:
                        marks += 1
                        buttonsound4.play()
                        if y + 50 == item[1]:
                            marks += 0

                if  y + 50 > item[1] and y < item[1]:
                    #print('touch the floor')
                    if x > item[0] and x < item[0] + floor_width or x + 30> item[0] and x + 30 < item[0] + floor_width:
                        #print('touch two floor2')
                        y = item[1] - 50
                        y +=  floor_speed

            for ritem in rfoo_list:
                ritem[1] += rfloor_speed
                pygame.draw.rect(self.gameDisplay, red, ritem)


                if ritem[1] < 0:
                    ritem[1] = random.randrange(display_height, display_height + 600)
                    ritem[0] = random.randrange(0 + 20, display_width -20 - rfloor_width)

                if  y + 50 > ritem[1] and y < ritem[1]:
                    #print('touch the floor')

                    if x > ritem[0] and x < ritem[0] + rfloor_width or x + 30 > ritem[0] and x + 30 < ritem[0] + rfloor_width:
                        #print('touch two floor2')
                        y = ritem[1] - 50
                        y +=  rfloor_speed
                        bar_width += -3
                        buttonsound5.play()
                        if bar_width <=0:
                            bar_width = 0
                            gameover()

            pygame.draw.rect(self.gameDisplay, red, (bar_x , bar_y , bar_width, bar_height))

            if y < 40:
                bar_width += -1
                buttonsound5.play()

                if bar_width <=0:
                    bar_width = 0
                    gameover()

            bladeImg = pygame.image.load('blade.png')#load the image source
            bladeImg = pygame.transform.scale(bladeImg, (blade_width, blade_height))
            self.gameDisplay.blit(bladeImg,(bx,by))


            pole1Img = pygame.image.load('pole1.png')#load the image source
            pole1Img = pygame.transform.scale(pole1Img, (pole_width, pole_height))
            self.gameDisplay.blit(pole1Img,(px,py))

            pole2Img = pygame.image.load('pole2.png')#load the image source
            pole2Img = pygame.transform.scale(pole2Img, (pole_width, pole_height))
            self.gameDisplay.blit(pole2Img,(ppx,ppy))

            font = pygame.font.SysFont(None, 40)
            text = font.render("Score:"+ str(marks), True, black)
            self.gameDisplay.blit(text, (10,10))




            pygame.display.update()
            self.clock.tick(60)

    def gameover(self):
        buttonsound6 = pygame.mixer.Sound('d.wav')
        buttonsound6.set_volume(1.0)
        buttonsound6.play(0)

        mapbgmusic = pygame.mixer.music.load("youdie.mp3")
        pygame.mixer.music.play()

        sx = -350
        sy = 0

        buttonsound1 = pygame.mixer.Sound('k.wav')

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            gameoverImg = pygame.image.load('gameoverbg.gif')#load the image source
            gameoverImg = pygame.transform.scale(gameoverImg, (s_width, s_height))
            self.gameDisplay.blit(gameoverImg,(sx,sy))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            font = pygame.font.Font('CutPixel.TTF',30)
            text = font.render("You die!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-115),(display_height/2-180 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2-90 + 40 > mouse[1] > display_height/2-90:
                pygame.draw.rect(self.gameDisplay, lightred, [display_width/2-60, display_height/2-90, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    self.let_jump()

            else:
                pygame.draw.rect(self.gameDisplay, red, [display_width/2-60, display_height/2-90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("play!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-20),(display_height/2-75 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2 + 40 > mouse[1] > display_height/2:
                pygame.draw.rect(self.gameDisplay, lightyellow, [display_width/2-60, display_height/2, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    self.game_loop()

            else:
                pygame.draw.rect(self.gameDisplay, yellow, [display_width/2-60, display_height/2, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("back to menu", True, black)
            self.gameDisplay.blit(text, ((display_width/2-48),(display_height/2+15 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2+90 + 40 > mouse[1] > display_height/2+90:
                pygame.draw.rect(self.gameDisplay, lightblue, [display_width/2-60, display_height/2+90, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    pygame.quit()
                    quit()

            else:
                pygame.draw.rect(self.gameDisplay, blue, [display_width/2-60, display_height/2+90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("quit!", True, black)
            self.gameDisplay.blit(text,((display_width/2-20),(display_height/2+105)))





            pygame.display.update()
            self.clock.tick(60)

    def paused(self):
        pygame.mixer.music.pause()
        gameExit = False

        buttonsound1 = pygame.mixer.Sound('k.wav')

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            font = pygame.font.Font('CutPixel.TTF',30)
            text = font.render("Pause!", True, black)
            self.gameDisplay.blit(text, ((display_width/2-65),(display_height/2-180 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2-90 + 40 > mouse[1] > display_height/2-90:
                pygame.draw.rect(self.gameDisplay, lightred, [display_width/2-60, display_height/2-90, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    self.game_loop()

            else:
                pygame.draw.rect(self.gameDisplay, red, [display_width/2-60, display_height/2-90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("continous", True, black)
            self.gameDisplay.blit(text, ((display_width/2-32),(display_height/2-75 )) )

            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2 + 40 > mouse[1] > display_height/2:
                pygame.draw.rect(self.gameDisplay, lightyellow, [display_width/2-60, display_height/2, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    pygame.quit()
                    quit()

            else:
                pygame.draw.rect(self.gameDisplay, yellow, [display_width/2-60, display_height/2, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("quit", True, black)
            self.gameDisplay.blit(text, ((display_width/2-15),(display_height/2+15 )) )



            if display_width/2-60 + 120 > mouse[0] > display_width/2-60  and display_height/2+90 + 40 > mouse[1] > display_height/2+90:
                pygame.draw.rect(self.gameDisplay, lightblue, [display_width/2-60, display_height/2+90, 120, 40])

                if click[0] == 1:
                    buttonsound1.play()
                    self.game_intro()

            else:
                pygame.draw.rect(self.gameDisplay, blue, [display_width/2-60, display_height/2+90, 120, 40])

            font = pygame.font.Font('CutPixel.TTF',10)
            text = font.render("to main page", True, black)
            self.gameDisplay.blit(text,((display_width/2-45),(display_height/2+105)))


            pygame.display.update()
            self.clock.tick(60)

    def incr_step(self, inc):
            self.step += inc



if __name__ == "__main__":
    root = tkinter.Tk()
    game = Game(root, 300, 450)
    root.mainloop()
