grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]

def check_rule(board,row,col,num):
    #check row
    for i in range(9):
        if num == board[row][i]:
            return False
        
    #check column
    for i in range(9):
        if num == board[i][col]:
            return False
        
    #check box 3x3
    pos_box_x = col//3
    pos_box_y = row//3
    
    for i in range(3):
        for j in range(3):
            if num == board[pos_box_y+i][pos_box_x+j]:
                return False
    return True

def find_entry_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j) #(row,col)
    return None

def sudoku():
    for i in range(81):
        row,col = find_entry_cell(grid)
        n = int(random(1,10))
        if( check_rule(grid,row,col,n)):
            grid[row][col] = n
        else:
            s = check_rule(grid,row,col,n)
            while(!s):
                n = int(random(1,10))
                s = check_rule(grid,row,col,n)
            grid[row][col] = n

def draw_table():
    strokeWeight(3)
    line(0,height/3,width,height/3)
    line(0,height/3*2,width,height/3*2)
    
    line(width/3,0,width/3,height)
    line(width/3*2,0,width/3*2,height)
    strokeWeight(1)
    line(0,height/9,width,height/9)
    line(0,height/9*2,width,height/9*2)
    line(0,height/9*4,width,height/9*4)
    line(0,height/9*5,width,height/9*5)
    line(0,height/9*7,width,height/9*7)
    line(0,height/9*8,width,height/9*8)
    
    line(width/9,0,width/9,height)
    line(width/9*2,0,width/9*2,height)
    line(width/9*4,0,width/9*4,height)
    line(width/9*5,0,width/9*5,height)
    line(width/9*7,0,width/9*7,height)
    line(width/9*8,0,width/9*8,height)

def show():
    for i in range(9):
        for j in range(9):
            fill(0)
            textSize(20)
            text(grid[i][j],width/18*2*j+(width/18),height/18*2*i+(height/18))
def setup():
    size(900,900)
    sudoku()
def draw():
    background(250)
    draw_table()  
    show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
