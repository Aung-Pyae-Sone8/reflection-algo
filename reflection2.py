import matplotlib.pyplot as plt

# Prompt the user to input the vertices of the triangle
print("Enter the coordinates of the three vertices of the triangle (x, y) separated by commas:")

# Get input for the vertices
triangle_vertices = []
for i in range(3):
    x, y = map(float, input(f"Enter the coordinates of vertex {i + 1}: ").split(','))
    triangle_vertices.append((x, y))

# Append the first vertex to close the triangle
triangle_vertices.append(triangle_vertices[0])

# Create a new plot
plt.figure()

# Draw original triangle
plt.plot([vertex[0] for vertex in triangle_vertices], [vertex[1] for vertex in triangle_vertices], 'r-')

# Reflect triangle across x-axis
reflected_x_triangle = [(x, -y) for x, y in triangle_vertices]
plt.plot([vertex[0] for vertex in reflected_x_triangle], [vertex[1] for vertex in reflected_x_triangle], 'b-')

# Reflect triangle across y-axis
# reflected_y_triangle = [(-x, y) for x, y in triangle_vertices]
# plt.plot([vertex[0] for vertex in reflected_y_triangle], [vertex[1] for vertex in reflected_y_triangle], 'g-')

# Plot vertices with color
plt.plot(*zip(*triangle_vertices), marker='o', color='r', markersize=8, linestyle='None')
plt.plot(*zip(*reflected_x_triangle), marker='o', color='b', markersize=8, linestyle='None')
# plt.plot(*zip(*reflected_y_triangle), marker='o', color='g', markersize=8, linestyle='None')

# Set axis limits and labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
# plt.legend(['Original', 'Reflection across x-axis', 'Reflection across y-axis'])

# Show plot
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Triangle Reflection')
plt.show()
