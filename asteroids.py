import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
      super().__init__(x, y, radius)  # Initialize the parent class (CircleShape)
      self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
      pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)  # Draw the asteroid as a circle with a width of 2

    def update(self, dt):
      self.position += self.velocity * dt # Move the asteroid in a straight line at constant speed