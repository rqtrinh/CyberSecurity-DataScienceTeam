import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv("../ConvertJSON/user_data.csv")

# Scatter plot for Time vs. Correctness
plt.figure(figsize=(10, 6))
colors = np.where(df['Correct'] == True, 'green', 'red')  # Green for correct, red for incorrect

plt.scatter(df['SecondsTakenToAnswer'], df['Correct'], c=colors, alpha=0.7)

# Set labels and title
plt.xlabel('Seconds Taken to Answer')
plt.ylabel('Correctness (True/False)')
plt.title('Scatter Plot: Time vs. Correctness')

# Display a legend
plt.legend(['Correct', 'Incorrect'])

# Show the plot
# plt.show()

# Save the plot as an image
plt.savefig('../../WebPage/Graphs/time-taken-vs-correctness-users.png')