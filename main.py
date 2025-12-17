import pygame
from typing import Any
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


def main() -> None:
    # pygame setup
    pygame.init()
    screen: Any = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Any = pygame.time.Clock()
    running = True
    dt: int = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
