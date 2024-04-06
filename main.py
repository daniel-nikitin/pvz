import arcade

from Game import Game

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PVZ"


def main():
    """ Main function """
    Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
