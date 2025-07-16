import requests
import time

def get_btc_price():
    url = "https://open-api.bingx.com/openApi/spot/v1/ticker/price?symbol=BTC-USDT"
    res = requests.get(url)
    data = res.json()
    print("状态码：", res.status_code)
    print("返回数据：", data)  # 关键调试语句
    #print("BTC价格:", data['data'][0]['price'])  # 修复点

# while True:
#     get_btc_price()
#     time.sleep(10)  # 每10秒查询一次
get_btc_price()

