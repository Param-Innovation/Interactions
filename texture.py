import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the cloth mesh parameters
cloth_width = 100
cloth_height = 100
cloth_spacing = 4
cloth_points = []

# Create the cloth mesh points
for i in range(cloth_width):
    for j in range(cloth_height):
        x = i * cloth_spacing
        y = j * cloth_spacing
        cloth_points.append((x, y))

# Set the cloth mesh constraints
cloth_constraints = []
for i in range(cloth_width):
    for j in range(cloth_height):
        if i < cloth_width - 1:
            cloth_constraints.append((i * cloth_height + j, (i+1) * cloth_height + j))
        if j < cloth_height - 1:
            cloth_constraints.append((i * cloth_height + j, i * cloth_height + j + 1))

# Start the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the cloth mesh
    for i, point in enumerate(cloth_points):
        x, y = point
        pygame.draw.circle(screen, BLACK, (x, y), 2)

    # Apply the mouse forces to the cloth mesh
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        for i, point in enumerate(cloth_points):
            x, y = point
            dx = mouse_pos[0] - x
            dy = mouse_pos[1] - y
            dist = (dx**2 + dy**2)**0.5
            if dist < 50:
                cloth_points[i] = (x + dx*0.1, y + dy*0.1)

    # Apply the cloth mesh constraints
    for i, constraint in enumerate(cloth_constraints):
        p1, p2 = constraint
        x1, y1 = cloth_points[p1]
        x2, y2 = cloth_points[p2]
        dx = x2 - x1
        dy = y2 - y1
        dist = (dx**2 + dy**2)**0.5
        diff = (dist - cloth_spacing) / dist
        if diff > 0:
            x1 += dx * 0.5 * diff
            y1 += dy * 0.5 * diff
            x2 -= dx * 0.5 * diff
            y2 -= dy * 0.5 * diff
        cloth_points[p1] = (x1, y1)
        cloth_points[p2] = (x2, y2)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
