import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_scatter_plot(df):
    user_answers = df[['User', 'Correct']]

    users = list(user_answers['User'].unique())  
    user_percentages = []

    for user in users:
        correct = len(user_answers[(user_answers['User'] == user) & (user_answers['Correct'] == True)])
        wrong = len(user_answers[(user_answers['User'] == user) & (user_answers['Correct'] == False)])
        
        #Calcualte percentages
        user_percentages.append(round(correct / (correct + wrong) * 100, 2))
    
    plt.scatter(users, user_percentages, label='Data Points')
    plt.xlabel("Players")
    plt.ylabel("Percentage Correct")
    plt.ylim(0, 110)
    plt.title("Percentage of Correct")
    plt.savefig('WebPage/Graphs/scatter_plot.png')

def generate_duration_correct(df):
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
    plt.savefig('WebPage/Graphs/time-taken-vs-correctness-users.png')

def generate_duration_correct_user(df):
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

        plt.savefig('WebPage/Graphs/time-taken-vs-correctness.png')

def generate_pi_chart(df):
    # 1. Category Distribution
    category_counts = df['Category'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Category Distribution')
    plt.savefig('WebPage/Graphs//category_distribution.png')
    plt.clf()

    # 2. User Performance (Combined)
    total_correct = df['Correct'].sum()
    total_incorrect = len(df) - total_correct

    user_performance_labels = ['Correct', 'Incorrect']
    user_performance_sizes = [total_correct, total_incorrect]

    plt.figure(figsize=(8, 8))
    plt.pie(user_performance_sizes, labels=user_performance_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Overall User Performance')
    plt.savefig('WebPage/Graphs//overall_user_performance.png')
    plt.clf()

    # 3. Question Answering by Month
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Month'] = df['Datetime'].dt.month_name()
    month_counts = df['Month'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(month_counts, labels=month_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Question Answering by Month')
    plt.savefig('WebPage/Graphs//question_answering_by_month.png')
    plt.clf()

    # 4. Correct vs. Incorrect Ratios (Combined)
    correct_answers = df['Correct'].sum()
    incorrect_answers = len(df) - correct_answers

    user_performance_labels = ['Correct', 'Incorrect']
    user_performance_sizes = [correct_answers, incorrect_answers]

    plt.figure(figsize=(8, 8))
    plt.pie(user_performance_sizes, labels=user_performance_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Correct vs. Incorrect Answers (All Users)')
    plt.savefig('WebPage/Graphs//correct_vs_incorrect.png')
    plt.clf()

    # 5. Correctness Distribution by Category (Combined)
    category_correctness = df.groupby('Category')['Correct'].mean()

    plt.figure(figsize=(8, 8))
    plt.pie(category_correctness, labels=category_correctness.index, autopct='%1.1f%%', startangle=90)
    plt.title('Correctness Distribution by Category (All Users)')
    plt.savefig('WebPage/Graphs//correctness_distribution_by_category.png')
    plt.clf()

    # 6. Answering Speed Distribution
    df['AnsweringSpeed'] = pd.cut(df['SecondsTakenToAnswer'], bins=[0, 10, 20, 30, 40, float('inf')],
                                labels=['<10s', '10-20s', '20-30s', '30-40s', '>40s'])
    answering_speed_counts = df['AnsweringSpeed'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(answering_speed_counts, labels=answering_speed_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Answering Speed Distribution')
    plt.savefig('WebPage/Graphs//answering_speed_distribution.png')
    plt.clf()

def correct_vs_category(df):
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
    plt.savefig("WebPage/Graphs/correct-vs-category.png")