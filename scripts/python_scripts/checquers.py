import time
def SetUpBoard():
    Board = []
    BoardRow = []
    for Column in range(9):
        BoardRow.append(str(Column))#the Column numbers
    Board.append(BoardRow)#gotta append that row
    
    for Row in range(8):#the 8 rows with board squares
        BoardRow = []
        BoardRow.append(str(Row+1))#each row starts with the row number
        for Column in range(8):
            BoardRow.append(' ')
        Board.append(BoardRow)#that's a big board

    for Row in range(1,4):
        a = 1 + Row % 2#every other column and the pattern alternates with each row
        for b in range(0,4):#four pieces per row
            Board[Row][b*2+a] = 'w'#places them

    for Row in range(6,9):
        a = 1 + Row % 2
        for b in range(0,4):
            Board[Row][b*2+a] = 'b'
    
    for Row in range(9):
        print(Board[Row])
        
    return Board

def MakeMove(Board, Turn):
    ValidInputs = False
    while ValidInputs == False:
        try:
            time.sleep(1)
            Row1 = int(input("On which row is your chosen piece?   "))
            time.sleep(1)
            Column1 = int(input("And the Column, please?   "))
            time.sleep(1)
            Row2 = int(input("On which row do you want to place it?   "))
            time.sleep(1)
            Column2 = int(input("And the Column?   "))
            time.sleep(1)
            
            ValidInputs = ValidateInputs(Board,Turn,Row1,Row2,Column1,Column2)
        except ValueError:
            Valid = False#Very False

    temp = Board[Row1][Column1]
    Board[Row1][Column1] = Board[Row2][Column2]
    Board[Row2][Column2] = temp#moves the piece into a space in an inefficent way, LOL

    if Row2 == 1 and Turn == 'b':
        Board[Row2][Column2] = 'B'
    elif Row2 == 8 and Turn == 'w':
        Board[Row2][Column2] = 'W'#where is my crown?

    
    if ((Row1 - Row2)**2) ** 0.5 == 2:#they hopped over an opponent
        a = int((Row1+Row2)/2)
        b = int((Column1+Column2)/2)
        Board[a][b] = ' '#erase the square they jumped
        if Turn == 'w':#nested if
            print("Epic take. Black has lost a piece.")#very true
            Turn = 'b'#it will get inverted again and when you take, you go again
        else:
            print("Epic take. White has lost a piece.")
            Turn = 'w'
    
    return Board, Turn
    
def CheckWin(Board):
    Bwin = True
    Wwin = True
    for a in range(1,9):
        for b in range(1,9):
            if (Board[a][b]).casefold() == 'w':
                Bwin = False#hah you thought you won
            if (Board[a][b]).casefold() == 'b':
                Wwin = False#keep on going
    if Bwin == True:
        print("Congratulations Black. You win.")
    if Wwin == True:
        print("Congratulations White. You win.")
    GameWon = False#for now
    if Bwin == True or Wwin == True:
        GameWon = True#ends game
    return GameWon

def ValidateInputs(Board,Turn,Row1,Row2,Column1,Column2):#that's a lot of parameters
    ValidInputs = True#so far
    if Row1 > 8 or Row1 < 1 or Row2 > 8 or Row2 < 1 or Column1 > 8 or Column1 < 1 or Column2 > 8 or Column2 < 1:
        print("Inputs out of range. Do it properly.")
        return False
                
    if ((Column1 - Column2)**2)**(1/2) != 1 or ((Row1 - Row2)**2)**(1/2) != 1:#was not a single diagonal step
        a = int((Row1+Row2)/2)
        b = int((Column1+Column2)/2)
        if ((Column1 - Column2)**2)**(1/2) != 2 or ((Row1 - Row2)**2)**(1/2) != 2:#then either they aren't moving perfectly diagonally or are jumping too far
            print("You can only move 1 space diagonally unless you're taking a piece. Then it's 2.")
            return False
        elif Board[a][b].casefold() == Turn:#so they are moving 2 diagonals but taking their OWN piece
            print("You can't take your own pieces")
            return False
        elif Board[a][b] == ' ':
            print("You can only move 1 space diagonally unless you're taking a piece.")
            return False
                    
    if Board[Row1][Column1] == 'w' and Row1 > Row2 or Board[Row1][Column1] == 'b' and Row1 < Row2:
        print("You can't go backwards")
        return False

    if Board[Row1][Column1].casefold() != Turn:
        print("Either that's not your piece to move or that's an empty start point")
        return False

    if Board[Row2][Column2] != ' ':
        print("You can't land there! It's taken.")
        return False

    return ValidInputs
        
Board = SetUpBoard()
Turn = 'b'#not for long
GameWon = False
while not GameWon:
    if Turn == 'b':
        Turn = 'w'
        print("White's Turn")#we take it in turns here
    else:
        Turn = 'b'
        print("Black's Turn")
    Board , Turn = MakeMove(Board, Turn)#the board gets incremented
    for Row in range(9):
        print(Board[Row])#displays board
    GameWon = CheckWin(Board)
