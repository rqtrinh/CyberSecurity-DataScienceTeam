import pandas as pd
from sklearn.metrics.pairwise import linear_kernel

# Load the CSV data into a DataFrame
df = pd.read_csv('test_user_data.csv')

def get_category_recommendations(user_id, num_recommendations=2):
    # Filter data for the given user
    user_data = df[df['User'] == user_id]

    # Calculate the user's average time to answer
    avg_time_to_answer = user_data['SecondsTakenToAnswer'].mean()

    # Create a dictionary to store the correctness and time spent for each category
    category_data = {}

    for index, row in user_data.iterrows():
        category = row['Category']
        correctness = row['Correct']
        time_spent = row['SecondsTakenToAnswer']

        if category not in category_data:
            category_data[category] = {'correctness': 0, 'time_spent': 0}
        
        category_data[category]['correctness'] += correctness
        category_data[category]['time_spent'] += time_spent

    # Calculate the weighted average for each category
    for category, data in category_data.items():
        data['weighted_avg'] = (data['time_spent'] / avg_time_to_answer) * data['correctness']

    # Calculate the cosine similarity between the user's data and all other users
    user_features = user_data[['Correct', 'SecondsTakenToAnswer']]
    df_features = df[['Correct', 'SecondsTakenToAnswer']]
    cosine_sim = linear_kernel(user_features, df_features)

    # Get the user index
    user_index = user_data.index[0]

    # Calculate the mean combined score for each category based on user similarity
    category_scores = {}
    for category, data in category_data.items():
        category_scores[category] = (cosine_sim[user_index] * data['weighted_avg']).mean()

    # Get the indices of the top categories
    top_category_indices = sorted(category_scores, key=category_scores.get)[:num_recommendations]

    return top_category_indices

# Test the recommender system for a specific user
user_id = "User6"
category_recommendations = get_category_recommendations(user_id)
print(f"Recommended categories for {user_id} to work on:")
print(category_recommendations)
