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
    return jsonify(pvYearly=pvYearly, pvDaily=pvDaily, eeDaily=eeDaily, eeYearly=eeYearly)

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

@app.route('/api/v1/kapasitas-terpasang', methods=['POST']) 
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
    pvSisi1 = nc.jumlahPV1SisiB24()
    pvSisiLawan = nc.jumlahPVSisiLawanE24()
    inverter = nc.inverterB21()
    wpInstalled = nc.kapasitasTerpasangD20()
    wattInstalled = nc.kapasitasTerpasangF20()
    return jsonify(pvSisi1=pvSisi1, pvSisiLawan=pvSisiLawan, inverter=inverter, wpInstalled=wpInstalled, wattInstalled=wattInstalled)

@app.route('/api/v1/energi-terbangkitkan', methods=['POST']) 
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
    sisi1 = nc.energiTerbangkitkanB36()
    sisi2 = nc.energiTerbangkitkanSisiLawanB37()
    pendapatanEnergi = nc.pendapatanEnergiB38()
    return jsonify(sisi1=sisi1, sisi2=sisi2, pendapatanEnergi=pendapatanEnergi)

@app.route('/api/v1/investasi', methods=['POST']) 
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
    pv = nc.pvB29()
    inverter = nc.inverterB30()
    shipping = nc.shippingPVInverterB31()
    pajak = nc.pajakB32()
    mounting = nc.mountingB33()
    total = nc.totalB34()
    simplepayback = nc.simplePayback()
    return jsonify(pv=pv, inverter=inverter, shiping=shipping, pajak=pajak, mounting=mounting, total=total)