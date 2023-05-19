import copy 
from board.Board import Board
from game.SlantGame import SlantGame

def main():
    game = SlantGame()
    board = Board()
    board.initialize("input/input.txt")

    action = game.actions(board, "/")[0]
    print(action.cooordinates)
    print(game.result(board, action))


if __name__ == "__main__":
    main()