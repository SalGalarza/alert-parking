import os
import requests
import json

from flask import Flask, session, render_template, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

@app.route("/userData", methods=["POST", "GET"])
def userData():
    API_KEY = "4081adfc-6f7f-4454-af8a-418ef920d1fc"

    # coordinates = request.args["coordinates"]

    res = requests.get("https://municipal.systems/v1/places/syc-ny/dataTypes/crime/data?limit=10000", params={"key": API_KEY})
    # if res.status_code != 200:
    #     raise Exception("API Error")
    data = res.json()
    # latitude = request.args["latitude"]
    # longitude = request.args["longitude"]
    # info = data['results'][0]
    # coordinates = [latitude, longitude]
    address = "300 S  CLINTON ST"
    # info = data['results'][0]['data']['address'] == "300 S  CLINTON ST"

    ii = 0
    l = []

    for i in range(9742):
        if data['results'][i]['data']['address'] == address:
            info = data['results'][i]['data']['address']
            l.append(data['results'][i]['data']['location']['coordinates'])
            ii += 1
        else:
            info = 0

    # x = data['results'][0]['data']['location']['coordinates'] == [-76.151675, 43.039448]


    # return "{}".format(str(info))
    return "number in loc:{}, coords:{}, ".format(str(data),l)



@app.route("/tesDatat", methods=["POST", "GET"])
def testData():
    latitude = request.args["latitude"]
    longitude = request.args["longitude"]
    time = request.args["longitude"]

    crimeGrade = "A"
    accidentsGrade = "B"
    overall = "B+"


    return jsonify(crime=crimeGrade,accidents=accidentsGrade,overall=overall)



def main():
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()
