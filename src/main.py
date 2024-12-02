import sys

import pygame

from game_engine import Clock, EventQueue, GameLogic, GameLoop, GameState
from renderer import Renderer


def main():
    width: int = 1280
    height: int = 720
    display: pygame.Surface = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Gem Poacher")
    pygame.mouse.set_visible(False)

    game_state: GameState = GameState(width, height)
    game_logic: GameLogic = GameLogic(game_state)
    clock: Clock = Clock()
    event_queue = EventQueue()

    pygame.font.init()
    renderer: Renderer = Renderer(display, game_state)
    game_loop: GameLoop = GameLoop(game_logic, renderer, clock, event_queue)

    pygame.init()
    game_loop.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
