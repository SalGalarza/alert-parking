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
    latitude = request.args["latitude"]
    longitude = request.args["longitude"]
    time = request.args["longitude"]

    crimeGrade = "A"
    accidentsGrade = "B"
    overall = "B+"

    # jsonify(latitude=latitude,longitude=longitude,time=time)



    return jsonify(crime=crimeGrade,accidents=accidentsGrade,overall=overall)

# if __name__ == '__main__':
#   app.run(debug=True, port=5000)
