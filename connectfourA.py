#player1turn Morris
#Connect Four

import sys
import copy


def main():

    print("Welcome to connect four\nHow many columns is your board. Max 4")
    columns = int(input())

    while(columns > 4):
        print("Invalid number for columns\nEnter new number <=4")
        columns = int(input())
    
    print(columns)
    
    print("How many rows is your board. Max 4")
    rows = int(input())
    
    while(rows > 4):
        print("Invalid number for rows\nEnter new number <=4")
        rows = int(input())
        
    print(rows)
    
    print("How many colors in a row do you have to get?")

    requiredtowin = int(input())

    while(requiredtowin > 4 or requiredtowin < 3):
        print("Invalid number for required to win\nEnter new number 3 or 4")
        requiredtowin = int(input())

    print(requiredtowin)

    board = [['0' for y in range(columns)] for x in range(rows)]

    printboard(board, columns, rows)
    
    player1turn = False
    table = {}

    print("Please wait. Calculating all possible moves. \nHigher numbers for rows and columns take around a minute to calculate")


    x = minimax(board, player1turn, columns, rows, requiredtowin, table)


    print("Total states: ", len(table))
    
    if x == 10000:
        print("minimax determines first player wins")
    elif x == -10000:
        print("minimax determines second player wins")
    else:
        print("minimax determines its a tie")

    print("Beginning game")
    player1turn = True

    while checkforwinner(board, columns, rows, requiredtowin) is False and isfull(board, columns, rows) is False:
            movesarray = []
            getmoves(board, not player1turn, columns, rows, movesarray)
            maxmove = -100000000
            for item in movesarray:
                x = str(item)
                if x in table:

                    if table[x] > maxmove:
                        maxmove = table[x]
                        bestmove = x
                        b = item

            if player1turn == True:
                board = b
                printboard(board, columns, rows)

            else:
                insertcoin(board,  player1turn, columns, rows)

            player1turn = not player1turn

 
def minimax(board, player1turn, columns, rows, requiredtowin, table):
    if str(board) in table:
        return table[str(board)]
    
    maxtotal = -100000000000
    movesarray = []
    getmoves(board, player1turn, columns, rows, movesarray)    
    for item in movesarray:
        t = minvalue(item, not player1turn, columns, rows, requiredtowin, table)
        if t > maxtotal:
            maxtotal = t
    return maxtotal

def maxvalue(board, player1turn, columns, rows, requiredtowin, table):   
    if str(board) in table:
        return table[str(board)]
    if checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == True:
        table[str(board)] = 10000
        return 10000
    if checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == False:
        table[str(board)] = -10000
        return -10000
    if isfull(board, columns, rows) is True:
        table[str(board)] = 0
        return 0
    v = -1000000
    movesarray = []
    getmoves(board, player1turn, columns, rows, movesarray)
        
    for item in movesarray:
        v = max(v, minvalue(item, not player1turn, columns, rows, requiredtowin, table))
        minimaxofchild = minimax(item, not player1turn, columns, rows, requiredtowin, table)
        if minimaxofchild > v:
            v = minimaxofchild
    table[str(board)] = v
    return v

def minvalue(board, player1turn, columns, rows, requiredtowin, table):
    if str(board) in table:
        return table[str(board)]
    if checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == True:
        table[str(board)] = 10000
        return 10000
    if checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == False:
        table[str(board)] = -10000
        return -10000
    if isfull(board, columns, rows) is True:
        table[str(board)] = 0
        return 0
    v = 1000000
    movesarray = []
    getmoves(board, player1turn, columns, rows, movesarray)    

    for item in movesarray:
        v = min(v, maxvalue(item, not player1turn, columns, rows, requiredtowin, table))
        minimaxofchild = minimax(item, not player1turn, columns, rows, requiredtowin, table)
        if minimaxofchild < v:
            v = minimaxofchild
    table[str(board)] = v
    return v



def getmoves(board, player1turn, columns, rows, movesarray):
    if player1turn == True:
        for columnchoice in range(columns):
            state = copy.deepcopy(board)

            if board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
                continue
            else:
                i = rows -1
                while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
                    i = i- 1          
                state[i][columnchoice-1] = 'R'
                movesarray.append(state)
    else:
        for columnchoice in range(columns):
            state = copy.deepcopy(board)

            if board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
                continue
            else:
                i = rows -1
                while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
                    i = i- 1          
                state[i][columnchoice-1] = 'B'
                movesarray.append(state)
    return movesarray
 

def printboard(board, columns, rows):
    for x in range(rows):
        for y in range(columns):
            print(' %s |' % board[x][y], end='')
        print("\n")
        
def insertcoin(board, player1turn, columns, rows):
    if player1turn == True:
        print("In which column would player1 like to insert coin?")
        columnchoice = int(input())
        while board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
            print("Can't put coin there. Enter new input: ")
            columnchoice = int(input())
        i = rows -1
        while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
            i = i- 1
        board[i][columnchoice-1] = 'B'
    else:
        print("In which column would player2 like to insert coin?")
        columnchoice = int(input())
        while(columnchoice <1 or columnchoice >columns):
            print("Can't put coin there. Enter new input: ")
            columnchoice = int(input())
        while board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
            print("Can't put coin there. Enter new input: ")
            columnchoice = int(input())
        i = rows -1
        while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
            i = i- 1          
        board[i][columnchoice-1] = 'R'
          
def isfull(board, columns, rows):
    for x in range(rows):
        for y in range(columns):
            if board[x][y] == '0':
                return False
    return True

def checkforwinner(board, columns, rows, requiredtowin):
    if requiredtowin == 3:
        for x in range(rows):
            for y in range(columns):
                if y+2<columns:
                    if board[x][y] == 'B' and board[x][y+1] =='B' and board[x][y+2] == 'B':
##                        print("player1 won horizontal")
                        return True
                    if board[x][y] == 'R' and board[x][y+1] =='R' and board[x][y+2] == 'R':
##                        print("player2 won horizontal")
                        return True
        
        for x in range(rows):
            for y in range(columns):
                if x+2<rows:
                    if board[x][y] == 'B' and board[x+1][y] =='B' and board[x+2][y] == 'B':
##                        print("player1 won vertical")
                        return True
                    if board[x][y] == 'R' and board[x+1][y] =='R' and board[x+2][y] == 'R':
##                        print("player2 won vertical")
                        return True

        for x in range(rows):
            for y in range(columns):
                if x+2<rows and y-2>=0:
                    if board[x][y] == 'B' and board[x+1][y-1] =='B' and board[x+2][y-2] == 'B':
##                        print("player1 won with up horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y-1] =='R' and board[x+2][y-2] == 'R':
##                        print("player2 won with up horizontal")
                        return True
                  # down and over
        for x in range(rows):
            for y in range(columns):
                if y+2<columns and x+2<rows:
                    if board[x][y] == 'B' and board[x+1][y+1] =='B' and board[x+2][y+2] == 'B':
##                        print("player1 won with down horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y+1] =='R' and board[x+2][y+2] == 'R':
##                        print("player2 won with down horizontal")
                        return True
        return False
    else:
        for x in range(rows):
            for y in range(columns):
                if y+3<columns:
                    if board[x][y] == 'B' and board[x][y+1] =='B' and board[x][y+2] == 'B' and board[x][y+3] == 'B':
##                        print("player1 won horizontal")
                        return True
                    if board[x][y] == 'R' and board[x][y+1] =='R' and board[x][y+2] == 'R' and board[x][y+3] == 'R':
##                        print("player2 won horizontal")
                        return True
        
        for x in range(rows):
            for y in range(columns):
                if x+3<rows:
                    if board[x][y] == 'B' and board[x+1][y] =='B' and board[x+2][y] == 'B' and board[x+3][y] == 'B':
##                        print("player1 won vertical")
                        return True
                    if board[x][y] == 'R' and board[x+1][y] =='R' and board[x+2][y] == 'R' and board[x+3][y] == 'R':
##                        print("player2 won vertical")
                        return True

        for x in range(rows):
            for y in range(columns):
                if x+3<rows and y-3>=0:
                    if board[x][y] == 'B' and board[x+1][y-1] =='B' and board[x+2][y-2] == 'B' and board[x+3][y-3] == 'B':
##                        print("player1 won with up horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y-1] =='R' and board[x+2][y-2] == 'R' and board[x+3][y-3] == 'R':
##                        print("player2 won with up horizontal")
                        return True
                  
        for x in range(rows):
            for y in range(columns):
                if y+3<columns and x+3<rows:
                    if board[x][y] == 'B' and board[x+1][y+1] =='B' and board[x+2][y+2] == 'B' and board[x+3][y+3] == 'B':
##                        print("player1 won with down horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y+1] =='R' and board[x+2][y+2] == 'R' and board[x+3][y+3] == 'R':
##                        print("player2 won with down horizontal")
                        return True
        return False

       
main()



