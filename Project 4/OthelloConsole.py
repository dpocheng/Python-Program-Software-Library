## Pok On Cheng 74157306. ICS 32 Lab 1 Project 4.

import OthelloGameLogic

def game_start():
    game_logic = OthelloGameLogic.Othello_Game_Logic()
    game_state = []
    turn = ""
    game_state, turn = game_logic.creating_new_game_board()
    while True:
        row, column = game_logic.make_a_move(game_state, turn)
        flip_list = []
        flip_list = game_logic.flip_disc(row, column, game_state, turn)
        if turn == "BLACK":
            game_state[row][column] = " B "
            for bfr, bfc in flip_list:
                game_state[bfr][bfc] = " B "
            turn = game_logic._opposite_turn()
        elif turn == "WHITE":
            game_state[row][column] = " W "
            for wfr, wfc in flip_list:
                game_state[wfr][wfc] = " W "
            turn = game_logic._opposite_turn()
        game_logic.display_game_board(game_state, turn)
        if game_logic.black_switch(game_state) and turn == "BLACK":
            turn = game_logic._opposite_turn()
            game_logic.display_game_board(game_state, turn)
        if game_logic.white_switch(game_state) and turn == "WHITE":
            turn = game_logic._opposite_turn()
            game_logic.display_game_board(game_state, turn)
        if game_logic.check_no_step(game_state):
            turn = game_logic.winning_option()
            game_logic.display_winner(game_state, turn)
            if replay():
				game_start()
			else:
				break
        if game_logic.check_game_win(game_state):
            turn = game_logic.winning_option()
            game_logic.display_winner(game_state, turn)
            if replay():
				game_start()
			else:
				break

def replay() -> bool:
    while True:
        answer = input("Do you want to play again?")
        answer = answer.upper()
        if answer == "NO" or answer == "N":
            return False
        elif answer == "YES" or answer == "Y":
            return True
        else:
            print("Wrong answer! So you have to play again. LOL")
            return True

if __name__ == "__main__":
    game_start()
