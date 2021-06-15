"""Breadth First Search and Depth First Search"""

# Importing Libraries
import pygame, sys, random, math,os
from collections import deque
from tkinter import messagebox, Tk
from pygame import mixer

def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS,relative_path)
    return os.path.join(os.path.abspath("."),relative_path)

def restart():
    #Setting the width and height of the screen
    size = (width, height) = 1280, 720
    pygame.init()

    #game icon
    programIcon = pygame.image.load(resource_path('complexity.png'))
    pygame.display.set_icon(programIcon)  
                                                
    #Creating a window of size given above
    win = pygame.display.set_mode(size)
    pygame.display.set_caption('Graph Algorithm Visualizer')

    BACKGROUND_COLOR = pygame.Color('white') #The background color of our window
    FPS = 10 #Frames per second
     
    class MySprite(pygame.sprite.Sprite):
        def __init__(self):
            super(MySprite, self).__init__()
            
            self.images = []
            

            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('pr.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            self.images.append(pygame.image.load('1.png'))
            
            self.images.append(pygame.image.load('2.png'))
            self.images.append(pygame.image.load('3.png'))
            self.images.append(pygame.image.load('4.png'))
            self.images.append(pygame.image.load('5.png'))
            self.images.append(pygame.image.load('6.png'))
            self.images.append(pygame.image.load('7.png'))
            self.images.append(pygame.image.load('8.png'))
            self.images.append(pygame.image.load('9.png'))
            self.images.append(pygame.image.load('10.png'))
            self.images.append(pygame.image.load('11.png'))
            self.images.append(pygame.image.load('12.png'))
            self.images.append(pygame.image.load('13.png'))
            self.images.append(pygame.image.load('14.png'))
            self.images.append(pygame.image.load('15.png'))
            self.images.append(pygame.image.load('16.png'))
            self.images.append(pygame.image.load('17.png'))
            self.images.append(pygame.image.load('18.png'))
            self.images.append(pygame.image.load('19.png'))
            self.images.append(pygame.image.load('20.png'))
            self.images.append(pygame.image.load('21.png'))
            self.images.append(pygame.image.load('22.png'))
            self.images.append(pygame.image.load('23.png'))
            self.images.append(pygame.image.load('24.png'))
            self.images.append(pygame.image.load('25.png'))
            self.images.append(pygame.image.load('26.png'))
            self.images.append(pygame.image.load('27.png'))
            self.images.append(pygame.image.load('28.png'))
            self.images.append(pygame.image.load('29.png'))
            self.images.append(pygame.image.load('30.png'))
            self.images.append(pygame.image.load('31.png'))
            self.images.append(pygame.image.load('32.png'))
            self.images.append(pygame.image.load('33.png'))
            

     
            self.index = 0
     
            self.image = self.images[self.index]
     
            self.rect = pygame.Rect(0,0,1280, 720)

            
     
        def update(self,stop):
            clock = pygame.time.Clock()
            clock.tick(25)
            self.index += 1

            if stop==True:
                self.index=0
                
     
            elif self.index >= len(self.images):
                self.index = 1
            
            self.image = self.images[self.index]

            




    CreateMaze = pygame.image.load('c.png')
    CreateMaze2 = pygame.image.load('c2.png')
    SampleMaze = pygame.image.load('s.png')
    SampleMaze2 = pygame.image.load('s2.png')
    lb = pygame.image.load('lb.png')
    rb = pygame.image.load('rb.png')
    #Defining Number and columns and rows 
    cols, rows = 32, 18

    # Defining pixels width and height in which the whole screen will be divided
    w = width//cols
    h = height//rows

    # Defining lists for storing the parts of the maze and their property
    # Defining queue for performing BFS
    grid = []
    queue, visited = deque(), []
    path = []

    # Defining Class which keeps all the data related to individual part of our grid
    class Spot:
        
        # Function that defines properties of individual part of grid
        def __init__(self, i, j):
            self.x, self.y = i, j
            self.neighbors = []
            self.prev = None
            self.wall = False
            self.visited = False
        
        # Function for coloring individual part of the grid
        def show(self, win, col, shape= 1):
            if self.wall == True: # Checks whether its a wall or not and changes value of color accordingly
                col = (0, 0, 0)
            if shape == 1:
                pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
            else:
                pygame.draw.rect(win, col, (self.x*w+9 , self.y*h+9 , 21 , 21))
        
        # Function for storing neghbouring individual grid so that they can be accesed afterwards
        def add_neighbors(self, grid):
            if self.x < cols - 1:
                self.neighbors.append(grid[self.x+1][self.y])
            if self.x > 0:
                self.neighbors.append(grid[self.x-1][self.y])
            if self.y < rows - 1:
                self.neighbors.append(grid[self.x][self.y+1])
            if self.y > 0:
                self.neighbors.append(grid[self.x][self.y-1]) # Checking for different conditions when the grid is out of bounds
            #Add Diagonals
            # if self.x < cols - 1 and self.y < rows - 1:
            #     self.neighbors.append(grid[self.x+1][self.y+1])
            # if self.x < cols - 1 and self.y > 0:
            #     self.neighbors.append(grid[self.x+1][self.y-1])
            # if self.x > 0 and self.y < rows - 1:
            #     self.neighbors.append(grid[self.x-1][self.y+1])
            # if self.x > 0 and self.y > 0:
            #     self.neighbors.append(grid[self.x-1][self.y-1])


    # Function for storing data related to the walls of the maze
    def clickWall(pos, state):
        i = pos[0] // w
        j = pos[1] // h
        grid[i][j].wall = state

    def createbutton(win,col,a,b,c,d):
        pygame.draw.rect(win,col,[a,b,c,d])

    # Loop to store coordinates of each individual grid in form of pairs
    for i in range(cols):
        arr = []
        for j in range(rows):
            arr.append(Spot(i, j))
        grid.append(arr)

    # Loop to add neighbours near individual grids
    for i in range(cols):
        for j in range(rows):
            grid[i][j].add_neighbors(grid)

        
    def main():
        my_sprite = MySprite()
        my_group = pygame.sprite.Group(my_sprite)
        clock = pygame.time.Clock()
        background=pygame.image.load(resource_path('background.png'))
        
        randomflag = 0
        winflag=False
        flag = False
        noflag = True
        dfsflag = False
        bfsflag = False
        startflag = False
        makewall = False
        pause = True

        randomdisplay2=True
        randomdisplay= False
        startpoint = False
        endpoint = False
        starttext=pygame.font.Font('FreeSansBold.ttf',22,bold=True)
        text1=starttext.render('SAMPLE MAZE',True,(0,0,0))
        text2=starttext.render('CREATE NEW MAZE',True,(0,0,0))
        text3=starttext.render('DFS',True,(0,0,0))
        text4=starttext.render('BFS',True,(0,0,0))
        text5=starttext.render('PRESS R TO RESTART',True,(0,0,0))
        text6=starttext.render('BACK',True,(0,0,0))

        button1=True
        button2=True
        button3=True
        button4=True
        button5=True
        click1=True
        click2=True
        buttonsound1=mixer.Sound(resource_path('button1.wav'))
        buttonsound2=mixer.Sound(resource_path('button2.wav'))
        nopath=mixer.Sound(resource_path('nopath.wav'))
        pathfound=mixer.Sound(resource_path('pathfound.wav'))
        createwall=mixer.Sound(resource_path('createwall.wav'))
        breakwall=mixer.Sound(resource_path('breakwall.wav'))
        mixer.Sound.set_volume(pathfound,0.3)
        mixer.Sound.set_volume(nopath,0.3)
        while True:
            
            my_group.update(stop=False)
            # win.fill(BACKGROUND_COLOR)
            my_group.draw(win)
            
            # clock.tick(10)
            # Define mouse as position of mouse
            mouse=pygame.mouse.get_pos()
            setposition=grid[mouse[0]//w][mouse[1]//h]
            # All the mouse and keyboard controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Tk().wm_withdraw()
                    result=messagebox.askquestion("Exit", "Are you sure you want to exit ?",icon='warning')
                    if result == 'yes':
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN and winflag:
                    if event.key == pygame.K_SPACE and pause:
                        pause = False
                    elif event.key == pygame.K_SPACE and not pause:
                        pause = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart()
                if not startflag:   
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button in (1, 3):

                            if event.button == 1:
                                if startpoint and not endpoint and (dfsflag or bfsflag):
                                    createwall.play()
                                    end=setposition
                                    endpoint=True

                            if event.button == 1:  
                                if not startpoint and (dfsflag or bfsflag):
                                    createwall.play()
                                    start=setposition
                                    startpoint=True
                                    queue.append(start)
                                    start.visited= True

                            if event.button == 3:
                                if startpoint and not endpoint and setposition==start and (dfsflag or bfsflag):
                                    breakwall.play()
                                    startpoint=False
                                    queue.pop()
                                    start.visited= False
                                if endpoint and setposition==end:
                                    breakwall.play()
                                    endpoint=False

                            if 200<=mouse[0]<=400  and height/2<=mouse[1]<=height/2 + 50 and event.button==1 and winflag and not bfsflag:
                                if not click1:
                                    buttonsound2.play()
                                    click1=True
                                dfsflag=True


                            if 740<=mouse[0]<=940  and height/2<=mouse[1]<=height/2 + 50 and event.button==1 and winflag and not dfsflag:
                                if not click1:
                                    buttonsound2.play()
                                    click1=True
                                bfsflag=True

                            if 20<=mouse[0]<=120 and 20<=mouse[1]<=60 and winflag and not (dfsflag or bfsflag):
                                if click2:
                                    buttonsound2.play()
                                    click2=False
                                click1=True
                                winflag=False
                                randomflag=0
                                
                            if 390<=mouse[0]<=825  and height/4 + 30<=mouse[1]<=height/4 + 90 and randomflag==0 and event.button==1 and not winflag:
                                if click1:
                                    buttonsound2.play()
                                    click1=False
                                randomdisplay2=False
                                winflag=True
                                randomflag=1
                                click2=True


                            if 390<=mouse[0]<=825  and height/4 + 260<=mouse[1]<=height/4 + 310 and event.button==1 and not winflag:
                                if click1:
                                    buttonsound2.play()
                                    click1=False
                                winflag=True
                                randomflag=3
                                click2=True
                            
                        
                            if (dfsflag or bfsflag) and randomflag==3 and startpoint and endpoint:
                                if event.button==1:
                                    createwall.play()
                                elif event.button==3:
                                    breakwall.play()
                                clickWall(mouse,event.button==1)
                        
                    elif event.type == pygame.MOUSEMOTION and randomflag==3 and startpoint and endpoint :
                        if event.buttons[0] or event.buttons[2]:
                            if event.buttons[0]:
                                createwall.play()
                            elif event.buttons[2]:
                                breakwall.play()
                            clickWall(mouse,event.buttons[0])
                    if event.type == pygame.KEYDOWN and startpoint and endpoint:
                        if event.key == pygame.K_RETURN:
                            startflag = True


                            
            if not winflag:
                if 390<=mouse[0]<=825 and height/4 + 30<=mouse[1]<=height/4 + 90:

                    my_group.update(stop=True)
                    
                    if not randomdisplay:
                        win.fill((0,0,0))
                        for i in range(cols):
                            for j in range(rows):
                                spot = grid[i][j]
                                if random.randint(0,100) < 20:
                                    spot.show(win, (0, 0, 0))
                                else:
                                    spot.show(win, (160, 160, 200))
                        randomdisplay=True
                elif 390>mouse[0]>825 and height/4 + 260>mouse[1]>height/4 + 310:
                    my_group.update(stop=False)
                    randomdisplay=False
                    #win.blit(background,(0,0))
                else:
                    randomdisplay=False
                    my_group.update(stop=False)
                    win.fill(BACKGROUND_COLOR)
                    my_group.draw(win)
                    #win.blit(background,(0,0))

                if 390<=mouse[0]<=825 and height/4 + 260<=mouse[1]<=height/2 + 310:
                    win.fill((0,0,0))
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            spot.show(win, (160, 160, 200))
     
                #elif 200>mouse[0]>400 and height/2>mouse[1]>height/2 + 50:
                    #win.blit(background,(0,0))
                            
                if 390<=mouse[0]<=825 and height/4+30<=mouse[1]<=height/4 + 90:
                    win.blit(lb,(270,height/4+8))
                    win.blit(rb,(820,height/4+8))
                    win.blit(SampleMaze2,(385,height/4+20))
                    if button1:
                        buttonsound1.play()
                        button1=False
                    #pygame.draw.rect(win,(255,0,255),[200,height/2,200,50])
                else:
                    win.blit(SampleMaze,(385,height/4+20))
                    button1=True
                    #pygame.draw.rect(win,(0,255,255),[200,height/2,200,50])


                if 390<=mouse[0]<=825 and height/4 + 260<=mouse[1]<=height/4 + 310:
                    win.blit(lb,(270,height/4+238))
                    win.blit(rb,(805,height/4+238))
                    win.blit(CreateMaze2,(385,height/4+250))
                    if button2:
                        buttonsound1.play()
                        button2=False
                    #pygame.draw.rect(win,(255,0,255),[740,height/2,260,50])
                else:
                    win.blit(CreateMaze,(385,height/4+250))
                    button2=True
                    #pygame.draw.rect(win,(0,255,255),[740,height/2,260,50])

                #win.blit(text1,(220,height/2+10))
                #win.blit(text2,(760,height/2+10))
            if winflag:
                my_group.update(stop=True)
                
            if winflag and not (bfsflag or dfsflag):
                if not randomdisplay2:
                    win.fill((0,0,0))
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            if random.randint(0,100) < 20:
                                spot.show(win, (0, 0, 0))
                            else:
                                spot.show(win, (160, 160, 200))
                    randomdisplay2=True
                elif randomflag==3:
                    win.fill((0,0,0))
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            spot.show(win, (160, 160, 200))
                if 200<=mouse[0]<=400 and height/2<=mouse[1]<=height/2 + 50:
                    if button3:
                        buttonsound1.play()
                        button3=False
                    pygame.draw.rect(win,(255,0,255),[200,height/2,200,50])
                else:
                    button3=True
                    pygame.draw.rect(win,(0,255,255),[200,height/2,200,50])


                if 740<=mouse[0]<=940 and height/2<=mouse[1]<=height/2 + 50:
                    if button4:
                        buttonsound1.play()
                        button4=False
                    pygame.draw.rect(win,(255,0,255),[740,height/2,200,50])
                else:
                    button4=True
                    pygame.draw.rect(win,(0,255,255),[740,height/2,200,50])


                if 20<=mouse[0]<=120 and 20<=mouse[1]<=60:
                    if button5:
                        buttonsound1.play()
                        button5=False
                    pygame.draw.rect(win,(255,0,255),[20,20,100,40])
                else:
                    button5=True
                    pygame.draw.rect(win,(0,255,255),[20,20,100,40])

                win.blit(text3,(280,height/2+10))
                win.blit(text4,(820,height/2+10))
                win.blit(text6,(40,25))

            if winflag:
                if randomflag==1:
                    for i in range(cols):
                        for j in range(rows):
                            if random.randint(0,100) < 20:
                                grid[i][j].wall=True
                        randomflag=2
            else:
                for i in range(cols):
                        for j in range(rows):
                            grid[i][j].wall=False

            if startflag and pause:
                if len(queue) > 0:
                    if dfsflag:
                        current = queue.pop()
                    elif bfsflag:
                        current = queue.popleft()
                    if current == end:
                        temp = current
                        while temp.prev:
                            path.append(temp.prev)
                            temp = temp.prev 
                        if not flag:
                            flag = True
                        elif flag:
                            continue
                    if not flag:
                        for i in current.neighbors:
                            if not i.visited and not i.wall:
                                i.visited = True
                                i.prev = current
                                queue.append(i)
                else:
                    if noflag and not flag:
                        nopath.play()
                        Tk().wm_withdraw()
                        messagebox.showinfo("No Path Found","There was no path found.")
                        Tk().wm_withdraw()
                        result=messagebox.askquestion("Restart", "Do you want to restart ?",icon='warning')
                        if result == 'yes':
                            mixer.pause()
                            restart()
                        elif result == 'no':
                            pygame.quit()
                            sys.exit()
                        noflag = False
                    else:
                        pathfound.play()
                        Tk().wm_withdraw()
                        messagebox.showinfo("Path Found","Hurrah! There exists a path.")
                        Tk().wm_withdraw()
                        result=messagebox.askquestion("Restart", "Do you want to restart ?",icon='warning')
                        if result == 'yes':
                            mixer.pause()
                            restart()
                        elif result == 'no':
                            pygame.quit()
                            sys.exit()


            
            if dfsflag or bfsflag:
                win.fill(BACKGROUND_COLOR)
                for i in range(cols):
                    for j in range(rows):
                        spot = grid[i][j]
                        spot.show(win, (160, 160, 200))
                        if spot in path:
                            spot.show(win, (0 , 0 , 0))
                            spot.show(win, (255, 153, 51),0)
                        elif spot.visited:
                            spot.show(win, (102, 0, 200))
                        if spot in queue and not flag:
                            spot.show(win, (255 , 128 , 255))
                        if startpoint: 
                            if spot == start:
                                spot.show(win,(0,0,0))
                                spot.show(win, (255,0,0),0)
                        if endpoint:
                            if spot == end:
                                spot.show(win, (0, 0, 0))
                                spot.show(win, (0,255,0),0)
                                
                if not startpoint:
                    setposition.show(win,(0,0,0))
                    setposition.show(win, (255,0,0),0)
                if startpoint and not endpoint:
                    if setposition!=start:
                        setposition.show(win,(0,0,0))
                        setposition.show(win, (0,255,0),0)   
                if startpoint and endpoint and not startflag and randomflag==3:
                    if setposition is not start and setposition is not end:
                        setposition.show(win,(0,0,0))     
                    
            # To avoid walls on the start and end
            if startpoint:
                start.wall=False
            if endpoint:
                end.wall=False
                
            pygame.display.flip()

    main()
restart()
