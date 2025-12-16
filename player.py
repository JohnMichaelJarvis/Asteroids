import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation: int = 0

    def triangle(self) -> list[float]:
        forward: float = pygame.Vector2(0, 1).rotate(self.rotation)
        right: float = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a: float = self.position + forward * self.radius
        b: float = self.position - forward * self.radius - right
        c: float = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
