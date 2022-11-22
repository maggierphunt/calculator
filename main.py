#!/usr/bin/env python 
from google_auth_oauthlib import flow
from google.cloud import bigquery

import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import configparser
from sqlalchemy.sql import func
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from pybigquery.api import ApiClient
from sqlalchemy.engine import create_engine
from google.oauth2 import service_account
from google.cloud import bigquery, storage

basedir = os.path.abspath(os.path.dirname(__file__))


# import pandas as pd
# from fastavro import writer, parse_schema

parser = configparser.ConfigParser()
parser.read(".env")

project_id = parser.get("DEFAULT", "project_id")
# region = parser.get("DEFAULT", "region")
# instance_name = parser.get("DEFAULT", "instance_name")
# db_user = parser.get("DEFAULT", "db_user")
# db_pass = parser.get("DEFAULT", "db_pass")
# db_name = parser.get("DEFAULT", "db_name")
dataset_id = parser.get("DEFAULT", "dataset_id")
credentials = parser.get("DEFAULT", "credentials")
table = parser.get("DEFAULT", "table")

storage_client = storage.Client.from_service_account_json(credentials)
# # INSTANCE_CONNECTION_NAME = f"{project_id}:{region}:{instance_name}"

# # connector = Connector()

# def getconn():
#    conn = connector.connect(
#        INSTANCE_CONNECTION_NAME,
#        "pg8000",
#        user=db_user,
#        password=db_pass,
#        db=db_name
#    )
#    return conn

# # pool = sqlalchemy.create_engine(
# #    "postgresql+pg8000://",
# #    creator=getconn,
# # )

# # tb_key_stats = pd.read_sql_query("SELECT * From `calc_list.products`", con=pool)
# # print(tb_key_stats)

bigquery_uri = "bigquery://"+dataset_id


engine = create_engine(
    bigquery_uri,
     credentials_path=credentials
)

query = f'SELECT title, url, referrer FROM {dataset_id}.{table} \
          WHERE referrer IS NOT NULL \
          AND title IS NOT NULL \
          ORDER BY RAND () LIMIT 20;'

rows = engine.execute(query).fetchall()
# rows = [dict(row) for row in rows]
# print(rows)

# base = sqlalchemy.declarative_base()
# class Products(base):
#     __tablename__ = "products"
#     item = sqlalchemy.Column(sqlalchemy.String,primary_key=True)
#     price = sqlalchemy.Column(sqlalchemy.Float)

app = Flask("calculator")

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

    query = ("INSERT INTO calc_list.products (item, price) values (%s, %s),(%s, %s), (%s, %s);", (inputText1, inputNumber1, inputText2, inputNumber2, inputText2, inputNumber3))

    print(total)
    return render_template("results.html",inputText1=inputText1, inputNumber1=inputNumber1, inputText2=inputText2, inputNumber2=inputNumber2, inputText3=inputText3, inputNumber3=inputNumber3,total=total)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
