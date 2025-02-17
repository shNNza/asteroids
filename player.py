from circleshape import CircleShape   # Assuming CircleShape is in circleshape.py
from shot import Shot
from constants import PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_RADIUS

import pygame

class Player(CircleShape):
    def __init__(self, position, shots):
         # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        # Call the parent class's constructor
        super().__init__(position.x, position.y, PLAYER_RADIUS)
        self.shots = shots
        self.rotation = 0
        self.direction = pygame.Vector2(0, -1)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.direction = pygame.Vector2(0, -1).rotate(-self.rotation)

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
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_velocity = self.direction * PLAYER_SHOOT_SPEED # Create a new shot at the player's position
        new_shot = Shot(self.position, shot_velocity)
        self.shots.add(new_shot)

    def handle_input(self, pressed_keys):
        if pressed_keys[pygame.K_SPACE]:
            self.shoot()  