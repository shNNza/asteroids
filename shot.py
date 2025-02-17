import pygame
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt
        if (self.position.x < 0 or 
            self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or 
            self.position.y > SCREEN_HEIGHT):
            self.kill()