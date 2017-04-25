# Pok On Cheng 74157306 and Vincent Tang 74655027. ICS 32 Lab 1 Project #2.
import connectfour
import collections
import socket
import connect_four_ver1

ConnectFourConnection = collections.namedtuple(
    'ConnectFourConnection', ['socket', 'socket_input', 'socket_output'])
ConnectFourMessage = collections.namedtuple(
    'ConnectFourMessage',
    ['username', 'text'])
ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])

def connect(host: str, port: int) -> ConnectFourConnection:
    '''
    Connects to a ConnectFour server running on the given host and listening
    on the given port, returning a ConnectFourConnection object describing
    that connection if successful, or raising an exception if the attempt
    to connect fails.
    '''

    connect_four_socket = socket.socket()
    
    connect_four_socket.connect((host, port))

    connect_four_socket_input = connect_four_socket.makefile('r')
    connect_four_socket_output = connect_four_socket.makefile('w')

    return ConnectFourConnection(
        socket = connect_four_socket,
        socket_input = connect_four_socket_input,
        socket_output = connect_four_socket_output)

def login(connection: ConnectFourConnection, username: str) -> bool:
    '''
    Logs a user into the ConnectFour service over a previously-made connection,
    returning True if successful and False otherwise.
    '''
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    return _expect_line(connection, 'WELCOME ' + username)

def start(connection: ConnectFourConnection) -> bool:
    _write_line(connection, 'AI_GAME')
    return _expect_line(connection, 'READY')

def red_drop(connection: ConnectFourConnection, message: str) -> bool:
    '''
    Sends a message to the ConnectFour server on behalf of the currently-
    logged-in user, returning True if successful and False otherwise.
    '''
    _write_line(connection, 'DROP ' + message)
    return _expect_line(connection, 'OKAY')

def red_pop(connection: ConnectFourConnection, message: str) -> bool:
    '''
    Sends a message to the ConnectFour server on behalf of the currently-
    logged-in user, returning True if successful and False otherwise.
    '''
    _write_line(connection, 'POP ' + message)
    return _expect_line(connection, 'OKAY')

def goodbye(connection: ConnectFourConnection) -> None:
    'Exchanges CONNECT_FOUR_GOODBYE messages with the server'
    _write_line(connection, 'CONNECT_FOUR_GOODBYE')
    _expect_line(connection, 'CONNECT_FOUR_GOODBYE')
    
def close(connection: ConnectFourConnection) -> None:
    'Closes the connection to the ConnectFour server'

    # To close the connection, we'll need to close the two pseudo-file
    # objects and the socket object.
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()




def _read_line(connection: ConnectFourConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    return connection.socket_input.readline()[:-1]



def _expect_line(connection: ConnectFourConnection, line_to_expect: str) -> bool:
    '''
    Reads a line of text sent from the server, expecting it to contain
    a particular text.  Returns True if the expected text was sent,
    False otherwise.
    '''
    return _read_line(connection) == line_to_expect


def _write_line(connection: ConnectFourConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence.
    '''
    connection.socket_output.write(line + '\r\n')
    connection.socket_output.flush()
