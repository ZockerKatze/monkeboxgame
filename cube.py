import tkinter as tk
import math

def cuberotate():
    # Create the root window
    root = tk.Tk()
    root.title("TkInter-DemTkInter-Demoo")

    # Canvas setup
    canvas = tk.Canvas(root, width=480, height=640, bg="white")
    canvas.pack()

    # Define the cube vertices (a unit cube centered at the origin)
    vertices = [
        [-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
        [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]
    ]

    # Define the edges that connect the vertices
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  # Back face
        (4, 5), (5, 7), (7, 6), (6, 4),  # Front face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
    ]

    # Projection parameters
    center_x, center_y = 240, 320  # Center of the canvas
    scale = 600  # Scaling factor


    # if you dont include this it will crash!
    global angle_x, angle_y

    # Rotation angle
    angle_x = 0
    angle_y = 0


    # Function to rotate the cube
    def rotate_cube():
        global angle_x, angle_y

        # Rotation matrices for X and Y axes
        rotation_matrix_x = [
            [1, 0, 0],
            [0, math.cos(angle_x), -math.sin(angle_x)],
            [0, math.sin(angle_x), math.cos(angle_x)]
        ]

        rotation_matrix_y = [
            [math.cos(angle_y), 0, math.sin(angle_y)],
            [0, 1, 0],
            [-math.sin(angle_y), 0, math.cos(angle_y)]
        ]

        # Apply rotation and projection
        rotated_vertices = []
        for vertex in vertices:
            # Apply rotation on X axis
            rotated_x = rotation_matrix_x[0][0] * vertex[0] + rotation_matrix_x[0][1] * vertex[1] + rotation_matrix_x[0][2] * vertex[2]
            rotated_y = rotation_matrix_x[1][0] * vertex[0] + rotation_matrix_x[1][1] * vertex[1] + rotation_matrix_x[1][2] * vertex[2]
            rotated_z = rotation_matrix_x[2][0] * vertex[0] + rotation_matrix_x[2][1] * vertex[1] + rotation_matrix_x[2][2] * vertex[2]

            # Apply rotation on Y axis
            temp_x = rotated_x
            rotated_x = rotation_matrix_y[0][0] * temp_x + rotation_matrix_y[0][2]  * rotated_z
            rotated_z = rotation_matrix_y[2][0] * temp_x + rotation_matrix_y[2][2] * rotated_z

            # Project onto 2D plane (perspective projection)
            projected_x = rotated_x / (rotated_z + 5) * scale + center_x
            projected_y = rotated_y / (rotated_z + 5) * scale + center_y

            rotated_vertices.append((projected_x, projected_y))

        # Clear the canvas
        canvas.delete("all")

        # Draw edges
        for edge in edges:
            x1, y1 = rotated_vertices[edge[0]]
            x2, y2 = rotated_vertices[edge[1]]
            canvas.create_line(x1, y1, x2, y2)

        # Update the rotation angles
        angle_x += 0.01
        angle_y += 0.01

        # Call the function again to create an animation effect
        canvas.after(5, rotate_cube)

    # Start rotating the cube
    rotate_cube()

    # Run the Tkinter event loop
    root.mainloop()

    ## check if app running if not destroy
    ## this does not work for multiple running threads?


    while root.mainloop() == True:
        pass
    else:
        root.destroy()
