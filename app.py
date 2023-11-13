from flask import Flask, render_template, request, jsonify
from RecommenderSystem.main import get_category_recommendations

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=['GET'])
def recommender():
    return render_template("recommendations.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form.get('user_id')

    if user_id:
        category_recommendations = get_category_recommendations(user_id)
        return jsonify({'user_id': user_id, 'recommendations': category_recommendations})
    else:
        return jsonify({'error': 'User ID not provided'})

if __name__ == "__main__":
    app.run(debug=True)