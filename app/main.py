import math as m
from flask import Flask, request, jsonify, render_template
from app.calculation import Calculation

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
#     return '''<h1>Irradiance Simulation</h1>
# <p>A prototype API for Calculating Expected Energy.</p>'''

@app.route('/api/v1/energy-svi-yearly', methods=['POST']) 
def expectedEnergySVIYearly():
    r = request.get_json()
    GMT = r['GMT']
    Lat = r['Lat']
    Long = r['Long']
    ColTilt = r['ColTilt']
    AzimuthCol = r['AzimuthCol']
    nc = Calculation(inputGMT = GMT, inputLat = Lat, inputLong = Long, inputColTilt = ColTilt, inputAzimuthCol = AzimuthCol)
    result = nc.getExpectedEnergySVIYearly()
    return jsonify(result)

@app.route('/api/v1/energy-svi-daily', methods=['POST']) 
def expectedEnergyDaily():
    r = request.get_json()
    GMT = r['GMT']
    Lat = r['Lat']
    Long = r['Long']
    ColTilt = r['ColTilt']
    AzimuthCol = r['AzimuthCol']
    nc = Calculation(inputGMT = GMT, inputLat = Lat, inputLong = Long, inputColTilt = ColTilt, inputAzimuthCol = AzimuthCol)
    result = nc.getExpectedEnergyDaily()
    return jsonify(result)

@app.route('/api/v1/pv-output-daily', methods=['POST']) 
def pvOutputDaily():
    r = request.get_json()
    GMT = r['GMT']
    Lat = r['Lat']
    Long = r['Long']
    ColTilt = r['ColTilt']
    AzimuthCol = r['AzimuthCol']
    nc = Calculation(inputGMT = GMT, inputLat = Lat, inputLong = Long, inputColTilt = ColTilt, inputAzimuthCol = AzimuthCol)
    result = nc.pvOutputDaily()
    return jsonify(result)

@app.route('/api/v1/pv-output-yearly', methods=['POST']) 
def pvOutputYearly():
    r = request.get_json()
    GMT = r['GMT']
    Lat = r['Lat']
    Long = r['Long']
    ColTilt = r['ColTilt']
    AzimuthCol = r['AzimuthCol']
    nc = Calculation(inputGMT = GMT, inputLat = Lat, inputLong = Long, inputColTilt = ColTilt, inputAzimuthCol = AzimuthCol)
    result = nc.pvOutputYearly()
    return jsonify(result)

@app.route('/api/v1/all-output', methods=['POST']) 
def allOutput():
    r = request.get_json()
    GMT = r['GMT']
    Lat = r['Lat']
    Long = r['Long']
    ColTilt = r['ColTilt']
    AzimuthCol = r['AzimuthCol']
    nc = Calculation(inputGMT = GMT, inputLat = Lat, inputLong = Long, inputColTilt = ColTilt, inputAzimuthCol = AzimuthCol)
    pvYearly = nc.pvOutputYearly()
    pvDaily = nc.pvOutputDaily()
    eeDaily = nc.getExpectedEnergyDaily()
    eeYearly = nc.getExpectedEnergySVIYearly()
    return jsonify(pvYearly=pvYearly, pvDaily=pvDaily, eeDaily=eeDaily, eeYearly=eeYearly)
