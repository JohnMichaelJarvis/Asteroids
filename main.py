from typing import Any
import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main() -> None:
    pygame.init()
    screen: Any = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Any = pygame.time.Clock()
    print(clock)
    dt: int = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt += clock.tick(60)


if __name__ == "__main__":
    main()
