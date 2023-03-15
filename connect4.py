# Connect 4 Python
# Haruki Yoshida

from graphics import *

def draw_initial_board(win):
    # Draw initial board
    board = Rectangle(Point(150, 90), Point(640, 510))
    board.setFill("Blue")
    board.draw(win)

    # Draw Slots
    for x in range(7):
        for y in range(6):
            slot = Circle(Point(150+35+x*70, 90+35+y*70), 33)
            slot.setFill("Black")
            slot.draw(win)

def get_and_draw_player_a(win, grid):
    message = Text(Point(400, 45), "Player A Make Your Move")
    message.setTextColor("Red")
    message.setSize(30)

    finished = False
    while finished != True:
        message.draw(win)
        pt = win.getMouse()
        message.undraw()

        if 150 <= pt.x < 220:
            x = 0
        elif 220 <= pt.x < 290:
            x = 1
        elif 290 <= pt.x < 360:
            x = 2
        elif 360 <= pt.x < 430:
            x = 3
        elif 430 <= pt.x < 500:
            x = 4
        elif 500 <= pt.x < 570:
            x = 5
        elif 570 <= pt.x < 640:
            x = 6
        else:
            x = 7

        if x == 7:
            pass
        else:
            for i in range(6):
                if grid[5-i][x] != 0:
                    pass
                else:
                    grid[5-i][x] = 1
                    y = 5-i
                    finished = True
                    break

    move = Circle(Point(150 + 35 + 70*x, 90 + 35 + 70*y), 33)
    move.setFill("Red")
    move.draw(win)



def get_and_draw_player_b(win, grid):
    message = Text(Point(400, 45), "Player B Make Your Move")
    message.setTextColor("Yellow")
    message.setSize(30)

    finished = False
    while finished != True:
        message.draw(win)
        pt = win.getMouse()
        message.undraw()

        if 150 <= pt.x < 220:
            x = 0
        elif 220 <= pt.x < 290:
            x = 1
        elif 290 <= pt.x < 360:
            x = 2
        elif 360 <= pt.x < 430:
            x = 3
        elif 430 <= pt.x < 500:
            x = 4
        elif 500 <= pt.x < 570:
            x = 5
        elif 570 <= pt.x < 640:
            x = 6
        else:
            x = 7

        if x == 7:
            pass
        else:
            for i in range(6):
                if grid[5-i][x] != 0:
                    pass
                else:
                    grid[5-i][x] = 2
                    y = 5-i
                    finished = True
                    break

    move = Circle(Point(150 + 35 + 70*x, 90 + 35 + 70*y), 33)
    move.setFill("Yellow")
    move.draw(win)

def check_hor(grid):
    for a in range(6):
        for b in range(4):
            if grid[a][b] != 0 and grid[a][b] == grid[a][b+1] and grid[a][b+1] == grid[a][b+2] and grid[a][b+2] == grid[a][b+3]:
                return True
    return False

def check_ver(grid):
    for a in range(7):
        for b in range(3):
            if grid[b][a] != 0 and grid[b][a] == grid[b+1][a] and grid[b+1][a] == grid[b+2][a] and grid[b+2][a] == grid[b+3][a]:
                return True
    return False

def check_diag(grid):
    for a in range (0,3):
        for b in range(0,4):
            if grid[a][b] != 0 and grid[a][b] == grid[a+1][b+1] and grid[a+1][b+1] == grid[a+2][b+2] and grid[a+2][b+2] == grid[a+3][b+3]:
                return True
    for a in range (0,3):
        for b in range(3,7):
            if grid[a][b] != 0 and grid[a][b] == grid[a-1][b-1] and grid[a-1][b-1] == grid[a-2][b-2] and grid[a-2][b-2] == grid[a-3][b-3]:
                return True
    print("diag")
    return False

def check_win(grid):
    if check_hor(grid) == True or check_ver(grid) == True or check_diag(grid) == True:
        return True
    else:
        print(grid)
        return False

def main():
    win_height = 600
    win_width = 800
    win = GraphWin("Connect Four @H.Yoshida", win_width, win_height)
    win.setBackground("White")

    draw_initial_board(win)

    grid = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    while True:
        get_and_draw_player_a(win, grid)
        if check_win(grid) == True:
            MessageBox = Rectangle(Point(140,250), Point(650, 350))
            MessageBox.setFill("Black")
            MessageBox.draw(win)
            Message = Text(Point(395, 300), "Player A Wins!!")
            Message.setTextColor("Red")
            Message.setSize(35)
            Message.draw(win)
            win.getMouse()
            break
        get_and_draw_player_b(win, grid)
        if check_win(grid) == True:
            MessageBox = Rectangle(Point(140,250), Point(650, 350))
            MessageBox.setFill("Black")
            MessageBox.draw(win)
            Message = Text(Point(395, 300), "Player B Wins!!")
            Message.setTextColor("Yellow")
            Message.setSize(35)
            Message.draw(win)
            win.getMouse()
            break


main()
