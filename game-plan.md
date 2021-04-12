# Game Plan

[![](https://repl.it/badge/github/matthew-occleshaw/computer-science-game)](https://repl.it/@ConspiracyTheor/Computer-Science-Game "repl.it")  

[TOC]

## Instructions

- Create a game (could be text or graphics based) which has the following:
- A character which you are able to move between rooms
- This character has the following attributes:
	- Health
	- Speed
	- Attack
- A backpack which can store up to 3 items (there has to be a mechanism to check -  whether it is full before you pick another item up)
- These rooms are linked to each other
- These rooms can contain:
	- Enemies
	- Locked Doors which require a key
	- Items that can help the adventurer along their quest (improve their attributes/keys)
	- Have a clear end circumstance which results in win/lose

## Rooms

```mermaid
graph BT
    1 --> 2
    2 --> 3
    2 --> 4
    3 --> 5
    4 --> 6
    4 --> 7
    5 --> 8
    6 --> 8
    7 --> 8
    8 --> 9
```

| Room Number | Basic Enemies | Normal Enemies | Hard Enemies |         Items          |
| :---------: | :-----------: | :------------: | :----------: | :--------------------: |
|      1      |       1       |                |              |          Key           |
|      2      |       3       |                |              | Apple, Upgrade Station |
|      3      |       1       |       1        |              |      Health Pack       |
|      4      |       1       |       1        |              |      Health Pack       |
|      5      |       1       |                |      1       |                        |
|      6      |       1       |                |      1       |                        |
|      7      |       1       |                |      1       |                        |
|      8      |               |       2        |      1       |                        |
|      9      |               |   Boss Fight   |              |                        |

## Item / Character Stats and Upgrades

- Apple - restores 15 health
- Key - unlocks doors
- Upgrade station - allows for the upgrade of any of the key attributes

## Enemy Classes

| Enemy Class | Health | Speed | Attack |
| :---------: | :----: | :---: | :----: |
|    Basic    |   15   |  35   |   5    |
|   Normal    |   25   |  50   |   10   |
|    Hard     |   35   |  65   |   15   |
|    Boss     |   75   |  100  |   25   |

## Program Flow

### More abstract

1. Enter room
2. Fight enemies
3. Pick up items in room
4. Use items
5. Pick and then move on to next room

### More detailed

1.  1. USERINPUT: pick room (not on first iteration)
    2. Update Player object to be in chosen room
2.  1. Announce one enemy (e.g. 'A Basic Enemy jumps out')
    2. USERINPUT: what does player want to do
    3. Execute their choice
    4. Inform the users of the changes caused by their choice
    5. Repeat steps 2.2 to 2.4 until player or enemy is dead
    6. Repeat steps 2.1 to 2.5 for each enemy
3.  1. 

## Expected Output

```
You enter room 1
A Basic Enemy jumps out
What would you like to do
ATTACK (1) or USE AN ITEM (2): 1
You vanquished the enemies!
You look around the room... [few second wait]
You find:
1   Apple
2   Upgrade Station
3   Key
You pick up object(s) (type number(s); seperate with forward slashes): 1/2/3
You use object 
```