from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
     BMI = w/(h/100*h/100)
     if BMI <16:
         return "Severely underweight"
     elif BMI < 18.5:
         return "Underweight"
     elif BMI < 25:
         return "Normal"
     elif BMI < 30:
         return "Overweight"
     else:
         return "Obese"






if __name__ == "__main__":
    app.run(debug=True)