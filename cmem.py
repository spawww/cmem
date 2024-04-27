
import redis
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def leggi():
    r = redis.Redis(host='redis-14427.c250.eu-central-1-1.ec2.cloud.redislabs.com', port=14427, password='a1Ifs4QLlpVzi0kbIj5SWNogdnL5BBum')
    r.close()
    response = jsonify({'screv': r.get('Italy').decode("utf-8")})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['POST'])
def scrivi():
    #testo = request.form.get('testo')
    testo = json.loads(request.data)['testo']
    r = redis.Redis(host='redis-14427.c250.eu-central-1-1.ec2.cloud.redislabs.com', port=14427, password='a1Ifs4QLlpVzi0kbIj5SWNogdnL5BBum')
    r.mset({"Italy": testo})
    r.close()
    return jsonify(str(testo))


#app.run()

