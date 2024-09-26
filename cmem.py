
import redis
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def leggi():
    r = redis.Redis(host='redis-14620.c293.eu-central-1-1.ec2.redns.redis-cloud.com', port=14620, password='9P03PNXUyBcFhpxZeFZJlc9LyqEEsSrt')
    r.close()
    response = jsonify({'testo': r.get('Italy').decode("utf-8")})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['POST'])
def scrivi():
    #testo = request.form.get('testo')
    testo = json.loads(request.data)['testo']
    r = redis.Redis(host='redis-14620.c293.eu-central-1-1.ec2.redns.redis-cloud.com', port=14620, password='9P03PNXUyBcFhpxZeFZJlc9LyqEEsSrt')
    r.mset({"Italy": testo})
    r.close()
    return jsonify(str(testo))


#app.run()

