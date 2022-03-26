from Director.Director import Director
from Structs.Window import Window

WINDOW = Window(width = 900, height = 600, caption = 'Impossible Pong', fps_cap = 60)

def main():

    game = Director(WINDOW)

    game.run()
    game.close()

if __name__ == "__main__":
    main()