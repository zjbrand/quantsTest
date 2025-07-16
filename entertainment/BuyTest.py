import requests

# 模拟账户资金
account = {
    "USDT": 10000,
    "BTC": 0
}

# 获取最新成交价格
def get_price():
    url = "https://open-api.bingx.com/openApi/spot/v1/ticker/price?symbol=BTC-USDT"
    res = requests.get(url)
    data = res.json()
    print("调试返回数据：", data)
    return float(data['data'][0]['trades'][0]['price'])

# 模拟买入
def simulate_buy(usdt_amount):
    price = get_price()
    btc_bought = usdt_amount / price
    account["USDT"] -= usdt_amount
    account["BTC"] += btc_bought
    print(f"✅ 买入 BTC：{btc_bought:.6f}，价格：{price:.2f}")

# 模拟卖出
def simulate_sell(btc_amount):
    price = get_price()
    usdt_gained = btc_amount * price
    account["BTC"] -= btc_amount
    account["USDT"] += usdt_gained
    print(f"✅ 卖出 BTC：{btc_amount:.6f}，价格：{price:.2f}")

# 示例操作
simulate_buy(1000)     # 用 1000 USDT 买入
simulate_sell(0.01)    # 卖出 0.01 BTC

# 打印账户余额
print("📊 当前模拟账户状态：", account)
