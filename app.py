# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, render_template
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

def get_history(account, symbol, limit, offset):
        """"Get the transaction history for an account and a token"""
        url = "https://accounts.hive-engine.com/accountHistory?account=%s&limit=%s&offset=%s&symbol=%s" % (account, limit, offset, symbol)
        response = []
        with requests.get(url) as r:
            result = r.json()
            for item in result:
                response.append(item)
                if item["to"] == "null":
                    break
                
             
            if len(response) == 500:
                result += get_history(account, symbol, limit, offset+500)
           

        return response

def account_history(account, symbol, limit, offset):
        """"Get the transaction history for an account and a token"""
        url = "https://accounts.hive-engine.com/accountHistory?account=%s&limit=%s&offset=%s&symbol=%s" % (account, limit, offset, symbol)
        with requests.get(url) as r:
            result = r.json()                
             
            if len(result) == 500:
                result += account_history(account, symbol, limit, offset+500)
           
        return result


@app.route('/proyecto1')
def proyecto1():
    balances =  get_contract_table("tokens", "balances", {"symbol":"BUDSX"}, 0)
    
    balance =  get_contract_table("tokens", "balances", {"account": "hk-staking"}, 0)
    
    budsxSupply =  get_contract_table("tokens", "tokens", {"symbol":"BUDSX"}, 0)
    
    poolPrice =  get_contract_table("marketpools", "pools", {"tokenPair": "BUDS:SWAP.HIVE"}, 0)


    for item in balances:
        item["balance"] = float(item["balance"])

    balances.sort(key=lambda x: x["balance"], reverse=True)

    if balances[0]["account"] == "null":
        balances.pop(0)
    

    return jsonify({"balanceStaking":balance, "budsxSupply":budsxSupply, "poolPrice":poolPrice, "holders":balances})


@app.route('/proyecto2')
def proyecto2():

    # @hk-vault   (`paquetes de avatares)
    # @hk-nvault (porros)
    # @hk-forge  (forja)
    # @hk-dev     (shared market fee)
    # @hashkings  (torres de agua)
    # @hk-bang   (paquetes bang!)
    balancevault = []
    balancenvault = []
    balanceforge = []
    balancedev = []
    balancehashkings = []
    balancebang = []
    accounts= {
        "hk-vault":balancevault,
        "hk-nvault":balancenvault,
        "hk-forge":balanceforge,
        "hk-dev":balancedev,
        "hashkings":balancehashkings,
        "hk-bang":balancebang
    }

    for k, v in accounts.items():
        accounts[k] = get_history(k, "BUDS", 500, 0)


    return jsonify(accounts)


@app.route('/proyecto3')
def proyecto3():
    landplots =  get_contract_table("nft", "HKFARMinstances", {"properties.TYPE": "plot"}, 0)

    return jsonify(landplots)


@app.route('/proyecto4')
def proyecto4():
    avatares =  get_contract_table("nft", "HKFARMinstances", {"properties.TYPE": "avatar"}, 0)

    return jsonify(avatares)


@app.route('/proyecto5')
def proyecto5():

    torres =  get_contract_table("nft", "HKFARMinstances", {"properties.TYPE": "water"}, 0)

    txsSWAPHIVE = []
    txsBUDS = []
    txsHIVE = []
    txs= {
        "SWAP.HIVE":txsSWAPHIVE,
        "BUDS":txsBUDS,
        "HIVE":txsHIVE,
    }

    for k, v in txs.items():
        txs[k] = account_history("hashkings", k, 500, 0)

    return jsonify({"hashkings":txs, "holders":torres})



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
    return render_template('index.html')

