from flask import Flask
from flask import request
from flask.json import jsonify
import json
import requests
from flask import Response
import pyttsx3;

app=Flask(__name__)
@app.route('/srinivas',methods=['POST'])
def name():
  print(request.get_json())
  action=request.get_json()['queryResult'][ "fulfillmentText"]
  print(action)
  engine = pyttsx3.init();
  engine.say(action);
  engine.runAndWait();

  return Response()

if __name__=="__main__":
    app.run(host = '0.0.0.0' ,debug=True,port=5000)
