# computer-science-game

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple text-based dungeon crawler created for a computer science project

[Plan](https://github.com/matthew-occleshaw/computer-science-game/blob/master/game-plan.md)  
[GitHub Repository](https://github.com/matthew-occleshaw/computer-science-game "Github")  
[To Do List](https://github.com/matthew-occleshaw/computer-science-game/blob/master/game-plan.md)

## To run

### Prerequisites:

- Pipenv
- Python 3.9.\*

Installation instructions for prerequisites on windows:

```bash
$ winget install python --version 3.9.*
$ pip install --user pipenv
```

### To set up project:

```bash
$ git clone https://github.com/mjocc/computer-science-game
$ cd computer-science-game
$ pipenv install
```

### To run:

```bash
$ pipenv run python computer-science-game
```

or

```bash
$ pipenv shell
$ python computer-science-game
```

## Supported file commands

### computer-science-game/leaderboard.py

Supported flags:

- `--reset` - resets the database
- `--get-data` - returns all the data (bar the primary key) from the database as an ASCII art table

### computer-science-game/save_game.py

Supported flags:

- `--reset` - deletes all the game saves from `game_saves.json`
