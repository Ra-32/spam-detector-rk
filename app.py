from flask import Flask, render_template, request
import joblib

# Load the saved model
model = joblib.load('spam2_classifier.joblib')  

# Initialize Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    message = ""

    if request.method == 'POST':
        message = request.form['message']
        prediction_label = model.predict([message])[0]
        prediction = 'Spam 💀' if prediction_label == 1 else 'Not Spam ✅'

    return render_template('index.html', prediction=prediction, message=message)

# # ✅ Corrected this line!
# if __name__ == '__main__':
#     app.run(debug=True)
