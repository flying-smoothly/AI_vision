import matplotlib.pyplot as plt

# Define the x-axis (module labels) and y-axis (course names)
module_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
course_names = ['Course1', 'Course2', 'Course3', 'Course4', 'Course5', 'Course6', 'Course7', 'Course8']

# Define the data points for each track
# Format: (module index, course index)
wireless_comm_multimedia = [(0, 2), (2, 4), (4, 6)]
intelligent_semiconductor = [(1, 1), (3, 3), (5, 5)]
fused_electronics = [(0, 0), (2, 2), (4, 4)]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter([x[0] for x in wireless_comm_multimedia], [x[1] for x in wireless_comm_multimedia], color='orange', label='Wireless Communication Multimedia')
plt.scatter([x[0] for x in intelligent_semiconductor], [x[1] for x in intelligent_semiconductor], color='red', label='an intelligent semiconductor')
plt.scatter([x[0] for x in fused_electronics], [x[1] for x in fused_electronics], color='yellow', label='fused electronics')

# Set the x and y axis labels
plt.xticks(range(len(module_labels)), module_labels)
plt.yticks(range(len(course_names)), course_names)

# Add title and legend
plt.title('Track completion condition')
plt.legend(loc='upper right')

# Show the plot
plt.grid(True)
plt.show()

