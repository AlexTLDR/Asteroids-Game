import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rotation = 0

    def triangle(self):
        center = pygame.Vector2(self.radius, self.radius)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]

    def draw(self):
        self.image.fill((0,0,0,0))
        pygame.draw.polygon(self.image, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.rect.center = self.position
        self.draw()
          # Wrap around the screen
            # Horizontal wrapping
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        # Vertical wrapping
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_start_pos = self.position + forward * self.radius
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        Shot(shot_start_pos.x, shot_start_pos.y, shot_velocity)

