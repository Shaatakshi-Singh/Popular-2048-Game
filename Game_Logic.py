import random
def start_game():
    #create a 4X4 matrix with initial values equal to 0, indicating empty spaces in the grid
    grid=[]
    for i in range(4):
        grid.append([0]*4)
    return grid
    
def add_new_number(grid):
#generating a random row and column index and checking whether it is empty or not
    row=random.randint(0,3)
    column=random.randint(0,3)
    while(grid[row][column] != 0):
        row=random.randint(0,3)
        column=random.randint(0,3)
    grid[row][column]=2
    
    
def compress(grid):
    change=False
    temp=grid
    new_grid=[]
    for i in range(4):
        new_grid.append([0]*4)
    for j in range(4):
        pos=0
        for k in range(4):
            if grid[j][k] != 0:
                new_grid[j][pos]=grid[j][k]
                if j!=pos:
                    change=True
                pos+=1
    return new_grid,change
    
def merging(grid):
    change=False
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1] and grid[i][j]!=0:
                grid[i][j]=grid[i][j]*2
                grid[i][j+1]=0
                change=True
    return change

#For right/down movement
def reverse(grid):
    new_grid=[]
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][4-j-1])
    return new_grid
    
#For up/down movement
def transpose(grid):
    new_grid=[]
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[j][i])
    return new_grid

#MOVEMENTS

def leftMove(grid):
    compressed_grid,change1=compress(grid)
    change2=merging(compressed_grid)
    final_change=change1 or change2
    compressed_grid,temp=compress(compressed_grid)
    return compressed_grid,final_change

def rightMove(grid):
    reversed_grid=reverse(grid)
    new_grid,change=leftMove(reversed_grid)
    final_grid=reverse(new_grid)
    return final_grid,change

def upMove(grid):
    transposed_grid=transpose(grid)
    new_grid,change=leftMove(transposed_grid)
    final_grid=transpose(new_grid)
    return final_grid,change

def downMove(grid):
    transposed_grid=transpose(grid)
    new_grid,change=rightMove(transposed_grid)
    final_grid=transpose(new_grid)
    return final_grid,change
                
            
        

def current_state(grid):
    #Won
    for i in range(4):
        for j in range(4):
            if grid[i][j]==2048:
                return "WON"
    #Still in the Game
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return "GAME NOT OVER"
    #For left  and right movement, i,j is equal to i,j+1 and i,j-1 respectively
    #For up an down movement,i,j is equal to i+1,j and i-1,j respectively
    for i in range(3):
        for j in range(3):
            if grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]:
                return "GAME NOT OVER"
    #checking last row  
    for j in range(3):
        if grid[3][j]==grid[3][j+1]:
            return "GAME NOT OVER"
    #checking last column
    for i in range(3):
        if grid[i][3]==grid[i+1][3]:
            return "GAME NOT OVER"
    return "LOST"
  



