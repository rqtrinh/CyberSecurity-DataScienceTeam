import matplotlib.pyplot as plt


def generate_scatter_plot(dataframe):
    user_answers = dataframe[['User', 'Correct']]

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
    plt.savefig('../../WebPage/Graphs/scatter_plot.png')