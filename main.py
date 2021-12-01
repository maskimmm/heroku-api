import math as m
from flask import Flask, request, jsonify
from calculation import Calculation

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Irradiance Simulation</h1>
<p>A prototype API for Calculating Expected Energy.</p>'''

@app.route('/api/v1/resources/list-api', methods=['GET'])
def api_all():
    print("List API Loaded.")
    # return jsonify(books)

@app.route('/api/v1/energy-svi-yearly', methods=['POST']) 
def expectedEnergySVIYearly():
    # r:float = request.args
    r = request.get_json()
    GMT = r['GMT']
    Lat = r['Lat']
    Long = r['Long']
    ColTilt = r['ColTilt']
    AzimuthCol = r['AzimuthCol']
    nc = Calculation(inputGMT = GMT, inputLat = Lat, inputLong = Long, inputColTilt = ColTilt, inputAzimuthCol = AzimuthCol)
    result = nc.getExpectedEnergySVIYearly()
    return jsonify(result)