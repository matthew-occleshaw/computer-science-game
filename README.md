# computer-science-game

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple text-based dungeon crawler created for a computer science project

[Plan](https://github.com/matthew-occleshaw/computer-science-game/blob/master/game-plan.md)  
[GitHub Repository](https://github.com/matthew-occleshaw/computer-science-game "Github")  
[To Do List (GitHub Project)](https://github.com/matthew-occleshaw/computer-science-game/projects/1)

### To run

1. `pip install --user pipenv`
2. `pipenv install`
3. `python main.py`

### leaderboard.py

Supported flags:

- `--reset` - resets the database
- `--get-data` - prints all the data (bar the primary key) from the database

### save_game.py

Supported flags:

- `--reset` - deletes all the game saves from `game_saves.json`
