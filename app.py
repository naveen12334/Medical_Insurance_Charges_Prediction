from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("pred_price.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        age= int(request.form['age'])
        sex=int(request.form['sex'])
        bmi= float(request.form['bmi'])
        children= int(request.form['children'])
        smoker = int(request.form['smoker'])
        region= int(request.form['region'])

    prediction=model.predict([[
            age,
            sex,
            bmi,
            children,
            smoker,
            region
        ]])
    output=round(prediction[0],2)

    return render_template('home.html',prediction_text="Predicted Insurance Charges is ${}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

