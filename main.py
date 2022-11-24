import os
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])    
def landing_page():

    return render_template("index.html")

@app.route("/calculator", methods=["POST", "GET"]) 
def calculator():
    inputText1=str(request.form['inputText1'])
    inputText2=str(request.form['inputText2'])
    inputText3=str(request.form['inputText3'])
    inputNumber1=int(request.form['inputNumber1'])
    inputNumber2=int(request.form['inputNumber2'])
    inputNumber3=int(request.form['inputNumber3'])
    total = inputNumber1+inputNumber2+inputNumber3

    print(total)
    return render_template("results.html",inputText1=inputText1, inputNumber1=inputNumber1, inputText2=inputText2, inputNumber2=inputNumber2, inputText3=inputText3, inputNumber3=inputNumber3,total=total)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))