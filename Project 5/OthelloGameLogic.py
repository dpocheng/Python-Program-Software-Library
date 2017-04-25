## Pok On Cheng 74157306. ICS 32 Lab 1 Project 5.

class OthelloGameLogic:
    def __init__(self, rows: int, columns: int, first: str, top: str, win: int):
        self._rows = rows
        self._columns = columns
        self._player = self._turn_side_string(first)
        self._disc = self._turn_side_string(top)
        self._win = win
        self._board = []
        self._turn = self._player

    def creating_new_game_board(self) -> list:
        for r in range(self._rows):
            self._row_list = []
            for c in range(self._columns):
                self._row_list.append('0')
            self._board.append(self._row_list)
        left = int((self._columns / 2) - 1)
        right = int(self._columns / 2)
        up = int((self._rows / 2) - 1)
        down = int(self._rows / 2)
        if self._disc == "WHITE":
            self._board[up][left] = 'W'
            self._board[up][right] = 'B'
            self._board[down][left] = 'B'
            self._board[down][right] = 'W'
        elif self._disc == "BLACK":
            self._board[up][left] = 'B'
            self._board[up][right] = 'W'
            self._board[down][left] = 'W'
            self._board[down][right] = 'B'
        return self._board

    def _turn_side_string(self, first: str) -> str:
        if (first == 'B') or (first == 'BLACK'):
            return 'BLACK'
        elif (first == 'W') or (first == 'WHITE'):
            return 'WHITE'

    def _opposite_turn(self, turn: str) -> str:
        self._turn = turn
        if self._turn == 'WHITE':
            return 'BLACK'
        elif self._turn == 'BLACK':
            return 'WHITE'

    def _count_black_and_white(self, board: list) -> int:
        count_black = 0
        count_white = 0
        self._board = board
        for numr in range(self._rows):
            for numc in range(self._columns):
                if self._board[numr][numc] == 'B':
                    count_black += 1
                elif self._board[numr][numc] == 'W':
                    count_white += 1
        return count_black, count_white

    def verify_player_move(self, row_move: int, column_move: int, turn: str, board: list) -> bool:
        self._board = board
        disc = ''
        opp = ''
        if turn == 'BLACK':
            disc = 'B'
            opp = 'W'
        elif turn == 'WHITE':
            disc = 'W'
            opp = 'B'
        if self._board[row_move][column_move] == 'B' or self._board[row_move][column_move] == 'W':
            return False
        move_direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        empty_num = 0
        disc_num = 0
        opp_num = 0
        for rp1, cp1 in move_direction:
            row = row_move
            column = column_move
            row = row + rp1
            column = column + cp1
            if self._check_on_board(row, column) and self._board[row][column] == opp:
                while True:
                    row = row + rp1
                    column = column + cp1
                    if not self._check_on_board(row, column):
                        opp_num += 1
                        break
                    elif self._board[row][column] == '0':
                        opp_num += 1
                        break
                    elif self._board[row][column] == disc:
                        return True
            elif not self._check_on_board(row, column):
                empty_num += 1
            elif self._board[row][column] == '0':
                empty_num += 1
            elif self._board[row][column] == disc:
                empty_num += 1
                while True:
                    row = row + rp1
                    column = column + cp1
                    if not self._check_on_board(row, column):
                        disc_num += 1
                        break
                    elif self._board[row][column] == '0':
                        disc_num += 1
                        break
                    elif self._board[row][column] == opp:
                        disc_num += 1
                        break
        if empty_num == 8 or disc_num == 8:
            return False

    def _check_on_board(self, row: int, column: int) -> bool:
        return row >= 0 and row < self._rows and column >= 0 and column < self._columns

    def flip_disc(self, row_move: int, column_move: int, board: list, turn: str) -> list:
        self._board = board
        if turn == 'BLACK':
            disc = 'B'
            opp = 'W'
        elif turn == 'WHITE':
            disc = 'W'
            opp = 'B'
        flip_disc_list = []
        move_direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        for rp, cp in move_direction:
            sub_list = []
            row = row_move
            column = column_move
            row = row + rp
            column = column + cp
            if self._check_on_board(row, column):
                if self._board[row][column] == disc:
                    continue
                elif self._board[row][column] == '0':
                    continue
                elif self._board[row][column] == opp:
                    sub_list.append((row, column))
                    verify = False
                    while True:
                        row = row + rp
                        column = column + cp
                        if not self._check_on_board(row, column):
                            break
                        elif self._board[row][column] == '0':
                            break
                        elif self._board[row][column] == opp:
                            sub_list.append((row, column))
                        elif self._board[row][column] == disc:
                            verify = True
                            break
                    if verify:
                        flip_disc_list.extend(sub_list)
        return flip_disc_list
            
    def check_game_win(self, board: list) -> bool:
        self._board = board
        num = 0
        for r in range(self._rows):
            for c in range(self._columns):
                if self._board[r][c] == '0':
                    num += 1
        if num == 0:
            return True
        else:
            return False

    def check_no_step(self, board: list) -> bool:
        self._board = board
        num = 0
        for r in range(self._rows):
            for c in range(self._columns):
                if self.verify_player_move(r, c, 'BLACK', self._board) or self.verify_player_move(r, c, "WHITE", self._board):
                    num += 1
        if num == 0:
            return True
        else:
            return False

    def black_switch(self, board: list) -> bool:
        self._board = board
        num = 0
        for r in range(self._rows):
            for c in range (self._columns):
                if self.verify_player_move(r, c, 'BLACK', self._board):
                    num += 1
        if num == 0:
            return True
        else:
            return False

    def white_switch(self, board: list) -> bool:
        self._board = board
        num = 0
        for r in range(self._rows):
            for c in range(self._columns):
                if self.verify_player_move(r, c, 'WHITE', self._board):
                    num += 1
        if num == 0:
            return True
        else:
            return False

    def winning_option(self, board: list) -> str:
        self._board = board
        if self._win == 1:
            count_black, count_white = self._count_black_and_white(self._board)
            if count_black > count_white:
                return "BLACK WON!"
            elif count_white > count_black:
                return "WHITE WON!"
            else:
                return "NO WINNER!"
        elif self._win == 2:
            count_black, count_white = self._count_black_and_white(self._board)
            if count_black < count_white:
                return "BLACK WON!"
            elif count_white < count_black:
                return "WHITE WON!"
            else:
                return "NO WINNER"
