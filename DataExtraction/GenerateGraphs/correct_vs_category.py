import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Load the CSV file into a DataFrame
df = pd.read_csv("../ConvertJSON/user_data.csv")

# used as a count for the correct column
correctAdd = df.groupby("Category")["Correct"].value_counts().unstack(fill_value=0)

# bar width when it is split for incorrect and correct
bar_width = 0.3

# separating the counts for true or false to differentiate between them in the bar graph
categories = correctAdd.index
correct = correctAdd[True]
incorrect = correctAdd[False]

x = np.arange(len(categories))


plt.figure(figsize=(10, 6))
plt.bar(
    x - bar_width / 2, correct, bar_width, label="Correct", color="green", alpha=0.7
)
plt.bar(
    x + bar_width / 2, incorrect, bar_width, label="Incorrect", color="red", alpha=0.7
)

# label titles
plt.xlabel("Correct/False")
plt.ylabel("Category")
plt.title("Bar Graph: Correct/Incorrect vs. Catergory")

plt.legend(["Correct", "Incorrect"])
# printing in graph png
plt.savefig("../../WebPage/Graphs/correct-vs-category.png")
