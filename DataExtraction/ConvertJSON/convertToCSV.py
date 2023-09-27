import csv
import json

# Define the JSON file path
json_file = "user_data.json"

# Load JSON data from the file
with open(json_file, 'r') as file:
    json_data = json.load(file)

# Define the CSV file path
csv_file = "user_data.csv"

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the CSV header
    writer.writerow(["User", "QuestionID", "Question", "Options", "Correct", "Category", "SecondsTakenToAnswer", "Datetime"])

    # Iterate through the JSON data and write rows to the CSV file
    for user, user_data in json_data.items():
        for question in user_data["questions"]:
            writer.writerow([
                user,
                question["questionId"],
                question["question"],
                "|".join(question["options"]),  # '|' is the delimiter for the list
                question["correct"],
                question["category"],
                question["secondsTakenToAnswer"],
                question["datetime"]
            ])

print(f"CSV data has been written to {csv_file}")
