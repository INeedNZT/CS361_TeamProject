import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/s',methods=['POST'])
def s():
    return render_template('read.html')

@app.route('/button',methods=["POST"])
def button():
    df = pd.read_csv('../limingx-CSV-web-scrap-service/FIFA10.csv')
    a = request.form['select']
    return str(df[a] )
app.run()