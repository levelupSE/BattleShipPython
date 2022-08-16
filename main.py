from os import system, name

from BattleShipGame import BS

if __name__ == '__main__':
    def clear():
       # for windows
       if name == 'nt':
          _ = system('cls')

       # for mac and linux
       else:
          _ = system('clear')

    game = BS()
    game.printGrid()
    while game.gameOver == False:
        pos = input("Input Position (eg: A0): ")
        if pos.lower() == "show":
            clear()
            print("Ships Left:", game.shipCount())
            game.printGrid(False)
        else:

                clear()
                print([pos[0].capitalize(),pos[1]])
                if game.attackShip([pos[0].capitalize(),pos[1]]):
                    print("HIT!")
                else:
                    print("Miss!")
                print("Ships Left:", game.shipCount())
                game.printGrid()


    print("Game Over")
