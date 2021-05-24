from flask import Flask,request
import requests
import json
app = Flask(__name__)


@app.route("/serviceB")
def getjsoninfo():
    url="http://servicea.default.svc.cluster.local/serviceA"
    #url="http://0.0.0.0:80/serviceA"
    response = requests.get(url)
    data = json.loads(response.text)
    return ("Hello my name is {} and {}". format(data['Name'], data['Description']))


@app.route("/")
def welcome():
    return "welcome to api serviceB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=80)
