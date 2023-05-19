class Action:
    def __init__(self, coordinates : tuple, mark : str) -> None:
        self.cooordinates = coordinates
        self.mark = mark

class Constraint():
    def __init__(self, value) -> None:
        self.value = value
        self.intersections = 0

    def __repr__(self) -> str:
        return str(self.value)

class Board:
    def __init__(self) -> None:
        self.grid = list()
        self.constraints = list()
        self.to_move = "/"
        self.score = 0

    def initialize(self, filepath):
        with open(filepath, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip().split(" ")

                constraint_line = list()
                for elem in line:
                    if elem == "*":
                        constraint_line.append(Constraint(-1))
                    else:
                        constraint_line.append(Constraint(int(elem)))
            
                self.constraints.append(constraint_line)
            size = len(self.constraints) - 1
            self.grid = [["" for _ in range(size)] for _ in range(size)]

    def new(self, action : Action):
        new_board = Board()
        new_board.grid = self.grid
        new_board.constraints = self.constraints

        x, y = action.cooordinates
        new_board.grid[x][y] = action.mark

        return new_board
    

    
    def __repr__(self) -> str:
        representation = ""

        for line in self.grid:
            representation += "|" + str(line) +"|" + "\n"
        
        representation += "\n"
        for line in self.constraints:
            representation += "|" + str(line) +"|" + "\n"
        
        return representation

