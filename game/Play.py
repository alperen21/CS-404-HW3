from game.SlantGame import SlantGame
from board.Board import Board
from copy import deepcopy

def play_game(game : SlantGame, strategies : dict,  state : Board):

    while(not game.game_is_over(state)):
        player = state.to_move
        temp_state = deepcopy(state)
        move = strategies[player](game, state)
        state = game.result(temp_state, move)
        
        print('Player', player, 'move:', move)
        print(state)

    first_player_win = game.win(state, "/")
    second_player_win = game.win(state, "\\")

    if not first_player_win and not second_player_win:
        print("game ended with a tie")
    elif first_player_win:
        print("first player (/) won")
    else:
        print("second player (\\) won")

    return state

