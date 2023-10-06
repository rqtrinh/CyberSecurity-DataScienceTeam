import matplotlib.pyplot as plt
import pandas as pd
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Specify the relative path to the CSV file
csv_file_path = os.path.join(script_dir, "..", "ConvertJSON", "user_data.csv")

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
# Create a folder to save pie charts
import os
if not os.path.exists("pie_charts"):
    os.makedirs("pie_charts")

# 1. Category Distribution
category_counts = df['Category'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Category Distribution')
plt.savefig('pie_charts/category_distribution.png')
plt.clf()

# 2. User Performance (Combined)
total_correct = df['Correct'].sum()
total_incorrect = len(df) - total_correct

user_performance_labels = ['Correct', 'Incorrect']
user_performance_sizes = [total_correct, total_incorrect]

plt.figure(figsize=(8, 8))
plt.pie(user_performance_sizes, labels=user_performance_labels, autopct='%1.1f%%', startangle=90)
plt.title('Overall User Performance')
plt.savefig('pie_charts/overall_user_performance.png')
plt.clf()

# 3. Question Answering by Month
df['Datetime'] = pd.to_datetime(df['Datetime'])
df['Month'] = df['Datetime'].dt.month_name()
month_counts = df['Month'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(month_counts, labels=month_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Question Answering by Month')
plt.savefig('pie_charts/question_answering_by_month.png')
plt.clf()

# 4. Correct vs. Incorrect Ratios (Combined)
correct_answers = df['Correct'].sum()
incorrect_answers = len(df) - correct_answers

user_performance_labels = ['Correct', 'Incorrect']
user_performance_sizes = [correct_answers, incorrect_answers]

plt.figure(figsize=(8, 8))
plt.pie(user_performance_sizes, labels=user_performance_labels, autopct='%1.1f%%', startangle=90)
plt.title('Correct vs. Incorrect Answers (All Users)')
plt.savefig('pie_charts/correct_vs_incorrect.png')
plt.clf()

# 5. Correctness Distribution by Category (Combined)
category_correctness = df.groupby('Category')['Correct'].mean()

plt.figure(figsize=(8, 8))
plt.pie(category_correctness, labels=category_correctness.index, autopct='%1.1f%%', startangle=90)
plt.title('Correctness Distribution by Category (All Users)')
plt.savefig('pie_charts/correctness_distribution_by_category.png')
plt.clf()

# 6. Answering Speed Distribution
df['AnsweringSpeed'] = pd.cut(df['SecondsTakenToAnswer'], bins=[0, 10, 20, 30, 40, float('inf')],
                             labels=['<10s', '10-20s', '20-30s', '30-40s', '>40s'])
answering_speed_counts = df['AnsweringSpeed'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(answering_speed_counts, labels=answering_speed_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Answering Speed Distribution')
plt.savefig('pie_charts/answering_speed_distribution.png')
plt.clf()
