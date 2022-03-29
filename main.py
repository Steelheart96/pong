from operator import sub, add

from Director.Director import Director
from Structs.Window import Window
import pyray as pr

WINDOW = Window(width = 900, height = 600, caption = 'Impossible Pong', fps_cap = 60)

PLAYER_KEYS_WORDS = {
        pr.KEY_W: sub,
        pr.KEY_S: add
        }

PLAYER_KEYS_ARROWS = {
        pr.KEY_UP: sub,
        pr.KEY_DOWN: add
        }


def main():

    game = Director(WINDOW, PLAYER_KEYS_WORDS)

    game.run()
    game.close()

if __name__ == "__main__":
    main()