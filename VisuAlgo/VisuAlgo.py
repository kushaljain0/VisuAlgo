"""BFS and DFS Algorithm visualizer"""


# Importing Libraries
import pygame, sys, random, math,os
from collections import deque
from tkinter import messagebox, Tk
from pygame import mixer

# Function to define path for sound and image files when executing as an executable file
def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS,relative_path)
    return os.path.join(os.path.abspath("."),relative_path)

def restart():
    #Setting the width and height of the screen
    size = (width, height) = 1280, 720
    pygame.init()

    #game icon
    programIcon = pygame.image.load(resource_path('image/icon.png'))
    pygame.display.set_icon(programIcon)  
                                                
    #Creating a window of size given above
    win = pygame.display.set_mode(size)
    pygame.display.set_caption('Graph Algorithm Visualizer')

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
                pygame.draw.rect(win, col, (self.x*w+w//4 , self.y*h+h//4, w//2, h//2))
        
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

    # Function to display images
    def showimage(image):
        return win.blit(image[0], image[1])

    # Function for defining area for buttons
    def buttonarea(pos, area, conjugate = 0):
        if conjugate == 0:
            return area[0] <= pos[0] <= area[0]+area[2] and area[1] <= pos[1] <= area[1]+area[3]
        return area[0] > pos[0] > area[0]+area[2] and area[1] > pos[1] > area[1]+area[3]

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
        
        # Background image and buttons image
        bg = (pygame.image.load(resource_path('image/background.png')), (-50,-40))
        CreateMaze = (pygame.image.load(resource_path('image/c.png')), (395,height/4+200))
        CreateMaze2 = (pygame.image.load(resource_path('image/c2.png')), (395,height/4+200))
        SampleMaze = (pygame.image.load(resource_path('image/s.png')), (390,height/4+90))
        SampleMaze2 = (pygame.image.load(resource_path('image/s2.png')), (390,height/4+90))
        bfs = (pygame.image.load(resource_path('image/bfs.png')), (550,height/4+200))
        dfs= (pygame.image.load(resource_path('image/dfs.png')), (550,height/4+90))
        bfs2 = (pygame.image.load(resource_path('image/bfs2.png')), (550,height/4+200))
        dfs2 = (pygame.image.load(resource_path('image/dfs2.png')), (550,height/4+90))
        back = (pygame.image.load(resource_path('image/back.png')), (20,20))
        back2 = (pygame.image.load(resource_path('image/back2.png')), (20,20))


        # Grid Colours
        gridcol = (160, 160, 200)
        startcol = ((0,0,0), (255,0,0))
        endcol = ((0,0,0), (0,255,0))
        visitedcol = (102, 0, 200)
        in_queuecol = (255 , 128 , 255)
        pathcol = ((0,0,0), (255, 153, 51))
        wallcol = (0,0,0)
        
        
        # Button colors and coordinates
        col1 = (255,0,255)
        col2 = (0,255,255)
        randommaze_area = [390,height/4 + 100,470,50]
        createmaze_area = [390,height/4 + 210,470,50]
        dfs_area = [540,height/4 + 100,210,50]
        bfs_area = [540,height/4 + 210,210,50]
        back_area = [20,20,100,40]

        
        # Flags 
        randomflag = 0
        winflag = False
        flag = False
        noflag = True
        dfsflag = False
        bfsflag = False
        startflag = False
        makewall = False
        pause = True
        startpoint = False
        endpoint = False
        randomdisplay2 = True
        randomdisplay = False



        # All sound variables 
        button1 = True
        button2 = True
        button3 = True
        button4 = True
        button5 = True
        click1 = True
        click2 = True
        buttonsound1=mixer.Sound(resource_path('sound/button1.wav'))
        buttonsound2=mixer.Sound(resource_path('sound/button2.wav'))
        nopath=mixer.Sound(resource_path('sound/nopath.wav'))
        pathfound=mixer.Sound(resource_path('sound/pathfound.wav'))
        createwall=mixer.Sound(resource_path('sound/createwall.wav'))
        breakwall=mixer.Sound(resource_path('sound/breakwall.wav'))
        mixer.Sound.set_volume(pathfound, 0.3)
        mixer.Sound.set_volume(nopath, 0.3)


        while True:

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
                if event.type == pygame.KEYDOWN and startpoint and endpoint:
                    if event.key == pygame.K_RETURN:
                        startflag = True
                if not startflag:   
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button in (1, 3):

                            if event.button == 1:
                                if startpoint and not endpoint and (dfsflag or bfsflag):
                                    createwall.play()
                                    end = setposition
                                    endpoint = True

                            if event.button == 1:  
                                if not startpoint and (dfsflag or bfsflag):
                                    createwall.play()
                                    start = setposition
                                    startpoint = True
                                    queue.append(start)
                                    start.visited = True

                            if event.button == 3:
                                if startpoint and not endpoint and setposition == start and (dfsflag or bfsflag):
                                    breakwall.play()
                                    startpoint = False
                                    queue.pop()
                                    start.visited = False
                                if endpoint and setposition == end:
                                    breakwall.play()
                                    endpoint = False

                            if buttonarea(mouse, dfs_area) and event.button == 1 and winflag and not bfsflag:
                                if not click1:
                                    buttonsound2.play()
                                    click1 = True
                                dfsflag = True


                            if buttonarea(mouse, bfs_area) and event.button == 1 and winflag and not dfsflag:
                                if not click1:
                                    buttonsound2.play()
                                    click1 = True
                                bfsflag = True

                            if buttonarea(mouse, back_area) and winflag and not (dfsflag or bfsflag):
                                if click2:
                                    buttonsound2.play()
                                    click2 = False
                                click1 = True
                                winflag = False
                                randomflag = 0
                                
                            if buttonarea(mouse, randommaze_area) and randomflag == 0 and event.button == 1 and not winflag:
                                if click1:
                                    buttonsound2.play()
                                    click1 = False
                                randomdisplay2 = False
                                winflag = True
                                randomflag = 1
                                click2 = True


                            if buttonarea(mouse, createmaze_area) and event.button == 1 and not winflag:
                                if click1:
                                    buttonsound2.play()
                                    click1 = False
                                winflag = True
                                randomflag = 3
                                click2 = True
                            
                        
                            if (dfsflag or bfsflag) and randomflag == 3 and startpoint and endpoint:
                                if event.button == 1:
                                    createwall.play()
                                elif event.button == 3:
                                    breakwall.play()
                                clickWall(mouse, event.button == 1)
                        
                    elif event.type == pygame.MOUSEMOTION and randomflag == 3 and startpoint and endpoint :
                        if event.buttons[0] or event.buttons[2]:
                            if event.buttons[0]:
                                createwall.play()
                            elif event.buttons[2]:
                                breakwall.play()
                            clickWall(mouse, event.buttons[0])
                    


            # Opening Screen                
            if not winflag:
                if buttonarea(mouse, randommaze_area):
                    if not randomdisplay:
                        win.fill(wallcol)
                        for i in range(cols):
                            for j in range(rows):
                                spot = grid[i][j]
                                if random.randint(0,100) < 20:
                                    spot.show(win, wallcol)
                                else:
                                    spot.show(win, gridcol)
                        randomdisplay = True
                elif buttonarea(mouse, createmaze_area, 1):
                    randomdisplay = False
                    showimage(bg)
                else:
                    randomdisplay = False
                    showimage(bg)

                if buttonarea(mouse, createmaze_area):
                    win.fill(wallcol)
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            spot.show(win,gridcol)
     
                elif buttonarea(mouse, randommaze_area, 1):
                    showimage(bg)
                            
                if buttonarea(mouse, randommaze_area):
                    if button1:
                        buttonsound1.play()
                        button1 = False
                    showimage(SampleMaze2)
                else:
                    button1 = True
                    showimage(SampleMaze)


                if buttonarea(mouse, createmaze_area):
                    if button2:
                        buttonsound1.play()
                        button2 = False
                    showimage(CreateMaze2)
                else:
                    button2 = True
                    showimage(CreateMaze)
                    

            # Algorithm Deciding Screen
            if winflag and not (bfsflag or dfsflag):
                if not randomdisplay2:
                    win.fill(wallcol)
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            if random.randint(0,100) < 20:
                                spot.show(win, wallcol)
                            else:
                                spot.show(win, gridcol)
                    randomdisplay2 = True
                elif randomflag == 3:
                    win.fill(wallcol)
                    for i in range(cols):
                        for j in range(rows):
                            spot = grid[i][j]
                            spot.show(win, gridcol)
                if buttonarea(mouse, dfs_area):
                    if button3:
                        buttonsound1.play()
                        button3 = False
                    showimage(dfs2)
                else:
                    button3 = True
                    showimage(dfs)


                if buttonarea(mouse, bfs_area):
                    if button4:
                        buttonsound1.play()
                        button4 = False
                    showimage(bfs2)
                else:
                    button4 = True
                    showimage(bfs)


                if buttonarea(mouse, back_area):
                    if button5:
                        buttonsound1.play()
                        button5 = False
                    showimage(back2)
                else:
                    button5 = True
                    showimage(back)


            # Loop to create a random maze when its selected
            if winflag:
                if randomflag == 1:
                    for i in range(cols):
                        for j in range(rows):
                            if random.randint(0,100) < 20:
                                grid[i][j].wall = True
                        randomflag = 2
            else:
                for i in range(cols):
                        for j in range(rows):
                            grid[i][j].wall = False


            # BFS or DFS Algorithm running
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
                        messagebox.showinfo("Path Found","Hurrah! Path found.")
                        Tk().wm_withdraw()
                        result=messagebox.askquestion("Restart", "Do you want to restart ?",icon='warning')
                        if result == 'yes':
                            mixer.pause()
                            restart()
                        elif result == 'no':
                            pygame.quit()
                            sys.exit()


            # Colouring Blocks and displaying it according to above running algorithm
            if dfsflag or bfsflag:
                win.fill(wallcol)
                for i in range(cols):
                    for j in range(rows):
                        spot = grid[i][j]
                        spot.show(win, gridcol)
                        if spot in path:
                            spot.show(win, pathcol[0])
                            spot.show(win, pathcol[1], 0)
                        elif spot.visited:
                            spot.show(win, visitedcol)
                        if spot in queue and not flag:
                            spot.show(win, in_queuecol)
                        if startpoint: 
                            if spot == start:
                                spot.show(win, startcol[0])
                                spot.show(win, startcol[1], 0)
                        if endpoint:
                            if spot == end:
                                spot.show(win, endcol[0])
                                spot.show(win, endcol[1], 0)
                                
                if not startpoint:
                    setposition.show(win, startcol[0])
                    setposition.show(win, startcol[1], 0)
                if startpoint and not endpoint:
                    if setposition != start:
                        setposition.show(win, endcol[0])
                        setposition.show(win, endcol[1], 0)   
                if startpoint and endpoint and not startflag and randomflag == 3:
                    if setposition is not start and setposition is not end:
                        setposition.show(win, wallcol)     

                    
            # To avoid walls on the start and end
            if startpoint:
                start.wall = False
            if endpoint:
                end.wall = False

            # Updating screen in every loop   
            pygame.display.flip()

    main()
restart()
