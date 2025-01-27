import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

# Define vertices and edges for the cube
vertices = [
    (1, 1, -1),   # Top-right-front
    (1, -1, -1),  # Bottom-right-front
    (-1, -1, -1), # Bottom-left-front
    (-1, 1, -1),  # Top-left-front
    (1, 1, 1),    # Top-right-back
    (1, -1, 1),   # Bottom-right-back
    (-1, -1, 1),  # Bottom-left-back
    (-1, 1, 1),   # Top-left-back
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Front face edges
    (4, 5), (5, 6), (6, 7), (7, 4),  # Back face edges
    (0, 4), (1, 5), (2, 6), (3, 7),  # Connecting edges
]

# Function to draw the cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main function to run the cube viewer
def GL_Cube_Window_Render():
    # Initialize Pygame
    pygame.init()
    display = (480, 640) ## GODS CHOSEN RESOLUTION!!!
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Perspective settings
    gluPerspective(65, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)

    # Initialize rotation variables
    x_rotation = 0
    y_rotation = 0

    # Main loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen and reset view
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Update rotation
        x_rotation += 1
        y_rotation += 1

        # Apply rotation and draw the cube
        glPushMatrix()
        glRotatef(x_rotation, 1, 0, 0)  # Rotate around x-axis
        glRotatef(y_rotation, 0, 1, 0)  # Rotate around y-axis
        draw_cube()
        glPopMatrix()

        # Update the display and delay
        pygame.display.flip()
        clock.tick(60)

# Allow this file to be both imported and run directly
if __name__ == "__main__":
    run_cube_viewer()
