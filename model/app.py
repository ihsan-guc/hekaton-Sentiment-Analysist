#import the libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import joblib
from flask_cors import CORS
vocabulary = joblib.load('vocabulary.pkl') 
vect= CountVectorizer(ngram_range=(1,2), vocabulary = vocabulary)
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
def predict():
    int_features = [request.json['predict']]
    prediction = model.predict(vect.transform(int_features))
    predictionValue = str(prediction)
    print(predictionValue)
    
    output = predictionValue
    return  output

#run the app
if __name__ == "__main__":
    app.run(debug = True)