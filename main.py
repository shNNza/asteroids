import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    # Set static containers for AsteroidField class (only updatable)
    AsteroidField.containers = (updatable,)

    # Create an AsteroidField object
    asteroid_field = AsteroidField()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Kyle's Asteroids Game")

    # Player Instance intialization
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    running = True
    while running:
        # Handle events (e.g., quitting the game)
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)  # Update Player Movement

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black
        for obj in drawable:
            obj.draw(screen)

        # Refresh the display
        pygame.display.flip()

    # Quit pygame when the loop ends
    pygame.quit()
   
if __name__ == "__main__":
    main()
