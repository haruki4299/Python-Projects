# Idea from https://www.youtube.com/watch?v=jl5yUEdekEM
# Starting by solving text base

def checkValid(board,number,row,col):
    # Check the row
    for i in range(9):
        if board[row][i] == number:
            return False
    # Check the column
    for i in range(9):
        if board[i][col] == number:
            return False
    
    # Check the 3x3 square
    squareRow = (row // 3) * 3
    squareCol = (col // 3) * 3
    for i in range(squareRow, squareRow + 3):
        for j in range(squareCol, squareCol + 3):
            if board[i][j] == number:
                return False
    
    return True
    
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for number in range(1,10):
                    if checkValid(board,number,row,col):
                        board[row][col] = number
                        res = solve(board)
                        if res == True:
                            # It is solved
                            return True
                        board[row][col] = 0
                return False
    return True

def printBoard(board):
    for i in range(9):
        print(str(board[i][0]) + " " + str(board[i][1]) + " " + str(board[i][2]) + " " + str(board[i][3]) + " " + str(board[i][4]) + " " + str(board[i][5]) + " " + str(board[i][6]) + " " + str(board[i][7]) + " " + str(board[i][8]))
    
def main():
    board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
    print("The board to Begin with: \n")
    printBoard(board)
    print()
    
    res = solve(board)
    
    if res == True:
        print("Sudoku solved: \n")
        printBoard(board)
    else:
        print("Unsolvable!")
    
main()