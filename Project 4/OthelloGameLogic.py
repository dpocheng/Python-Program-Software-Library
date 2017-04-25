## Pok On Cheng 74157306. ICS 32 Lab 1 Project 4.

class Othello_Game_Logic:
    def __init__(self):
        self._rows = 0
        self._columns = 0
        self._player = ""
        self._disc = ""
        self._win = 0
        self._board = []

    def _get_rows(self) -> int:
        while True:
            try:
                print("\nThe number of rows must be an even integer between 4 and 16.")
                self._rows = int(input("Please enter the number of rows on the board: "))
            except ValueError:
                print("It's an invalid input. Please try again.")
            else:
                if self._rows in [4, 6, 8, 10, 12, 14, 16]:
                    return self._rows
                else:
                    print("It is an invalid integer. Please try again.")

    def _get_columns(self) -> int:
        while True:
            try:
                print("\nThe number of columns must be an even integer between 4 and 16.")
                print("It does not have to be the same as the number of rows.")
                self._columns = int(input("Please enter the number of columns on the board: "))
            except ValueError:
                print("It's an invalid input. Please try again.")
            else:
                if self._columns in [4, 6, 8, 10, 12, 14, 16]:
                    return self._columns
                else:
                    print("It is an invalid integer. Please try again.")

    def _player_first(self) -> str:
        while True:
            try:
                self._player = input("\nWhich of the players will move first (black or white): ")
            except:
                print("It is an invalid input. Please try again.")
            else:
                self._player = self._player.upper()
                if (self._player == "BLACK") or (self._player == "B"):
                    self._player = "BLACK"
                    return self._player
                elif (self._player == "WHITE") or (self._player == "W"):
                    self._player = "WHITE"
                    return self._player
                else:
                    print("It is an invalid input. Please try again.")

    def _disc_on_top_left(self) -> str:
        while True:
            try:
                self._disc = input("\nWhich color disc will be in the top-left position of these four center cells (white or black): ")
            except:
                print("It is an invalid input. Please try again.")
            else:
                self._disc = self._disc.upper()
                if (self._disc == "WHITE") or (self._disc == "W"):
                    self._disc = "WHITE"
                    return self._disc
                elif (self._disc == "BLACK") or (self._disc == "B"):
                    self._disc = "BLACK"
                    return self._disc
                else:
                    print("It is an invalid input. Please try again.")

    def _select_win_option(self) -> int:
        while True:
            try:
                print("\nPlease select the option what it means to win the game.")
                print("1. The player with the most discs on the board at the end of the game is the winner.")
                print("2. The player with the fewest discs on the board at the end of the game is the winner.")
                self._win = int(input("Option: "))
            except ValueError:
                print("Please enter 1 or 2 to preform winning option.")
            else:
                if (self._win == 1) or (self._win == 2):
                    return self._win
                else:
                    print("Please select 1 or 2 to perform winning option.")

    def _count_black_and_white(self) -> int:
        count_black = 0
        count_white = 0
        for numr in range(self._rows):
            for numc in range(self._columns):
                if self._board[numr][numc] == " B ":
                    count_black += 1
                elif self._board[numr][numc] == " W ":
                    count_white += 1
        return count_black, count_white

    def _opposite_turn(self) -> str:
        if self._player == "BLACK":
            return "WHITE"
        elif self._player == "WHITE":
            return "BLACK"
            
    def creating_new_game_board(self) -> list:
        rows_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        self._rows = Othello_Game_Logic._get_rows(self)
        self._columns = Othello_Game_Logic._get_columns(self)
        row_top = "  "
        for ct in range(self._columns):
            if (ct+1) > 9:
                row_top = row_top + str(ct+1) + " "
            else:
                row_top = row_top + " " + str(ct+1) + " "
        self._board.append(row_top)
        for r in range(self._rows):
            row_column = []
            row = rows_character[r] + " "
            row_column.append(row)
            for c in range(self._columns):
                row_column.append(" . ")
            self._board.append(row_column)
        self._player = Othello_Game_Logic._player_first(self)
        left = int(self._columns / 2)
        right = int((self._columns / 2) + 1)
        up = int(self._rows / 2)
        down = int((self._rows / 2) + 1)
        self._disc = Othello_Game_Logic._disc_on_top_left(self)
        if self._disc == "WHITE":
            self._board[up][left] = " W "
            self._board[up][right] = " B "
            self._board[down][left] = " B "
            self._board[down][right] = " W "
        elif self._disc == "BLACK":
            self._board[up][left] = " B "
            self._board[up][right] = " W "
            self._board[down][left] = " W "
            self._board[down][right] = " B "
        self._win = Othello_Game_Logic._select_win_option(self)
        Othello_Game_Logic.display_game_board(self, self._board, self._player)
        return self._board, self._player

    def display_game_board(self, game_board: list, turn: str) -> None:
        count_black, count_white = Othello_Game_Logic._count_black_and_white(self)
        print("\nBlack: " + str(count_black) + " White: " + str(count_white))
        self._board = game_board
        for l in game_board:
            if type(l) == list:
                print("".join([str(i) for i in l]))
            else:
                print(l)
        self._player = turn
        print("It's " + self._player + " player's turn now.")

    def display_winner(self, game_board: list, turn: str) -> None:
        count_black, count_white = Othello_Game_Logic._count_black_and_white(self)
        print("\nBlack: " + str(count_black) + " White: " + str(count_white))
        self._board = game_board
        for l in game_board:
            if type(l) == list:
                print("".join([str(i) for i in l]))
            else:
                print(l)
        self._player = turn
        print(self._player + " player win the game.")

    def winning_option(self) -> str:
        if self._win == 1:
            count_black, count_white = Othello_Game_Logic._count_black_and_white(self)
            if count_black > count_white:
                return "BLACK"
            elif count_white > count_black:
                return "WHITE"
            else:
                return "NO"
        elif self._win == 2:
            count_black, count_white = Othello_Game_Logic._count_black_and_white(self)
            if count_black < count_white:
                return "BLACK"
            elif count_white < count_black:
                return "WHITE"
            else:
                return "NO"
            
    def _ask_a_move(self) -> int:
        row_move = 0
        column_move = 0
        move_list = []
        rows_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        for i in range(self._rows):
            for j in range(self._columns):
                move = ""
                move = rows_character[i] + str(j+1)
                move_list.append(move)
        while True:
            location = input("\nPlease enter a move (e.g. a1): ")
            if location in move_list:
                if len(location) == 2:
                    row_move = Othello_Game_Logic._transform_string_to_integer(self, location[0])
                    column_move = Othello_Game_Logic._transform_string_to_integer(self, location[1])
                elif len(location) == 3:
                    row_move = Othello_Game_Logic._transform_string_to_integer(self, location[0])
                    column_move = Othello_Game_Logic._transform_string_to_integer(self, location[1:])
                else:
                    print("It's an invalid input. Please try again.")
                    continue
                if (row_move <= self._rows) and (column_move <= self._columns):
                    return row_move, column_move
                else:
                    print("It is an invalid input. Please try again.")
            elif location not in move_list:
                print("It is an invalid input. Please try again.")

    def _transform_string_to_integer(self, character: str) -> int:
        if character == "a" or character == "1":
            return 1
        elif character == "b" or character == "2":
            return 2
        elif character == "c" or character == "3":
            return 3
        elif character == "d" or character == "4":
            return 4
        elif character == "e" or character == "5":
            return 5
        elif character == "f" or character == "6":
            return 6
        elif character == "g" or character == "7":
            return 7
        elif character == "h" or character == "8":
            return 8
        elif character == "i" or character == "9":
            return 9
        elif character == "j" or character == "10":
            return 10
        elif character == "k" or character == "11":
            return 11
        elif character == "l" or character == "12":
            return 12
        elif character == "m" or character == "13":
            return 13
        elif character == "n" or character == "14":
            return 14
        elif character == "o" or character == "15":
            return 15
        elif character == "p" or character == "16":
            return 16
        
    def make_a_move(self, board: list, turn: str):
        self._player = turn
        self._board = board
        while True:
            row_move, column_move = Othello_Game_Logic._ask_a_move(self)
            if Othello_Game_Logic.verify_player_move(self, row_move, column_move, self._player, self._board):
                return row_move, column_move
            else:
                print("It is an invalid move. Please try again.")
        
    def verify_player_move(self, row_move: int, column_move: int, turn: str, board: list) -> bool:
        self._board = board
        disc = ""
        opp = ""
        if turn == "BLACK":
            disc = " B "
            opp = " W "
        elif turn == "WHITE":
            disc = " W "
            opp = " B "
        if self._board[row_move][column_move] == " B " or self._board[row_move][column_move] == " W ":
            return False
        move_direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        empty_num = 0
        for rp1, cp1 in move_direction:
            row = row_move
            column = column_move
            row = row + rp1
            column = column + cp1
            if not Othello_Game_Logic._check_on_board(self, row, column):
                empty_num += 1
            elif self._board[row][column] == " . ":
                empty_num += 1
            elif self._board[row][column] == disc:
                empty_num += 1
        if empty_num == 8:
            return False
        num = 0
        for rrp, ccp in move_direction:
            rrow = row_move
            ccolumn = column_move
            rrow = rrow + rrp
            ccolumn = ccolumn + ccp
            if Othello_Game_Logic._check_on_board(self, rrow, ccolumn) and self._board[rrow][ccolumn] == opp:
                rrow = rrow + rrp
                ccolumn = ccolumn + ccp
            if not Othello_Game_Logic._check_on_board(self, rrow, ccolumn):
                num += 1
                continue
            while self._board[rrow][ccolumn] == opp:
                rrow = rrow + rrp
                ccolumn = ccolumn + ccp
                if not Othello_Game_Logic._check_on_board(self, rrow, ccolumn):
                    num += 1
                    break
        if num == 8:
            return False
        for rp2, cp2 in move_direction:
            row2 = row_move
            column2 = column_move
            row2 = row2 + rp2
            column2 = column2 + cp2
            if Othello_Game_Logic._check_on_board(self, row2, column2) and self._board[row2][column2] == opp:
                row2 = row2 + rp2
                column2 = column2 + cp2
            if not Othello_Game_Logic._check_on_board(self, row2, column2):
                continue
            while self._board[row2][column2] == opp:
                row2 = row2 + rp2
                column2 = column2 + cp2
                if not Othello_Game_Logic._check_on_board(self, row2, column2):
                    break
                elif self._board[row2][column2] == disc:
                    return True
            if not Othello_Game_Logic._check_on_board(self, row2, column2):
                continue
            if self._board[row2][column2] == disc:
                return True
                    
                        
    def _check_on_board(self, row: int, column: int) -> bool:
        return row > 0 and row <= self._rows and column > 0 and column <= self._columns

    def flip_disc(self, row_move: int, column_move: int, board: list, turn: str) -> list:
        self._board = board
        disc = ""
        if turn == "BLACK":
            disc = " B "
        elif turn == "WHITE":
            disc = " W "
        flip_disc_list = []
        move_direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        for rp, cp in move_direction:
            sub_list = []
            row = row_move
            column = column_move
            row = row + rp
            column = column + cp
            if not Othello_Game_Logic._check_on_board(self, row, column):
                continue
            if self._board[row][column] == disc:
                continue
            while True:
                if self._board[row][column] == " . ":
                    break
                elif self._board[row][column] == disc:
                    flip_disc_list.extend(sub_list)
                    break
                else:
                    sub_list.append([row, column])
                    row = row + rp
                    column = column + cp
                    if row < 0 or row > self._rows or column < 0 or column > self._columns:
                        break
        return flip_disc_list
            
    def check_game_win(self, board: list) -> bool:
        self._board = board
        num = 0
        for r in range(self._rows):
            for c in range(self._columns):
                if self._board[r+1][c+1] == " . ":
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
                if Othello_Game_Logic.verify_player_move(self, r+1, c+1, "BLACK", self._board) or Othello_Game_Logic.verify_player_move(self, r+1, c+1, "WHITE", self._board):
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
                if Othello_Game_Logic.verify_player_move(self, r+1, c+1, "BLACK", self._board):
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
                if Othello_Game_Logic.verify_player_move(self, r+1, c+1, "WHITE", self._board):
                    num += 1
        if num == 0:
            return True
        else:
            return False
