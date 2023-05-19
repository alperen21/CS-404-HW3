from game.game import Game
from board.Board import Board, Constraint, Action

class SlantGame(Game):
    # def __init__(self) -> None:
    #     super().__init__(initial)
    
    def actions(self, state):
        allowed_actions = []
        for x, row in enumerate(state.grid):
            for y, elem in row:
                if elem != "\\" and elem != "/":
                    allowed_actions.append((x,y))
        
        return allowed_actions

    def result(self, board, action):
        board = board.new(action)
        player = board.to_move
        board.to_move = '\\' if player == "/" else '\\'
        
        board.score = self.score(board, action)
        board = self.move(board, action)
        
        return board
    def score(board : Board, action : Action):
        score = 0

        x,y = action.cooordinates
        action_mark = action.mark
        affected_coordinates = list()

        if action_mark == "/":
            affected_coordinates.append((x,y-1))
            affected_coordinates.append((x-1,y))
        else:
            affected_coordinates.append((x-1,y-1))
            affected_coordinates.append((x,y))
        
        for coordinate in affected_coordinates:
            x,y = coordinate

            if board.constraints[x][y].value + 1 == board.constraints[x][y].intersection:
                score += board.constraints[x][y].value
        
        return score

    def move(board ,action):
        action_coordinates = action.cooordinates
        action_mark = action.mark
        affected_coordinates = list()
        x,y = action_coordinates

        if action_mark == "/":
            affected_coordinates.append((x,y-1))
            affected_coordinates.append((x-1,y))
        else:
            affected_coordinates.append((x-1,y-1))
            affected_coordinates.append((x,y))
        
        for coordinate in affected_coordinates:
            x,y = coordinate
            board.constraints[x][y].intersection += 1

        board.grid[x][y] = action_mark


    def game_is_over(self, board : Board):
        grid = self.board.grid

        for row in grid:
            for elem in row:
                if elem == '':
                    return False 
        return True

    def win(self, board : Board, player : str):
        if not self.game_is_over(board):
            return False
        
        if board.score == 0:
            return False
        
        if player == "/":
            return board.score > 0
        else:
            return board.score < 0