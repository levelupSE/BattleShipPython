# BattleShip-Python

Battleship Python is a simple script that automatically generates battleship levels as per your configuration. It even includes a few functions to make it playable.

## How it Works

- First the game's grid is generated using nested lists. Each box/square can be accessed by using BS.grid[Y][X]
 ![Grid](https://drive.google.com/uc?export=view&id=1xUQw9BmmyZPKnm4Vsp5A0Xbtx3vomxdC)
- In order to generate the levels, the rule set below is followed:
- - Create a random X and Y point and check if the point is an empty cell.
 ![RandomPoint](https://drive.google.com/uc?export=view&id=1SUcy-r_DToI3WyGk8fPksg35w5SIX8tR)
- - Iterate through a list of shuffled directions. 
- - In each direction check if the size of the ship fits. If not, repeat step 1.
![SizeCheck](https://drive.google.com/uc?export=view&id=1UpRraxboFfMbADJ6QQ-sOWo6Uw5namcV)
- - If the size fits, use that direction to check if the point is valid by checking if there is no ship in it's path and include the gap/padding if required.
![GapCheck](https://drive.google.com/uc?export=view&id=12fhaJCTLdFIS8MHr8GDx4nrDxBwoZCcD)
- - If all the steps work, it would add the ship to the grid. Else it would repeat the steps until all points have been attempted. Beyond which it would not ignore and not include that ship.
![Done](https://drive.google.com/uc?export=view&id=1wvFFxwilDu4rfS0XGG1pV0FG6IdZAkc4)

## Accessing the Code Class

The BS class has only 2 functions that are usually called by a user.
- ```printGrid(hide=True)```
- ```attackShip(pos)```
- ```shipCount()```

```printGrid(hide=True)``` displays the grid in a neat manner. It takes an optional boolean value. On True it hides the position of every ship. On false, it shows the position of every ship upon printed.
```attackShip(pos)``` takes in the position in the form of HorizontalVertical / "A2" or "B8" and returns True if there is a ship in that position, else returns false.
```shipCount()``` returns the number of ships left

Variables can also be read from the BS Class such as:
```
height (int)
width (int)
gap (int)
direction (list)
gameOver (bool)
ship (list)
shipChar (list)
shipHealth (list)
shipPieces (int)
emptyCell (string)
sunkShip (string)
gridHor (list)
gridVert (list)
grid (list)
```