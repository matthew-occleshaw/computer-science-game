from json import loads, dumps


def store_game_state(player):
    try:
        open("game_saves.json", "x")
    except FileExistsError:
        with open("game_saves.json", "rt") as read_file:
            file_contents = read_file.read()
            file_data = loads(file_contents)
    else:
        file_data = []

    game_data = vars(player)
    file_data.append(game_data)
    with open("game_saves.json", "wt"):
        pass
    # TODO Implement game state storage


def retrieve_game_state():
    pass
    # TODO Implement game state retrieval
