import math as m
from flask import Flask, request, jsonify, render_template
from numpy import result_type
from app.calculation import Calculation

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    # return 'api'

@app.route('/api/v1/energy-svi-yearly', methods=['POST']) 
def expectedEnergySVIYearly():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.getExpectedEnergySVIYearly()
    return jsonify(result)

@app.route('/api/v1/energy-svi-daily', methods=['POST']) 
def expectedEnergyDaily():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.getExpectedEnergyDaily()
    return jsonify(result)

@app.route('/api/v1/pv-output-daily', methods=['POST']) 
def pvOutputDaily():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.pvOutputDaily()
    return jsonify(result)

@app.route('/api/v1/pv-output-yearly', methods=['POST']) 
def pvOutputYearly():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.pvOutputYearly()
    return jsonify(result)

@app.route('/api/v1/all-output', methods=['POST']) 
def allOutput():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    pvYearly = nc.pvOutputYearly()
    pvDaily = nc.pvOutputDaily()
    eeDaily = nc.getExpectedEnergyDaily()
    eeYearly = nc.getExpectedEnergySVIYearly()
    inverter = nc.inverterB17()
    kt = nc.kapasitasTerpasangB18()
    return jsonify(pvYearly=pvYearly, pvDaily=pvDaily, eeDaily=eeDaily, eeYearly=eeYearly, inverter=inverter, kt=kt)

@app.route('/api/v1/return-of-investment', methods=['POST']) 
def rOI():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.rOI()
    return jsonify(result)

@app.route('/api/v1/net-present-value', methods=['POST']) 
def nPV():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.netPresentValue()
    return jsonify(result)

@app.route('/api/v1/payback-bunga-bank', methods=['POST']) 
def paybackBungaBank():
    r = request.get_json()
    gMT = r['GMT']
    lat = r['Lat']
    long = r['Long']
    colTilt = r['ColTilt']
    azimuthCol = r['AzimuthCol']
    rLength = r['RLength']
    rWidth = r['RWidth']
    pln = r['PLN']
    nc = Calculation(inputGMT = gMT, inputLat = lat, inputLong = long, inputColTilt = colTilt, 
    inputAzimuthCol = azimuthCol, inputRoofLength = rLength, inputRoofWidth = rWidth, inputPLN = pln)
    result = nc.paybackPinjamanBungaBank()
    return jsonify(result)