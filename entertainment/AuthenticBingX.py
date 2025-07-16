import time
import hmac
import hashlib
import requests

API_KEY = ""
API_SECRET = ""

def generate_signature(secret, params):
    query_string = '&'.join([f"{k}={params[k]}" for k in sorted(params)])
    return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

def test_contract_account_balance():
    url = "https://open-api.bingx.com/openApi/swap/v1/user/balance"  # ✅ 正确路径
    timestamp = int(time.time() * 1000)

    params = {
        "timestamp": timestamp,
        "recvWindow": 5000
    }

    params["signature"] = generate_signature(API_SECRET, params)

    headers = {
        "X-BX-APIKEY": API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = requests.post(url, headers=headers, data=params)
    print("状态码：", res.status_code)
    print("返回内容：", res.json())

test_contract_account_balance()