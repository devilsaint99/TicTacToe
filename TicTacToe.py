def printBoard(board):
    print(board['Top-1']+'|'+board['Top-2']+'|'+board['Top-3'])
    print('------')
    print(board['Mid-1'] + '|' + board['Mid-2'] + '|' + board['Mid-3'])
    print('------')
    print(board['Bot-1'] + '|' + board['Bot-2'] + '|' + board['Bot-3'])



def check(board):
    if (board['Top-1'] == board['Top-2'] and board['Top-2'] == board['Top-3']) or ( #row
            board['Mid-1'] == board['Mid-2'] and board['Mid-2'] == board['Mid-3']) or ( #row
            board['Bot-1'] == board['Bot-2'] and board['Bot-2'] == board['Bot-3'])or ( #row
            board['Top-1'] == board['Mid-2'] and board['Mid-2'] == board['Bot-3']) or ( #diagonal
            board['Top-3'] == board['Mid-2'] and board['Mid-2'] == board['Bot-1']) or ( #diagonal
            board['Top-1'] == board['Mid-1'] and board['Mid-1'] == board['Bot-1']) or ( #column
            board['Top-2'] == board['Mid-2'] and board['Mid-2'] == board['Bot-2']) or ( #column
            board['Top-3'] == board['Mid-3'] and board['Mid-3'] == board['Bot-3']):
        var = True
    else:
        var=False
    return var

