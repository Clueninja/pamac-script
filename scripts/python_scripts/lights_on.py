import random
side = 5
def gen_board():
    board = []
    
    for column in range(side):
        board.append([])
        for _row in range(side):
            board[column].append(0)
    return board
        
def pboard(board):
    [print(row) for row in board]

def gen_ran(board):
    num = int((side**2)/2)
    for _x in range(num):
        column=random.randint(0,side-1)
        row=random.randint(0,side-1)
        board[row][column] = 1
    return board

def get_i():
    column = int(input("Enter column No: "))
    row = int(input("Enter row No: "))
    while row>=10 or column>=10:
        print("Incorrect Input")
        column = int(input("Enter column No: "))
        row = int(input("Enter row No: "))
    return column, row

def toggle(board, row, column):
    if row<side and column<side and row>-1 and column >-1:
        light_status = board[column][row]
        if light_status==1:
            board[column][row] = 0
        elif light_status==0:
            board[column][row] = 1
    return board

def check(board):
    for column in range(side):
        for row in range(side):
            if board[column][row] == 1:
                return False

    return True

if __name__ =="__main__":
    end = False
    board = gen_board()
    board = gen_ran(board)
    while end == False:
        pboard(board)
        column,row = get_i()
        #yes its bad, could do a vector list
        board = toggle(board, row, column)
        board = toggle(board, row+1, column)
        board = toggle(board, row-1, column)
        board = toggle(board, row, column+1)
        board = toggle(board, row, column-1)
        end = check(board)

        

