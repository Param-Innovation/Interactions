import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Smoke')

# Set up the clock
clock = pygame.time.Clock()

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the smoke variables
smoke_particles = []
max_particles = 100
particle_size = 5
particle_lifetime = 5
particle_speed = 5

# Create the Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = particle_size
        self.color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
        self.lifetime = particle_lifetime
        self.speed = particle_speed
        self.angle = random.uniform(0, 2 * 3.14)
        
        self.x_vel = self.speed * math.cos(self.angle)
        self.y_vel = self.speed * math.sin(self.angle)

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.lifetime -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # Add new particles
            x, y = event.pos
            for i in range(max_particles):
                smoke_particles.append(Particle(x, y))

    # Update particles
    for particle in smoke_particles:
        particle.update()
        if particle.lifetime <= 0:
            smoke_particles.remove(particle)

    # Draw the screen
    screen.fill(black)
    for particle in smoke_particles:
        particle.draw(screen)

    # Update the screen
    pygame.display.update()

    # Set the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
