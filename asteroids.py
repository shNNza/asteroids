import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
      super().__init__(x, y, radius)  # Initialize the parent class (CircleShape)

    def draw(self, screen):
      pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)  # Draw the asteroid as a circle with a width of 2

    def update(self, dt):
      self.position += self.velocity * dt # Move the asteroid in a straight line at constant speed

    def split(self): # asteroid spilting method once shot
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vel_1 = self.velocity.rotate(random_angle)
            new_vel_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = (new_vel_1 * 1.2)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = (new_vel_2 * 1.2)  