## Pok On Cheng 74157306. ICS 32 Lab 1 Project 5.

import tkinter
import OthelloGameLogic
from math import ceil

DEFAULT_FONT = ('Times New Roman', 12)

class CreatingOthelloGUI:
    def __init__(self):
        self._creating_GUI = tkinter.Toplevel()

        ask_row1_label = tkinter.Label(master = self._creating_GUI, text = 'How many rows do you want to create?', font = DEFAULT_FONT)
        ask_row1_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        ask_row2_label = tkinter.Label(master = self._creating_GUI, text = 'Please enter an even number between [4] and [16].', font = DEFAULT_FONT)
        ask_row2_label.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        row_label = tkinter.Label(master = self._creating_GUI, text = 'Row:', font = DEFAULT_FONT)
        row_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._row_entry = tkinter.Entry(master = self._creating_GUI, width = 20, font = DEFAULT_FONT)
        self._row_entry.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        ask_column1_label = tkinter.Label(master = self._creating_GUI, text = 'How many columns do you want to create?', font = DEFAULT_FONT)
        ask_column1_label.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        ask_column2_label = tkinter.Label(master = self._creating_GUI, text = 'Please enter an even number between [4] and [16].', font = DEFAULT_FONT)
        ask_column2_label.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        column_label = tkinter.Label(master = self._creating_GUI, text = 'Column:', font = DEFAULT_FONT)
        column_label.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._column_entry = tkinter.Entry(master = self._creating_GUI, width = 20, font = DEFAULT_FONT)
        self._column_entry.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        ask_first_label = tkinter.Label(master = self._creating_GUI, text = 'Which player go first? ([B]lack or [W]hite)', font = DEFAULT_FONT)
        ask_first_label.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        first_label = tkinter.Label(master = self._creating_GUI, text = 'First player:', font = DEFAULT_FONT)
        first_label.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._first_entry = tkinter.Entry(master = self._creating_GUI, width = 20, font = DEFAULT_FONT)
        self._first_entry.grid(row = 7, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        ask_top_label = tkinter.Label(master = self._creating_GUI, text = 'Which color be on top-left? ([W]hite or [B]lack)', font = DEFAULT_FONT)
        ask_top_label.grid(row = 8, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.W)
        top_label = tkinter.Label(master = self._creating_GUI, text = 'Top-left:', font = DEFAULT_FONT)
        top_label.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._top_entry = tkinter.Entry(master = self._creating_GUI, width = 20, font = DEFAULT_FONT)
        self._top_entry.grid(row = 9, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        ask_win1_label = tkinter.Label(master = self._creating_GUI, text = 'Please select the option what it means to win the game:', font = DEFAULT_FONT)
        ask_win1_label.grid(row = 10, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        ask_win2_label = tkinter.Label(master = self._creating_GUI, text = '[1] The player with the most discs on the board at the end of the game is the winner.', font = DEFAULT_FONT)
        ask_win2_label.grid(row = 11, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        ask_win3_label = tkinter.Label(master = self._creating_GUI, text = '[2] The player with the fewest discs on the board at the end of the game is the winner.', font = DEFAULT_FONT)
        ask_win3_label.grid(row = 12, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = tkinter.W)
        win_label = tkinter.Label(master = self._creating_GUI, text = 'Win option:', font = DEFAULT_FONT)
        win_label.grid(row = 13, column = 0, padx = 10, pady = 19, sticky = tkinter.W)
        self._win_entry = tkinter.Entry(master = self._creating_GUI, width = 20, font = DEFAULT_FONT)
        self._win_entry.grid(row = 13, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master = self._creating_GUI)
        button_frame.grid(row = 14, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(master = button_frame, text = 'OK', font = DEFAULT_FONT, command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(master = button_frame, text = 'Cancel', font = DEFAULT_FONT, command = self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._creating_GUI.rowconfigure(14, weight = 1)
        self._creating_GUI.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        self._row = ''
        self._column = ''

    def show(self) -> None:
        self._creating_GUI.grab_set()
        self._creating_GUI.wait_window()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_rows(self) -> str:
        return self._row

    def get_columns(self) -> str:
        return self._column

    def get_first(self) -> str:
        return self._first

    def get_top(self) -> str:
        return self._top

    def get_win(self) -> str:
        return self._win

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._row = self._row_entry.get()
        self._column = self._column_entry.get()
        self._first = self._first_entry.get()
        self._top = self._top_entry.get()
        self._win = self._win_entry.get()
        self._creating_GUI.destroy()

    def _on_cancel_button(self) -> None:
        self._creating_GUI.destroy()

class OthelloGameboard:
    def __init__(self, rows: int, columns: int, first: str, top: str, win: int):
        self._gameboard = tkinter.Toplevel()
        self._rows = rows
        self._columns = columns
        self._first = first
        self._top = top
        self._win = win
        logic = OthelloGameLogic.OthelloGameLogic(rows, columns, first, top, win)
        self._board = logic.creating_new_game_board()
        black, white = logic._count_black_and_white(self._board)
        self._turn = self._turn_side_string(self._first)
        self._turn_state = tkinter.StringVar()
        self._turn_state.set(self._turn + '\'s turn')
        self._game_state1 = tkinter.StringVar()
        self._game_state1.set('BLACK: ' + str(black))
        self._game_state2 = tkinter.StringVar()
        self._game_state2.set('WHITE: ' + str(white))
        self._replay_clicked = False
        self._exit_clicked = True
        turn_state_label = tkinter.Label(master = self._gameboard, textvariable = self._turn_state, font = DEFAULT_FONT)
        turn_state_label.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        self._size = 32
        self._width = self._columns * self._size
        self._height = self._rows * self._size
        self._canvas = tkinter.Canvas(master = self._gameboard, width = self._width, height = self._height, border = 2, relief = tkinter.GROOVE, background = 'lightgreen')
        self._canvas.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._gameboard.rowconfigure(1, weight = 1)
        self._gameboard.columnconfigure(0, weight = 1)
        game_state1_label = tkinter.Label(master = self._gameboard, textvariable = self._game_state1, font = DEFAULT_FONT)
        game_state1_label.grid(row = 2, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        game_state2_label = tkinter.Label(master = self._gameboard, textvariable = self._game_state2, font = DEFAULT_FONT)
        game_state2_label.grid(row = 3, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        self._button1 = tkinter.Button(master = self._gameboard, text = 'Replay', font = DEFAULT_FONT, command = self._on_replay_button)
        self._button1.grid(row = 4, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        self._button2 = tkinter.Button(master = self._gameboard, text = 'Exit', font = DEFAULT_FONT, command = self._on_exit_button)
        self._button2.grid(row = 5, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._redraw_all_spots()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        xsize = canvas_width / self._columns
        ysize = canvas_height / self._rows
        height_list = self._frange(0, canvas_height, ysize)
        width_list = self._frange(0, canvas_width, xsize)
        logic = OthelloGameLogic.OthelloGameLogic(self._rows, self._columns, self._first, self._top, self._win)
        for rspot in range(self._rows):
            for cspot in range(self._columns):
                if (event.x > width_list[cspot]) and (event.x < width_list[cspot+1]) and (event.y > height_list[rspot]) and (event.y < height_list[rspot+1]):
                    if logic.verify_player_move(rspot, cspot, self._turn, self._board):
                        self._flip_list = []
                        self._flip_list = logic.flip_disc(rspot, cspot, self._board, self._turn)
                        if self._turn == 'BLACK':
                            self._board[rspot][cspot] = 'B'
                            for bfr, bfc in self._flip_list:
                                self._board[bfr][bfc] = 'B'
                        elif self._turn == 'WHITE':
                            self._board[rspot][cspot] = 'W'
                            for wfr, wfc in self._flip_list:
                                self._board[wfr][wfc] = 'W'
                        self._turn = logic._opposite_turn(self._turn)
                        self._turn_state.set(self._turn + '\'s turn')
        self._redraw_all_spots()
        black, white = logic._count_black_and_white(self._board)
        self._game_state1.set('BLACK: ' + str(black))
        self._game_state2.set('WHITE: ' + str(white))
        if logic.check_game_win(self._board):
            self._turn_state.set(logic.winning_option(self._board))
        elif logic.check_no_step(self._board):
            print("Failed")
            self._turn_state.set(logic.winning_option(self._board))
        elif logic.black_switch(self._board):
            self._turn = logic._opposite_turn(self._turn)
        elif logic.white_switch(self._board):
            self._turn = logic._opposite_turn(self._turn)
            

    def _redraw_all_spots(self) -> None:
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        xsize = canvas_width / self._columns
        ysize = canvas_height / self._rows
        self._color1 = 'light sky blue'
        self._color2 = 'light green'
        color = self._color2
        for row in range(self._rows):
            color = self._color1 if color == self._color2 else self._color2
            for column in range(self._columns):
                left_top_x = (column * xsize)
                left_top_y = (row * ysize)
                right_buttom_x = left_top_x + xsize
                right_buttom_y = left_top_y + ysize
                self._canvas.create_rectangle(left_top_x, left_top_y, right_buttom_x, right_buttom_y, outline="black", fill=color, tags="square")
                color = self._color1 if color == self._color2 else self._color2
        height_list = self._frange(0, canvas_height, ysize)
        width_list = self._frange(0, canvas_width, xsize)
        for rspot in range(self._rows):
            for cspot in range(self._columns):
                center_x = (2*width_list[cspot] + xsize)/2
                center_y = (2*height_list[rspot] + ysize)/2
                radius_x = xsize/4
                radius_y = ysize/4
                if self._board[rspot][cspot] == 'B':
                    self._canvas.create_oval(center_x - radius_x, center_y - radius_y, center_x + radius_x, center_y + radius_y, fill = 'black', outline = 'black')
                elif self._board[rspot][cspot] == 'W':
                    self._canvas.create_oval(center_x - radius_x, center_y - radius_y, center_x + radius_x, center_y + radius_y, fill = 'white', outline = 'white')
                cspot += 1
            rspot += 1

    def _frange(self, ini: float, fin: float, size: float) -> list:
        float_list = []
        while ini <= fin:
            float_list.append(ini)
            ini += size
        return float_list
    
    def _was_replay_clicked(self) -> bool:
        return self._replay_clicked

    def _was_exit_clicked(self) -> bool:
        return self._exit_clicked

    def _on_replay_button(self) -> None:
        self._replay_clicked = True
        self._gameboard.destroy()

    def _on_exit_button(self) -> None:
        self._gameboard.destroy()

    def _turn_side_string(self, first: str) -> str:
        if (first == 'B') or (first == 'BLACK'):
            return 'BLACK'
        elif (first == 'W') or (first == 'WHITE'):
            return 'WHITE'

    def gameStart(self) -> None:
        self._gameboard.grab_set()
        self._gameboard.wait_window()

class OthelloGame:
    def __init__(self):
        self._starting_interface = tkinter.Tk()
        create_button = tkinter.Button(master = self._starting_interface, text = 'Create', font = DEFAULT_FONT, command = self._on_create)
        create_button.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = tkinter.N)
        
        self._system_info = tkinter.StringVar()
        self._system_info.set('Welcome to Othello Game!')
        system_info_label = tkinter.Label(master = self._starting_interface, textvariable = self._system_info, font = DEFAULT_FONT)
        system_info_label.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)

        self._system_info = tkinter.StringVar()
        self._system_info.set('No game is created yet!')
        system_info_label = tkinter.Label(master = self._starting_interface, textvariable = self._system_info, font = DEFAULT_FONT)
        system_info_label.grid(row = 2, column = 0, padx = 0, pady = 0, sticky = tkinter.NSEW)
        
        self._starting_interface.rowconfigure(0, weight = 1)
        self._starting_interface.rowconfigure(1, weight = 1)
        self._starting_interface.rowconfigure(2, weight = 1)
        self._starting_interface.columnconfigure(0, weight = 1)

    def start(self) -> None:
        self._starting_interface.mainloop()
    
    def _on_create(self) -> None:
        interface = CreatingOthelloGUI()
        interface.show()
        if interface.was_ok_clicked():
            rows = interface.get_rows()
            rows = self._convert_str_to_int(rows)
            columns = interface.get_columns()
            columns = self._convert_str_to_int(columns)
            first = interface.get_first().upper()
            top = interface.get_top().upper()
            win = interface.get_win()
            win = self._convert_str_to_int(win)

            if rows not in [4, 6, 8, 10, 12, 14, 16]:
                self._system_info.set('Rows: Please enter an even number between [4] and [16].')
            elif columns not in [4, 6, 8, 10, 12, 14, 16]:
                self._system_info.set('Columns: Please enter an even number between [4] and [16].')
            elif first not in ['B', 'BLACK', 'W', 'WHITE']:
                self._system_info.set('First player: Please enter [B]lack or [W]hite.')
            elif top not in ['B', 'BLACK', 'W', 'WHITE']:
                self._system_info.set('Top-left: Please enter [W]hite or [B]lack.')
            elif win not in [1, 2]:
                self._system_info.set('Win option: Please enter [1] or [2] to preform winning method.')
            else:
                self._system_info.set('A game is created!')
                board = OthelloGameboard(rows, columns, first, top, win)
                board.gameStart()
                if board._was_replay_clicked():
                    self._system_info.set('No game is created yet!')
                    self._on_create()
                elif board._was_exit_clicked():
                    self._system_info.set('No game is created yet!')

    def _convert_str_to_int(self, num: str) -> int:
        if num == '1':
            return 1
        elif num == '2':
            return 2
        elif num == '4':
            return 4
        elif num == '6':
            return 6
        elif num == '8':
            return 8
        elif num == '10':
            return 10
        elif num == '12':
            return 12
        elif num == '14':
            return 14
        elif num == '16':
            return 16
            
if __name__ == '__main__':
    OthelloGame().start()
