from BattleShipGame import BS
from os import name, system

if __name__ == '__main__':
    game = BS()
    game.printGrid()

    for c in range(65, 75):
        for i in range(0, 10):
            pos = [chr(c), str(i)]
            print(''.join(pos))
            game.attackShip(pos)

            if (game.gameOver):
                break
    print('Game Over')
