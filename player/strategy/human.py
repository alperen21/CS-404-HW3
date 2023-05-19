from game.SlantGame import SlantGame
from board.Board import Board
import math


def human(game : SlantGame, state : Board, player : str):
    print(state)
    print("available actions:")
    actions = game.actions(state, player)
    actions_dict = dict()
    index = 1

    for action in actions:
        actions_dict[index] = action
        index += 1
    
    for key in actions_dict.keys():
        print(key, "->", actions_dict[key].cooordinates)

    try:
        key = int(input("please select an action: "))
        return None, actions_dict[key]
    except Exception:
        print("invalid selection")
        return human(game, state, player)
