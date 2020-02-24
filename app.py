"""
Name: Aayog Koirala
"""
from flask import Flask, render_template, request, redirect, url_for
import sys
import requests

access_key = "ab3da48538912c170cb2f285427d951d"
app = Flask(__name__)
app.debug = True
global data
def apiRequest():    
    forSymbols = f"http://data.fixer.io/api/symbols?access_key={access_key}"
    res = requests.get(forSymbols)
    data = dict()
    if res.status_code != 200:
        raise Exception("Error. API request unsuccessful.")
    data['symbols'] = res.json()['symbols']
    return data

@app.route("/")
@app.route("/index")
def index():
    data = apiRequest()
    return render_template("index.html", data=data)

@app.route("/response/<string:fromCurrency>/<string:toCurrency>")
def response(fromCurrency, toCurrency):
    fromCurrency = fromCurrency.upper()
    toCurrency = toCurrency.upper()
    url = f"http://data.fixer.io/api/latest?access_key={access_key}"
    res = requests.get(url)
    symbols = apiRequest()
    if res.status_code != 200:
        raise Exception("Error. API request unsuccessful.")
    data = res.json()
    exchangeRate = round(((data['rates'][toCurrency]))/(data['rates'][fromCurrency]),2)
    return render_template("index.html", toValue = toCurrency, fromValue=fromCurrency, data=symbols, exchangeRate=exchangeRate)