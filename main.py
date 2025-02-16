import pygame
from constants import *
from player import Player 

def main():
    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

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
