from operator import itemgetter
import os
from app import app
from typing import ItemsView
from flask import Flask, render_template, request, url_for, redirect
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from pybigquery.api import ApiClient
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
# import configparser

# parser = configparser.ConfigParser()
# parser.read(".env")

# project_id = parser.get("DEFAULT", "project_id")
# dataset_id = parser.get("DEFAULT", "dataset_id")
# credentials = parser.get("DEFAULT", "credentials")
# table_name = parser.get("DEFAULT", "table")
project_id="calculator-369319"
dataset_id="calculator-369319.calc_list"
credentials="calculator-369319-f1a35f938612.json"


api_client = ApiClient()
engine_path = "bigquery:///?DataSetId="+dataset_id+"&ProjectId="+project_id+"&InitiateOAuth=GETANDREFRESH&OAuthSettingsLocation="+credentials
engine = create_engine(engine_path, arraysize=1000)

Session = sessionmaker(bind=engine)
session = Session()
# session.Model = session.make_declarative_base()
# # base.query = session.query_property()
# base = sqlalchemy.declarative_base()

class products(ItemsView, price): #todo: sort
    __tablename__ = "products"
    item = Column(String,primary_key=True)
    price = Column(Float)

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
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))