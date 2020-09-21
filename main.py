
from flask import Flask, request, jsonify,render_template
import joblib
from joblib import load


clf = load("clf.joblib")
app = Flask(__name__) #Initialize the flask App

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        
        text = request.form.values()
        output=clf.predict(text)[0]
        if output==1:
            news="Real news"
        elif output==0:
            news="Fake news"
        
        return render_template('index.html', prediction_text='This piece of the news most likely is: {}'.format(news))
    except Exception as e:
        return render_template('index.html', prediction_text='This piece of the news most likely is: {}'.format(repr(e)))
        
        

if __name__ == "__main__":
    app.run(debug=True)