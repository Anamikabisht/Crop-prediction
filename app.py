import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array([int_features])   # 2D array for model
    prediction = model.predict(final_features)
    output = prediction[0]   # for classification (string label)

    return render_template(
        'index.html',
         prediction_text = f"The suggested crop is ({output})"
    )

if __name__ == '__main__':
    flask_app.run(debug=True)
