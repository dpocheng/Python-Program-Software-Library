# Pok On Cheng 74157306 and Vincent Tang 74655027. ICS 32 Lab 1 Project #2.
import connectfour
import collections
import socket
import connectfour
import connect_four_ver1
import connect_four_protocol

CONNECT_FOUR_HOST = 'evil-monkey.ics.uci.edu'
CONNECT_FOUR_PORT = 4444
ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])

def _run_user_interface() -> None:
    _show_welcome_banner()
    username = _ask_for_username()

    connection = connect_four_protocol.connect(CONNECT_FOUR_HOST, CONNECT_FOUR_PORT)

    try:
        if connect_four_protocol.login(connection, username):
            print('Welcome ' + username[1:] + "!")
        else:
            print('Login failed')
            
        while _handle_command(connection):
            pass
    finally:
        connect_four_protocol.close(connection)


def _handle_command(connection: connect_four_protocol.ConnectFourConnection) -> bool:
    command = input('[N]ew Game or [G]oodbye? ').strip().upper()
    if command == 'N':
        connect_four_protocol.start(connection)
        gameplay(connection)
        return True
    elif command == 'G':
        _handle_goodbye_command(connection)
        return False
    else:
        print('Not a valid command!')
        return True




def gameplay(connection: connect_four_protocol.ConnectFourConnection) -> None:
    board = connectfour.new_game_state()
    connect_four_ver1.display_board(board[0])
    while True:
        try:
            if connectfour.winning_player(board) == ' ':
                if board[1] == 'R':
                    print('\nRed\'s Turn')
                    column = int(input('Enter column number: '))
                    respond = True
                    if board[0][column-1][-1] == 'R':
                        while respond:
                            answer = input("Pop or Drop? (P/D) ")
                            answer = answer.upper()
                            if answer == 'P':
                                board = connectfour.pop_piece(board, column-1)
                                connect_four_protocol.red_pop(connection, str(column))
                                respond = False
                            elif answer == 'D':
                                board = connectfour.drop_piece(board, column-1)
                                connect_four_protocol.red_drop(connection, str(column))
                                respond = False
                            else:
                                print('Not a valid command! Please type P or D!\n')
                        connect_four_ver1.display_board(board[0])
                            
                    else:
                        board = connectfour.drop_piece(board, column-1)
                        connect_four_protocol.red_drop(connection, str(column))
                        connect_four_ver1.display_board(board[0])
                        
                else:
                    print('\nYellow\'s Turn')
                    yellow_turn = connect_four_protocol._read_line(connection).split()
                    if yellow_turn[0] != 'DROP' and yellow_turn[0] != 'POP':
                        yellow_turn = connect_four_protocol._read_line(connection).split()
                        board = _handle_drop_n_pop(board, yellow_turn)
                        connect_four_ver1.display_board(board[0])
                    else:
                        board = _handle_drop_n_pop(board, yellow_turn)
                        connect_four_ver1.display_board(board[0])

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
            connect_four_ver1.display_board(board[0])
        except ValueError:
            print('Not an integer!\n')
            connect_four_ver1.display_board(board[0])
        except connectfour.InvalidConnectFourMoveError:
            print('Column is full! Please enter another column number!\n')
            connect_four_ver1.display_board(board[0])

                    
                
def _handle_drop_n_pop(board:ConnectFourGameState, yellow_turn: list) -> ConnectFourGameState:
    if yellow_turn[0] == 'DROP':
        column = int(yellow_turn[1])
        board = connectfour.drop_piece(board, column-1)
        return board
    elif yellow_turn[0] == 'POP':
        column = int(yellow_turn[1])
        board = connectfour.pop_piece(board, column-1)
        return board
    else:
        print('Boo is cute!')

def _handle_goodbye_command(connection: connect_four_protocol.ConnectFourConnection) -> None:
    '''
    Handles a Goodbye command by exchanging GOODBYE messages with the server.
    '''
    print('Goodbye!')
    connect_four_protocol.goodbye(connection)

def _show_welcome_banner() -> None:
    '''
    Shows the welcome banner
    '''
    print('Welcome to Connect Four!')
    print()
    print('Please login with your username.')
    print('Remember that usernames must begin with an @ symbol')
    print()

def _ask_for_username() -> str:
    '''
    Asks the user to enter a username and returns it as a string.  Continues
    asking repeatedly until the user enters a username that begins with an
    @ symbol, as Connect Four requires.
    '''
    while True:
        username = input('Login: ')

        if username.startswith('@') and len(username) > 1:
            return username
        else:
            print('That username does not start with an @ symbol; please try again')

if __name__ == '__main__':
    _run_user_interface()
