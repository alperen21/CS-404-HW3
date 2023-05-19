def player(search_algorithm, player):
    return lambda game, state: search_algorithm(game, state, player)[1]