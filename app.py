from flask import Flask
from flask import render_template
from flask import request
import joblib
app = Flask(__name__)

#code business logib

@app.route("/")
def base():
    return render_template("home.html")

@app.route("/predict",methods = ["post"])
def predict():

    model = joblib.load("diabetes_80.pkl")

    preg = request.form.get("preg")
    plas = request.form.get("plas")
    pres = request.form.get("pres")
    skin = request.form.get("skin")
    test = request.form.get("test")
    mass = request.form.get("mass")
    pedi = request.form.get("pedi")
    age = request.form.get("age")

    print(preg, plas, pres, skin, test, mass, pedi, age)

    output  = model.predict([[int(preg), int(plas), int(pres), int(skin), int(test), int(mass), int(pedi), int(age)]])
    if output == 0:
        message = "Person is not diabetic"
    else:
        message = "Person is diabetic"

    return render_template("predict.html",data=message)
if __name__ == "__main__":
    app.run(debug=True) # writing debug = True you are in a developer mode so you dont have to close it and open it again