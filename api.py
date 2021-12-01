import math as m
import numpy as np
from flask import Flask, request, jsonify
from calculation import Calculation

app = Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


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

if __name__ == '__main__':
    app.run()