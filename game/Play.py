from game.SlantGame import SlantGame
from board.Board import Board

def play_game(game : SlantGame, strategies : dict,  board : Board):
    state = board

    while(not game.game_is_over(board)):
        player = state.to_move
        move = strategies[player](game, state)
        state = game.result(state, move)
        
        print('Player', player, 'move:', move)
        print(state)
        
    return state

