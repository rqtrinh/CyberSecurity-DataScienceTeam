import matplotlib.pyplot as plt
import numpy as np

# Generate some random data points
x = np.random.rand(50)
y = np.random.rand(50)

# Index of the point to highlight
highlight_index = 25

# Create a scatter plot of all data points
plt.scatter(x, y, label='Data Points')

# Highlight one point with a different color or marker
plt.scatter(x[highlight_index], y[highlight_index], c='red', marker='o', label='Highlighted Point')

# Add labels and a legend
plt.xlabel('Players')
plt.ylabel('Missed Questions')
plt.title('PIP Plan')
plt.savefig('scatter-graph.png')

# Clear most recent graph
plt.clf()

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 24, 18, 30]

plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Categories Missed')

# Save the plot as an image
plt.savefig('categories-graph.png')