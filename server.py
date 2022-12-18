import pandas as pd
from flask import Flask, request, jsonify
from waitress import serve
import pickle
from datetime import datetime
# install flask, waitress, pickle into your ananconda environment

app = Flask(__name__)
modelOne = pickle.load(open('model1.pkl', 'rb')) # load model1 to the server, 'rb' - read binary
moving_avg_50 = pd.read_pickle('50_MA.pkl') 
moving_avg_200 = pd.read_pickle('200_MA.pkl') 


@app.route('/model1', methods=['GET'])
def callModelOne():
    a = request.args.get('a', type= float)
    b = request.args.get('b', type= float)
    c = request.args.get('c', type= float)
    d = request.args.get('d', type= float)
    arr = pd.DataFrame({'sepal_length_cm': [a], 'sepal_width_cm': [b], 'petal_length_cm': [c], 'petal_width_cm':[d]})
    predictedvalue = modelOne.predict(arr)[0]
    display = "Inputs(in cm): SeptalLength:{0}, SeptalWidth:{1},PetalLength:{2},PetalWidth:{3}. Predicted Class: {4}"
    result = display.format(a,b,c,d,predictedvalue)
    return str(result)

 
@app.route('/model2', methods=['GET'])
def callModelTwo():
   x = request.args.get('x')
   input_date = pd.Timestamp(x)
   print(input_date)
   print(moving_avg_50)
   for value in list(moving_avg_50.index):
    print (value)
    if input_date == value:
        print(value)
        predictedStockPrice_50 = moving_avg_50.loc[value]
        predictedStockPrice_200 = moving_avg_200.loc[value]
        return "Input Date:" + str(x) + " Predicted Stock Price: " + str(predictedStockPrice_50) + " (moving avg 50), " +  str(predictedStockPrice_200) + " (moving avg 200)"
   return str("Date not available in dataset for prediction")

# run the server
if __name__ == '__main__':
    print("Starting the server.....")
    serve(app, host="0.0.0.0", port=8070)
