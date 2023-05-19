import copy 
from board.Board import Board
from game.SlantGame import SlantGame
from game.Play import play_game
from player.strategy.alpha_beta import search
from player.strategy.human import human
from player.Player import player

def main():
    game = SlantGame()
    board = Board()
    board.initialize("input/input.txt")

    # action = game.actions(board, "/")[0]
    # print(action.cooordinates)
    # print(game.result(board, action))
    strategy = {
        "/": player(human, "/"),
        "\\": player(search, "\\")
    }
    play_game(game, strategy, board).score


if __name__ == "__main__":
    main()