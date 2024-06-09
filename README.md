# Moving Car Simulation with OpenGL
# Overview
This project is a graphical simulation using OpenGL that features moving cars, a plane, and dynamic clouds in a cityscape. The program allows for the interaction with the scene via keyboard inputs to control traffic lights and switch between day and night modes.

# Features
Moving Cars: Three cars move across the screen. Their motion can be stopped and started based on traffic light signals.
Dynamic Plane: A plane moves across the screen during the "morning" state.
Cloud Animation: Clouds move continuously across the screen during the "morning" state.
Day/Night Mode: The scene can switch between morning and night settings, altering the colors and states of objects.
Traffic Light Control: Traffic lights can be toggled between red and green, affecting the movement of cars.

# Requirements
Python 3.x
OpenGL libraries (PyOpenGL, PyOpenGL_accelerate)
PIL (Python Imaging Library)
pygame
numpy

# Installation

Install Python packages: pip install PyOpenGL PyOpenGL_accelerate pillow pygame numpy
Download the texture file: Ensure you have the home.jpg texture file in the same directory as your script.

# Controls
'r' Key: Set traffic lights to red, stopping all cars.
'g' Key: Set traffic lights to green, allowing cars to move.
'w' Key: Switch to morning mode.
'b' Key: Switch to night mode.


# Code Structure

# Initialization
myInit(): Initializes the OpenGL environment, sets up the 2D orthographic view, and loads textures.

# Drawing Functions
draw_buliding_tex(x1, y1, x2, y2, x3, y3, x4, y4): Draws a textured building.
draw_quad(a, b, c, d, e, f, g, h, i, j, k): Draws a colored quadrilateral.
draw_polygon(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s): Draws a colored polygon with up to 7 vertices.
draw_triangle(a, b, c, d, e, f, g, h, i): Draws a colored triangle.
draw_circle(a, b, c, d, e, f): Draws a filled circle.

# Update Functions
update_cars(): Updates the position of the cars based on their current state.
update_plane(): Updates the position of the plane based on the current time of day.
update_clouds(): Updates the position of the clouds.
Keyboard Function
keyboard(key, x, y): Handles keyboard input to control the traffic light and switch between day and night modes.

# Display Function
display(): Renders the entire scene, including the sky, street, buildings, trees, sun, clouds, plane, cars, and traffic light.

# Idle Function
idle(): Continuously updates the scene and triggers redisplay.

# Notes
Ensure that all necessary libraries and the texture file are available in the correct paths before running the script.
The window created by the script is sized at 1500x750 pixels.
Enjoy the simulation and feel free to modify and expand the code to add more features or improve the existing ones! 
