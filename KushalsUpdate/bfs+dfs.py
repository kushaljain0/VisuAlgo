"""Breadth First Search and Depth First Search"""

# Importing Libraries
import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk
from pygame import mixer

def restart():
    #Setting the width and height of the screen
    size = (width, height) = 1280, 960
    pygame.init()

    #game icon
    programIcon = pygame.image.load('complexity.png')
    pygame.display.set_icon(programIcon)  
                                                
    #Creating a window of size given above
    win = pygame.display.set_mode(size)
    pygame.display.set_caption('Graph Algorithm Visualizer')

    #Defining Number and columns and rows 
    cols, rows = 32, 24

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
        starttext=pygame.font.SysFont('gabriolia',28,bold=True)
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
        buttonsound1=mixer.Sound("button1.wav")
        buttonsound2=mixer.Sound("button2.wav")
        nopath=mixer.Sound("nopath.wav")
        pathfound=mixer.Sound("pathfound.wav")
        while True:
            # Define mouse as position of mouse
            mouse=pygame.mouse.get_pos()
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
                                    end=grid[mouse[0]//w][mouse[1]//h]
                                    endpoint=True

                            if event.button == 1:  
                                if not startpoint and (dfsflag or bfsflag):
                                    start=grid[mouse[0]//w][mouse[1]//h]
                                    startpoint=True
                                    queue.append(start)
                                    start.visited= True

                            if event.button == 3:
                                if startpoint and not endpoint and grid[mouse[0]//w][mouse[1]//h]==start and (dfsflag or bfsflag):
                                    startpoint=False
                                    queue.pop()
                                    start.visited= False
                                if endpoint and grid[mouse[0]//w][mouse[1]//h]==end:
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
                                
                            if 200<=mouse[0]<=400  and height/2<=mouse[1]<=height/2 + 50 and randomflag==0 and event.button==1 and not winflag:
                                if click1:
                                    buttonsound2.play()
                                    click1=False
                                randomdisplay2=False
                                winflag=True
                                randomflag=1
                                click2=True


                            if 740<=mouse[0]<=1000  and height/2<=mouse[1]<=height/2 + 50 and event.button==1 and not winflag:
                                if click1:
                                    buttonsound2.play()
                                    click1=False
                                winflag=True
                                randomflag=3
                                click2=True
                            
                        
                            if (dfsflag or bfsflag) and randomflag==3 and startpoint and endpoint:
                                clickWall(mouse,event.button==1)
                        
                    elif event.type == pygame.MOUSEMOTION and randomflag==3 and startpoint and endpoint :
                        if event.buttons[0] or event.buttons[2]:
                            clickWall(mouse,event.buttons[0])
                    if event.type == pygame.KEYDOWN and startpoint and endpoint:
                        if event.key == pygame.K_RETURN:
                            startflag = True


                            
            if not winflag:
                if 200<=mouse[0]<=400 and height/2<=mouse[1]<=height/2 + 50:
                    if not randomdisplay:
                        for i in range(cols):
                            for j in range(rows):
                                spot = grid[i][j]
                                if random.randint(0,100) < 20:
                                    spot.show(win, (0, 0, 0))
                                else:
                                    spot.show(win, (160, 160, 200))
                        randomdisplay=True
                elif 740>mouse[0]>1000 and height/2>mouse[1]>height/2 + 50:
                    randomdisplay=False
                    win.fill((0,0,0))
                else:
                    randomdisplay=False
                    win.fill((0,0,0))

                if 740<=mouse[0]<=1000 and height/2<=mouse[1]<=height/2 + 50:
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            spot.show(win, (160, 160, 200))
     
                elif 200>mouse[0]>400 and height/2>mouse[1]>height/2 + 50:
                    win.fill((0,0,0))
                            
                if 200<=mouse[0]<=400 and height/2<=mouse[1]<=height/2 + 50:
                    if button1:
                        buttonsound1.play()
                        button1=False
                    pygame.draw.rect(win,(255,0,255),[200,height/2,200,50])
                else:
                    button1=True
                    pygame.draw.rect(win,(0,255,255),[200,height/2,200,50])


                if 740<=mouse[0]<=1000 and height/2<=mouse[1]<=height/2 + 50:
                    if button2:
                        buttonsound1.play()
                        button2=False
                    pygame.draw.rect(win,(255,0,255),[740,height/2,260,50])
                else:
                    button2=True
                    pygame.draw.rect(win,(0,255,255),[740,height/2,260,50])

                win.blit(text1,(220,height/2+12))
                win.blit(text2,(760,height/2+12))

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

                win.blit(text3,(280,height/2+12))
                win.blit(text4,(820,height/2+12))
                win.blit(text6,(40,30))

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
                        continue


            
            if dfsflag or bfsflag:
                win.fill((0, 0, 0))
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
                            spot.show(win, (255 , 128 , 0))
                        if startpoint: 
                            if spot == start:
                                spot.show(win,(0,0,0))
                                spot.show(win, (255,0,0),0)
                        if endpoint:
                            if spot == end:
                                spot.show(win, (0, 0, 0))
                                spot.show(win, (0,255,0),0)
                                
                if not startpoint:
                    grid[mouse[0]//w][mouse[1]//h].show(win,(0,0,0))
                    grid[mouse[0]//w][mouse[1]//h].show(win, (255,0,0),0)
                if startpoint and not endpoint:
                    if grid[mouse[0]//w][mouse[1]//h]!=start:
                        grid[mouse[0]//w][mouse[1]//h].show(win,(0,0,0))
                        grid[mouse[0]//w][mouse[1]//h].show(win, (0,255,0),0)   
                if startpoint and endpoint and not startflag and randomflag==3:
                    if grid[mouse[0]//w][mouse[1]//h] is not start and grid[mouse[0]//w][mouse[1]//h] is not end:
                        grid[mouse[0]//w][mouse[1]//h].show(win,(0,0,0))     

            if flag and len(queue)==0:
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
                    
            # To avoid walls on the start and end
            if startpoint:
                start.wall=False
            if endpoint:
                end.wall=False
                
            pygame.display.flip()

    main()
restart()
