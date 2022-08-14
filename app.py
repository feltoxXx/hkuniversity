# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_contract_table(contract, table, query, offset):

    url = 'https://engine.rishipanthee.com/contracts'
    params = {'contract':contract, 'table':table, 'query':query, 'limit':1000, 'offset':offset, 'indexes':[]}
    j = {'jsonrpc':'2.0', 'id':1, 'method':'find', 'params':params}

    with requests.post(url, json=j) as r:
        data = r.json()
        result = data['result']
        if len(result) == 1000:
            result += get_contract_table(contract, table, query, offset+1000)

    return result

@app.route('/balances/<string:symbol>', methods=['GET'])
def read_tokens(symbol):

    balances =  get_contract_table("tokens", "balances", {"symbol":symbol}, 0)

    for item in balances:
        item["balance"] = float(item["balance"])


    balances.sort(key=lambda x: x["balance"], reverse=True)

    if balances[0]["account"] == "null":
            balances.pop(0)

    return jsonify(balances)


@app.route('/')
def hello_world():
    return 'Hello from new Flask!'

