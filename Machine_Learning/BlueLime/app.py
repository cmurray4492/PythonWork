from flask import Flask,jsonify, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

model_scaler = joblib.load('model_scaler.pkl')
model = model_scaler['model']
scaler = model_scaler['scaler']


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
