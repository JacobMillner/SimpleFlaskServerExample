from flask import Flask, jsonify
import datetime
app = Flask(__name__)

@app.route('/')
def time():
    # get the UTC DateTime in ISO format
    dateTime = datetime.datetime.utcnow().isoformat()
    data = {}
    data['timestamp'] = dateTime
    return jsonify(data)
