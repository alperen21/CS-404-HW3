from game.game import Game
from board.Board import Board, Constraint, Action
from copy import deepcopy

class SlantGame(Game):
    # def __init__(self) -> None:
    #     super().__init__(initial)
    
    def actions(self, state, player):
        allowed_actions = []
        for x, row in enumerate(state.grid):
            for y, elem in enumerate(row):
                if elem != "\\" and elem != "/":
                    allowed_actions.append((x,y))
        

        action_objects = list()
        for action in allowed_actions:
            action_objects.append(
                Action(action, player)
            )

        return action_objects

    def result(self, board, action):
        board = self.move(board, action)
        player = board.to_move

        if board.to_move == "/":
            board.to_move = '\\'
        else:
            board.to_move = "/"
        
        board.score = self.score(board, action, player)
        
        return board
    
    def score(self, board : Board, action : Action, player : str):
        score = 0

        x,y = action.cooordinates
        action_mark = action.mark
        affected_coordinates = list()

        if action_mark == "/":
            affected_coordinates.append((x,y+1))
            affected_coordinates.append((x+1,y))
        else:
            affected_coordinates.append((x+1,y+1))
            affected_coordinates.append((x,y))
        
        for coordinate in affected_coordinates:
            x,y = coordinate

            if board.constraints[x][y].value == board.constraints[x][y].intersections + 1:
                score += board.constraints[x][y].value
        
        if player == "\\":
            score = (-1) * score

        return score

    def move(self, board ,action):
        action_coordinates = action.cooordinates
        action_mark = action.mark
        affected_coordinates = list()
        x,y = action_coordinates
        board.grid[x][y] = action_mark

        if action_mark == "/":
            affected_coordinates.append((x,y-1))
            affected_coordinates.append((x-1,y))
        else:
            affected_coordinates.append((x-1,y-1))
            affected_coordinates.append((x,y))
        
        for coordinate in affected_coordinates:
            x,y = coordinate
            board.constraints[x][y].intersections += 1

        

        return board


    def game_is_over(self, board : Board):
        grid = board.grid

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