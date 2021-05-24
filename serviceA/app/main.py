from flask import Flask,json,jsonify
import requests

app = Flask(__name__)

@app.route("/serviceA")
def getdata():
    data= {
                "Name": "Shiva",
                "Title": "DevOps engineer",
                "DoB": "15/02/20002",
                "Description": "I love DevOps"
          }
    json_object = json.dumps(data, indent = 4)
    return json_object

@app.route("/")
def welcome():
    return "welcome to ServiceA"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=80)
