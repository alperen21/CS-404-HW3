import copy 
from board.Board import Board
from game.SlantGame import SlantGame

def main():
    game = SlantGame()
    board = Board()
    board.initialize("input/input.txt")
    

if __name__ == "__main__":
    main()