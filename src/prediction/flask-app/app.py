import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/flights/airlines', methods=['GET'])
