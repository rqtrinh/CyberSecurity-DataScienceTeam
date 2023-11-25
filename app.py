from flask import Flask, render_template, request, jsonify
from RecommenderSystem.main import get_category_recommendations
from DataExtraction.ConvertJSON.convertToCSV import convert_json_csv
from DataExtraction.GenerateGraphs.extract_data import extract_data, read_csv
from DataExtraction.GenerateGraphs.generate_graphs import generate_duration_correct_user, generate_percentage_user
app = Flask(__name__)

@app.route("/")
def home():
    convert_json_csv()
    extract_data()

    return render_template("index.html")

@app.route("/recommend", methods=['GET'])
def recommender():
    return render_template("recommendations.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form.get('user_id')

    if user_id:
        # Get dataframe
        df = read_csv()
        category_recommendations = get_category_recommendations(user_id)
        # Generate user sepcific graphs
        generate_duration_correct_user(df, user_id)
        generate_percentage_user(df, user_id)

        return jsonify({'user_id': user_id, 
                        'recommendations': category_recommendations})
    else:
        return jsonify({'error': 'User ID not provided'})

if __name__ == "__main__":
    app.run(debug=True)