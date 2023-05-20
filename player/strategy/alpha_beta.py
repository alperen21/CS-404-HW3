from game.SlantGame import SlantGame
from board.Board import Board
import math

def min_value(game : SlantGame, state : Board, alpha : int, beta : int, player : str):
    if game.game_is_over(state):
        return state.utility(state, player), None

    v = -math.inf
    move = None

    for action in game.actions(state, player):
        v2, _ = max_value(game, game.result(state, action), alpha, beta, player)
        if v2 < v:
            v, move = v2, action
            alpha = min(alpha, v)
        if v <= beta:
            return v, move
    return v, move

def max_value(game : SlantGame, state : Board, alpha : int, beta : int, player : str):
    if game.game_is_over(state):
        return state.utility(state, player), None#state.score, None

    v = -math.inf
    move = None

    for action in game.actions(state, player):
        v2, _ = min_value(game, game.result(state, action), alpha, beta, player)
        if v2 > v:
            v, move = v2, action
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def search(game : SlantGame, state : Board, player : str):
    return max_value(game, state, -math.inf, math.inf, player)

def player(search_algorithm):
    return lambda game, state: search_algorithm(game, state)[1]
