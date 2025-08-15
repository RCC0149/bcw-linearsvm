from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            # Get features from form
            features = [float(request.form[f'feature{i}']) for i in range(1, 10)]
            # Validate input (1-10)
            if any(f < 1 or f > 10 for f in features):
                error = "All features must be between 1 and 10."
            else:
                # Scale and predict
                features_scaled = scaler.transform([features])
                prob = model.predict_proba(features_scaled)[0, 1]
                # Use custom threshold (0.1 for high recall)
                prediction = 1 if prob > 0.1 else 0
        except Exception as e:
            error = f"Error processing input: {str(e)}"
    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)