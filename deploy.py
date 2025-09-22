from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
#load the model
model = pickle.load(open('savedmodel.sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    sepal_legth = request['sepal_length']
    sepal_width = request




if __name__=='__main__':
    app.run(debug=True)
