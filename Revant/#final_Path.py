"""Breadth First Search and Depth First Search"""

# Importing Libraries
import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk


#Setting the width and height of the screen
size = (width, height) = 1280, 720
pygame.init()
                                            
#Creating a window of size given above
win = pygame.display.set_mode(size)
pygame.display.set_caption('Graph Algorithm Visualizer')


BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        
        self.images = []
        
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/pr.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/1.png'))
        
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/2.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/3.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/4.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/5.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/6.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/7.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/8.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/9.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/10.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/11.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/12.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/13.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/14.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/15.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/16.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/17.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/18.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/19.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/20.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/21.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/22.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/23.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/24.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/25.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/26.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/27.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/28.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/29.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/30.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/31.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/32.png'))
        self.images.append(pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/images/33.png'))
        

 
        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(0,0,1200, 700)

        
 
    def update(self,stop):
        clock = pygame.time.Clock()
        # clock.tick(25)
        self.index += 1

        if stop==True:
            self.index=0
            
 
        elif self.index >= len(self.images):
            self.index = 1
        
        self.image = self.images[self.index]

        




CreateMaze = pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/c.png')
CreateMaze2 = pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/c2.png')
SampleMaze = pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/s.png')
SampleMaze2 = pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/s2.png')
lb = pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/lb.png')
rb = pygame.image.load('c:/Users/REVANT/Desktop/CODING/notebooks/codingfile/rb.png')
#Defining Number and columns and rows 
cols, rows = 32, 18

# Defining pixel width and height in which the whole screen will be divided
w = width//cols
h = height//rows

# Defining lists for storing the parts of the maze and their property
# Defining queue for performing BFS
grid = []
queue = deque()
visited = []
path = []

    # Defining Class which keeps all the data related to individual part of our grid
class Spot:
    
    # Function that defines properties of individual part of grid
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
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
            pygame.draw.rect(win, col, (self.x*w+4 , self.y*h+4 , 11 , 11))
    
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
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
    
 
        


    randomflag = 0
    winflag=False
    flag = False
    noflag = True
    dfsflag = False
    bfsflag = False
    startflag = False
    pause = True

    randomdisplay= False
    startpoint = False
    endpoint = False
    starttext=pygame.font.SysFont('gabriolia',28,bold=True)
    text1=starttext.render('SAMPLE MAZE',True,(0,0,0))
    text2=starttext.render('CREATE NEW MAZE',True,(0,0,0))
    text3=starttext.render('DFS',True,(0,0,0))
    text4=starttext.render('BFS',True,(0,0,0))
    text5=starttext.render('PRESS R TO RESTART',True,(0,0,0))

    running = True
    while running:

        my_group.update(stop=False)
        # win.fill(BACKGROUND_COLOR)
        my_group.draw(win)
        
        # clock.tick(10)




        if startpoint:
            start.wall=False
        if endpoint:
            end.wall=False
        if startflag==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in (1, 3):

                        if event.button == 1:
                            if startpoint and endpoint==False and (dfsflag or bfsflag):
                                end=grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]
                                endpoint=True

                        if event.button == 1:  
                            if startpoint==False and (dfsflag or bfsflag):
                                start=grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]
                                startpoint=True
                                queue.append(start)
                                start.visited= True

                        if event.button == 3:
                            if startpoint and endpoint==False and grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]==start and (dfsflag or bfsflag):
                                startpoint=False
                                queue.pop()
                                start.visited= False
                            if endpoint and grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]==end:
                                endpoint=False

                        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+30<=pygame.mouse.get_pos()[1]<=height/4 + 90 and event.button==1 and winflag and bfsflag==False:
                            dfsflag=True


                        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+260<=pygame.mouse.get_pos()[1]<=height/4 + 310 and event.button==1 and winflag and dfsflag==False:
                            bfsflag=True
                            
                        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+30<=pygame.mouse.get_pos()[1]<=height/4 + 90 and randomflag==0 and event.button==1 and winflag==False:
                            winflag=True
                            randomflag=1


                        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+260<=pygame.mouse.get_pos()[1]<=height/4 + 310 and event.button==1 and winflag==False:
                            winflag=True
                            randomflag=3

                            
                        if (dfsflag or bfsflag) and randomflag==3 and startpoint and endpoint:
                            clickWall(pygame.mouse.get_pos(), event.button==1)
                            
                elif event.type == pygame.MOUSEMOTION and randomflag==3 and startpoint and endpoint :
                    if event.buttons[0] or event.buttons[2]:
                        clickWall(pygame.mouse.get_pos(),event.buttons[0])
                if event.type == pygame.KEYDOWN and startpoint and endpoint:
                    if event.key == pygame.K_RETURN:
                        startflag = True
                
                        
# Exiting and pause function for path finder
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and winflag:
                if event.key == pygame.K_SPACE and pause==True:
                    pause = False
                elif event.key == pygame.K_SPACE and pause==False:
                    pause = True
            if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
        
        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+30<=pygame.mouse.get_pos()[1]<=height/4 + 90:

            my_group.update(stop=True)


            if randomdisplay==False:
                for i in range(cols):
                    for j in range(rows):
                        spot = grid[i][j]
                        if random.randint(0,100) < 20:
                            spot.show(win, (0, 0, 0))
                        else:
                            spot.show(win, (160, 160, 200))
                randomdisplay=True
        elif 390<pygame.mouse.get_pos()[0]<825 and height/4+260<pygame.mouse.get_pos()[1]<height/4 +310:

            my_group.update(stop=False)

            randomdisplay=False
            for i in range(cols):
                for j in range(rows):
                    spot = grid[i][j]
                    spot.show(win, (0, 0, 0))
        else:
            randomdisplay=False

            my_group.update(stop=False)
            win.fill(BACKGROUND_COLOR)
            my_group.draw(win) 
            # for i in range(cols):
            #     for j in range(rows):
            #         spot = grid[i][j]
            #         spot.show(win, (0, 0, 0))

        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+260<=pygame.mouse.get_pos()[1]<=height/4 + 310:
            for i in range(cols):
                for j in range(rows):
                    spot = grid[i][j]
                    spot.show(win, (160, 160, 200))

        # elif 390>pygame.mouse.get_pos()[0]>825 and height/4+30>pygame.mouse.get_pos()[1]>height/4 + 90:
        #     for i in range(cols):
        #         for j in range(rows):
        #             spot = grid[i][j]
        #             spot.show(win, (0, 0, 0))
                    
        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+30<=pygame.mouse.get_pos()[1]<=height/4 + 90:
            win.blit(lb,(270,height/4+8))
            win.blit(rb,(820,height/4+8))
            win.blit(SampleMaze2,(385,height/4+20))
            #pygame.draw.rect(win,(255,0,255),[0,height/4-200,1200,400],2)
            
        else:
            win.blit(SampleMaze,(385,height/4+20))
            #pygame.draw.rect(win,(0,255,255),[400,height/4,400,50])
            


        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+260<=pygame.mouse.get_pos()[1]<=height/4 + 310:
            win.blit(lb,(270,height/4+238))
            win.blit(rb,(805,height/4+238))
            win.blit(CreateMaze2,(385,height/4+250))
        #     pygame.draw.rect(win,(255,0,255),[400,3*height/4,400,50])
        else:
            win.blit(CreateMaze,(385,height/4+250))
        #     pygame.draw.rect(win,(0,255,255),[400,3*height/4,400,50])

        
        
        #win.blit(text1,(220,height/2+12))


        #win.blit(text2,(760,height/2+12))

        if winflag:
            win.fill(BACKGROUND_COLOR)
            
        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+30<=pygame.mouse.get_pos()[1]<=height/4 + 90 and winflag:
            pygame.draw.rect(win,(255,0,255),[200,height/2,200,50])
        elif winflag:
            pygame.draw.rect(win,(0,255,255),[200,height/2,200,50])


        if 390<=pygame.mouse.get_pos()[0]<=825 and height/4+260<=pygame.mouse.get_pos()[1]<=height/4 + 310 and winflag:
            pygame.draw.rect(win,(255,0,255),[740,height/2,200,50])
        elif winflag:
            pygame.draw.rect(win,(0,255,255),[740,height/2,200,50])

        if winflag:
            win.blit(text3,(280,height/2+12))
            win.blit(text4,(820,height/2+12))


        if randomflag==1:
            for i in range(cols):
                for j in range(rows):
                    if random.randint(0,100) < 20:
                        grid[i][j].wall=True
                randomflag=2

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
                        print("Done")
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    noflag = False
                else:
                    continue


        
        if dfsflag or bfsflag:
            win.fill(BACKGROUND_COLOR)
            for i in range(cols):
                for j in range(rows):
                    spot = grid[i][j]
                    spot.show(win, (160, 160, 200))
                    if spot in path:
                        spot.show(win, (0 , 0 , 0)) #solution path
                        spot.show(win, (255, 153, 51),0)
                    elif spot.visited:
                        spot.show(win, (102, 0, 200))
                    if spot in queue and flag==False:
                        spot.show(win, (255 , 128 , 0))
                    if startpoint: 
                        if spot == start:
                            spot.show(win,(0,0,0))
                            spot.show(win, (255,0,0),0)
                    if endpoint:
                        if spot == end:
                            spot.show(win, (0, 0, 0))
                            spot.show(win, (0,255,0),0)
                            
            if startpoint==False:
                grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win,(0,0,0))
                grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win, (255,0,0),0)
            if startpoint and endpoint==False:
                if grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]!=start:
                    grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win,(0,0,0))
                    grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win, (0,255,0),0)   
            if startpoint and endpoint and startflag==False and randomflag==3:
                if grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]!=start and grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]!=end:
                    grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win,(0,0,0))     
            if flag or not noflag:
                win.blit(text5,(560,height/2+12))
                
        pygame.display.flip()



main()

