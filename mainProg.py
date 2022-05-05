import TicTacToe
board={'Top-1':'1','Top-2':'2','Top-3':'3','Mid-1':'4','Mid-2':'5','Mid-3':'6','Bot-1':'7','Bot-2':'8','Bot-3':'9'}
print("Let's Play Tic-Tac-Toe.....")
print()
print("Player 1 you are ......   'X'")
print()
print("Player 2 you are ......   'O'")
win=False
turn='X'
for i in range(9):
    TicTacToe.printBoard(board)
    if turn=='X':
        print('Player 1 your turn: ')
    else:
        print('Player 2 your turn: ')
    move=input('Enter the square name where you want to update: ')
    if turn == 'X':
        board[move]='X'
        turn='O'
    else:
        board[move] = 'O'
        turn='X'
    if TicTacToe.check(board):
        TicTacToe.printBoard(board)
        if turn=='X':
            print('Player 1 Lost!!!!!')
        else:
            print('Player 2 Lost!!!!!')
        break


print('Game Over')