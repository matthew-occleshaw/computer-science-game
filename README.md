# computer-science-game

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Simple text-based dungeon crawler created for a computer science project

[Plan](https://github.com/matthew-occleshaw/computer-science-game/blob/master/game-plan.md)  
[GitHub Repository](https://github.com/matthew-occleshaw/computer-science-game "Github")  
[To Do List](https://github.com/matthew-occleshaw/computer-science-game/blob/master/game-plan.md)

## To run

### Prerequisites:

- Pipenv
- Python 3.9.\*

Installation instructions for prerequisites on Windows:

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
$ pipenv run python -m computer_science_game
```

or

```bash
$ pipenv shell
$ python -m computer_science_game
```

## Supported file commands

### computer_science_game/leaderboard.py

Supported flags:

- `--reset` - resets the database
- `--get-data` - returns all the data (bar the primary key) from the database as an ASCII art table

### computer_science_game/save_game.py

Supported flags:

- `--reset` - deletes all the game saves from `game_saves.json`
