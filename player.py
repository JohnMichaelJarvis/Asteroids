import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation: int = 0

    def triangle(self) -> list[pygame.Vector2]:
        # 1. Define direction vectors
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius / 1.5)

        # 2. Scale forward vector to the radius
        offset_vec = pygame.Vector2(forward * self.radius)

        # 3. Calculate points using standard vector addition/subtraction
        a: pygame.Vector2 = self.position + offset_vec
        b: pygame.Vector2 = self.position - offset_vec - right
        c: pygame.Vector2 = self.position - offset_vec + right

        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

    def move(self, dt: int) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
