import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Balloons")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Balloon class
class Balloon:
    def __init__(self):
        self.color = random.choice([pygame.Color("red"), pygame.Color("blue"), pygame.Color("green"), pygame.Color("yellow"), pygame.Color("purple")])
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + random.randint(50, 150)  # Start below the screen
        self.size = random.randint(20, 50)
        self.speed = random.uniform(1, 3)  # Speed of the balloon moving up

    def move(self):
        self.y -= self.speed  # Balloon moves up

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.size)

# Create a list to hold balloons
balloons = [Balloon() for _ in range(10)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw balloons
    for balloon in balloons:
        balloon.move()
        balloon.draw()
        if balloon.y < -balloon.size:  # If the balloon goes off the screen, reset it to the bottom
            balloon.y = HEIGHT + random.randint(50, 150)
            balloon.x = random.randint(100, WIDTH - 100)

    pygame.display.flip()  # Update the screen
    clock.tick(60)  # Frame rate control
