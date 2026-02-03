from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# 1. LOAD MODELS
# We load all the brains just like before
with open('model_layout.pkl', 'rb') as f: m_lay = pickle.load(f)
with open('model_font.pkl', 'rb') as f: m_font = pickle.load(f)
with open('model_pri.pkl', 'rb') as f: m_pri = pickle.load(f)
with open('model_sec.pkl', 'rb') as f: m_sec = pickle.load(f)
with open('model_ter.pkl', 'rb') as f: m_ter = pickle.load(f)

# Map names to numbers (Must match training!)
cat_map = {
    'Blog': 0, 'Corporate': 1, 'E-commerce': 2, 'Education': 3, 
    'Food': 4, 'Gaming': 5, 'Portfolio': 6, 'Travel': 7
}

# 2. THE HOME PAGE ROUTE
@app.route('/')
def home():
    # This serves the HTML file to the browser
    return render_template('index.html')

# 3. THE PREDICTION API ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from JavaScript
        data = request.json
        category = data['category']
        
        # Convert text to code
        if category in cat_map:
            code = cat_map[category]
        else:
            return jsonify({'error': 'Invalid Category'})

        # Predict
        input_data = pd.DataFrame([[code]], columns=['Category_Code'])
        
        result = {
            'layout': m_lay.predict(input_data)[0],
            'font': m_font.predict(input_data)[0],
            'primary': m_pri.predict(input_data)[0],
            'secondary': m_sec.predict(input_data)[0],
            'tertiary': m_ter.predict(input_data)[0]
        }
        
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)