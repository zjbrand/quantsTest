import requests

def get_btc_price():
    url = "https://open-api.bingx.com/openApi/spot/v1/ticker/price?symbol=BTC-USDT"
    res = requests.get(url)
    data = res.json()

    print("状态码：", res.status_code)

    try:
        price = data['data'][0]['trades'][0]['price']
        print("当前BTC价格：", price)
    except Exception as e:
        print("解析失败：", e)
        print("返回数据：", data)

get_btc_price()
