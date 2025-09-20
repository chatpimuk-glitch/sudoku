grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]
num = []
temp = 0
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
    
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == num:
                return False
    return True

def find_entry_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j) #(row,col)
    return None

def sudoku():
    pos = find_entry_cell(grid)
    if(pos != None):
        row,col = pos
        for i in num:
            if(check_rule(grid,row,col,i)):
                grid[row][col]=i
                if(sudoku()):
                    return True
                grid[row][col]=0
            
        return False
    else:
        return True
                
def generate_game():
    sudoku()
    for _ in range(40): 
        row = int(random(9))
        col = int(random(9))
        grid[row][col] = 0

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
            if(grid[i][j] != 0):
                text(grid[i][j],width/18*2*j+(width/18),height/18*2*i+(height/18))

def setup():
    for i in range(9):
        temp = int(random(1,10))
        while(temp in num):
            temp = int(random(1,10))
        num.append(temp)
    size(900,900)
    generate_game()
def draw():
    background(250)
    draw_table()  
    show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
