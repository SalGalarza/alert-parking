import os
import requests
import json

from flask import Flask, session, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

@app.route("/userData", methods=["POST", "GET"])
def userData():
    API_KEY = "4081adfc-6f7f-4454-af8a-418ef920d1fc"

    # coordinates = request.args["coordinates"]

    res = requests.get("https://municipal.systems/v1/places/syc-ny/dataTypes/crime/data?limit=10000", params={"key": API_KEY})
    res1 = requests.get("https://municipal.systems/v1/places/syc-ny/dataTypes/crime/data?key=4081adfc-6f7f-4454-af8a-418ef920d1fc&filters%5B0%5D%5Bdata%5D%5Btype%5D%5B%24eq%5D=Driving%20under%20influence")



    if res.status_code != 200:
        raise Exception("API Error")

    data = res.json()
    data1 = res1.json()

    latitude = request.args['latitude']
    longitude = request.args['longitude']
    # info = data['results'][0]
    coordinates = [latitude, longitude]
    userLat = str(coordinates[0])
    userLon = str(coordinates[1])
    # address = "300 S  CLINTON ST"
    # info = data['results'][0]['data']['address'] == "300 S  CLINTON ST"
    crimes = {'Driving Under Influence':0, 'Extortion':0,'Forgery/counterfeit':0,'Stolen Property':0,'Possession/marijuana':0, 'Criminal mischief':0,'Kidnapping':0,'Larceny':0,'Loitering':0,'Liquor Law Violations':0, 'Simple assault':0, 'Possession/use drug':0, 'Fraud':0, 'Disorderly conduct':0,'Sale/Manufacture Controlled Substance':0,'Sale/Manufacture Marijuana':0,'Prostitution Patron/Promoting':0, 'Sex offenses':0,'Possession/use dangerous weapons':0, 'Unauthorized use mv':0, 'All other  offenses':0, 'Offn against family':0,'Coercion':0}
    ii = 0
    l = []
    #9742
            # dataLon = str(data['results'][i]['data']['location']['coordinates'][0])
            # dataLat = str(data['results'][i]['data']['location']['coordinates'][1])

    for i in range(data['meta']['total']):

        try:
            mindataLat = str(data['results'][i]['data']['location']['bbox'][0])
            mindataLon = str(data['results'][i]['data']['location']['bbox'][1])
            maxdataLat = str(data['results'][i]['data']['location']['bbox'][2])
            maxdataLon = str(data['results'][i]['data']['location']['bbox'][3])
        except KeyError:
            pass
        else:
            if float(userLat) >= float(mindataLat) and float(userLat) <= float(maxdataLat) and float(userLon) >= float(mindataLon) and float(userLon) <= float(maxdataLon):
                # info = data['results'][i]['data']['address']
                l.append(data['results'][i]['data']['type'])
                for c in crimes:
                    if data['results'][i]['data']['type'] == c:
                        crimes[c]+=1
                        # data['results'][i]['data']['type']
                        # l.append(data['results'][i]['data']['type']==)
                # ii += 1
            maximum = max(crimes, key=crimes.get)
            print(maximum)
            if crimes[maximum] > 1:
                crime1 = maximum
            else:
                crime1 = 'none'



    # for i in range(data['meta']['total']):
    #     if data['results'][i]['data']['address'] == address:
    #         info = data['results'][i]['data']['address']
    #         l.append(data['results'][i]['data']['location']['coordinates'])
    #         ii += 1
    #     else:
    #         info = 0



# 23
    # x = data['results'][0]['data']['location']['coordinates'] == [-76.151675, 43.039448]

    # crime1 = 'Stolen Property'


    # return "{}".format(str(coordinates))
    return jsonify(crime=crime1)
    # return "coords:{}-----{}, ".format(l,crimes[max(crimes, key=crimes.get)])
    # return "{}".format(crimes)



# @app.route("/tesDatat", methods=["POST", "GET"])
# def testData():
#     latitude = request.args["latitude"]
#     longitude = request.args["longitude"]
#     time = request.args["longitude"]
#
#     crimeGrade = "A"
#     accidentsGrade = "B"
#     overall = "B+"
#
#
#     return jsonify(crime=crimeGrade,accidents=accidentsGrade,overall=overall)



def main():
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    main()
