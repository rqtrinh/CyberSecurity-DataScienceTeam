import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv("../ConvertJSON/user_data.csv")

# Get a list of unique users
unique_users = df['User'].unique()

# Set up subplots
fig, axs = plt.subplots(nrows=len(unique_users), figsize=(10, 6 * len(unique_users)), sharex=True)

# Loop through each user and create a scatter plot
for i, user in enumerate(unique_users):
    user_data = df[df['User'] == user]
    colors = np.where(user_data['Correct'] == True, 'green', 'red')  # Green for correct, red for incorrect

    axs[i].scatter(user_data['SecondsTakenToAnswer'], user_data['Correct'], c=colors, alpha=0.7)

    # Set labels and title
    axs[i].set_xlabel('Seconds Taken to Answer')
    axs[i].set_ylabel('Correctness (True/False)')
    axs[i].set_title(f'Scatter Plot: Time vs. Correctness - User {user}')

    # Display a legend
    axs[i].legend(['Correct', 'Incorrect'])

# Adjust layout for better spacing
# plt.tight_layout()

# Show the plot
# plt.show()

plt.savefig('../../WebPage/Graphs/time-taken-vs-correctness.png')