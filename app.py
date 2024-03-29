from flask import Flask, render_template, request, url_for, redirect
import os
from operator import itemgetter
from typing import ItemsView
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from pybigquery.api import ApiClient
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import configparser

parser = configparser.ConfigParser()
parser.read(".env")
print(parser.read(".env"))
project_id = "calculator-369319" #parser.get("DEFAULT", "project_id")
dataset_id = "calculator-369319.calc_list"#parser.get("DEFAULT", "dataset_id")
credentials = "calculator-369319-f1a35f938612.json"
# parser.get("DEFAULT", "credentials")

api_client = ApiClient()
engine_path = "bigquery:///?DataSetId="+dataset_id+"&ProjectId="+project_id+"&InitiateOAuth=GETANDREFRESH&OAuthSettingsLocation="+credentials
engine = create_engine(engine_path, arraysize=1000)
Session = sessionmaker(bind=engine)
session = Session()

base = declarative_base()
class products(base):
    __tablename__ = "calc_list.products"
    item = Column(String,primary_key=True)
    price = Column(Float)

app = Flask("calculator-maggie-hunt")

@app.route("/", methods=["POST", "GET"])    
def landing_page():
    return render_template("index.html")

@app.route("/calculator", methods=["POST", "GET"]) 
def calculator():
    inputText1=str(request.form['inputText1'])
    inputText2=str(request.form['inputText2'])
    inputText3=str(request.form['inputText3'])
    inputNumber1=float(request.form['inputNumber1'])
    inputNumber2=float(request.form['inputNumber2'])
    inputNumber3=float(request.form['inputNumber3'])
    total = inputNumber1+inputNumber2+inputNumber3
    print("Total: ", total)
    
    input1 = products(item=inputText1, price=inputNumber1)
    input2 = products(item=inputText2, price=inputNumber2)
    input3 = products(item=inputText3, price=inputNumber3)

    inputs_list=[input1, input2, input3]
    print("List: ",inputs_list)

    for i in inputs_list:
        session.add(i)
        session.commit()
        print("Committed, ", i)

    return render_template("results.html",inputText1=inputText1, inputNumber1=inputNumber1, inputText2=inputText2, inputNumber2=inputNumber2, inputText3=inputText3, inputNumber3=inputNumber3,total=total)

if __name__ == "__main__":
    app.run(debug= True)