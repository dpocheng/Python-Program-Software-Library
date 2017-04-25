# Pok On Cheng 74157306 and Vincent Tang 74655027. ICS 32 Lab 1 Project #2.

import connectfour
import collections

ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])

def display_board(game_state: ConnectFourGameState) -> None:
    ''' Show the connect four board
    '''
    print("1  2  3  4  5  6  7")
    for r in range(connectfour.BOARD_ROWS):
        print('  '.join(game_state[x][r] for x in range(connectfour.BOARD_COLUMNS)))

def gameplay() -> None:
    board = connectfour.new_game_state()
    display_board(board[0])
    while True:
        try:
            if connectfour.winning_player(board) == ' ':
                if board[1] == 'R':
                    print('\nRed\'s Turn')
                    column = int(input('Enter column number: '))
                    if board[0][column-1][-1] == 'R':
                        board = pop_or_drop(board, column)
                    else:
                        board = connectfour.drop_piece(board, column-1)
                        display_board(board[0])
                else:
                    print('\nYellow\'s Turn')
                    column = int(input('Enter column number: '))
                    if board[0][column-1][-1] == 'Y':
                        board = pop_or_drop(board, column)
                    else:
                        board = connectfour.drop_piece(board, column-1)
                        display_board(board[0])
            else:
                
                player = ""
                if connectfour.winning_player(board) == 'R':
                    player += "Red Player"
                else:
                    player += "Yellow Player"
                print('Game is over! '+player+' is the winner!')
                break
        except IndexError:
            print('Column number you entered is not in the range of 1-7!\n')
            display_board(board[0])
        except ValueError:
            print('Not an integer!\n')
            display_board(board[0])
        except connectfour.InvalidConnectFourMoveError:
            print('Column is full! Please enter another column number!\n')
            display_board(board[0])


def pop_or_drop(board:ConnectFourGameState, column:int)->ConnectFourGameState:
    respond = True
    while respond:
        answer = input("Pop or Drop? (P/D) ")
        answer = answer.upper()
        if answer == 'P':
            board = connectfour.pop_piece(board, column-1)
            display_board(board[0])
            respond = False
            return board
        elif answer == 'D':
            board = connectfour.drop_piece(board, column-1)
            display_board(board[0])
            respond = False
            return board
        else:
            print('Not a valid command! Please type P or D!\n')


    
        
if __name__ == '__main__':
    gameplay()
