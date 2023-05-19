from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, state, move):
        pass
    
        

def play_game(game, strategies: dict, verbose=False):
    state = game.initial
    while not game.is_terminal(state):
        input()
        player = state.to_move
        move = strategies[player](game, state)
        state = game.result(state, move)
        if verbose: 
            print('Player', player, 'move:', move)
            print(state)
    return state
