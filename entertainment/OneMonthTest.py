import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import hmac
import hashlib
import requests

API_KEY = ""
API_SECRET = ""

symbol = "BTC-USDT"
interval = "1h"

# 获取毫秒时间戳
def to_millis(dt):
    return int(dt.timestamp() * 1000)

# 签名函数
def sign(params, secret):
    sorted_params = sorted(params.items())
    query_string = "&".join([f"{k}={v}" for k, v in sorted_params])
    return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# 获取历史K线
def fetch_kline(start_time, end_time):
    url = "https://open-api.bingx.com/openApi/swap/market/kline"
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": 100
    }
    res = requests.get(url, params=params)
    return res.json()

# 下载 4 月全量小时K线
def download_april_data():
    all_data = []
    start = pd.Timestamp("2024-04-01 00:00:00")
    end = pd.Timestamp("2024-04-30 23:59:59")  # 覆盖整月
    delta = pd.Timedelta(hours=100)
    while start < end:
        batch_end = min(start + delta, end)
        print(f"请求时间范围: {start} ~ {batch_end}")  # 调试打印
        result = fetch_kline(to_millis(start), to_millis(batch_end))
        if result["code"] != 0 or "data" not in result or not result["data"]:
            print("⚠️ 错误或无数据: ", result)
            start = batch_end  # 继续尝试下一个窗口
            continue
        all_data.extend(result["data"])
        start = batch_end
        time.sleep(0.3)

    if not all_data:
        raise ValueError("❌ 全部请求都未获取到数据，请检查API权限或时间范围是否有数据")

    df = pd.DataFrame(all_data)
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    df = df.astype(float)
    return df

# 策略回测函数
def backtest(df):
    initial_cash = 10000
    cash = initial_cash
    btc = 0
    entry_time = df.index[0]
    exit_time = df.index[-1]
    base_price = None
    position_history = []
    for current_time, row in df.iterrows():
        p = row["close"]
        if current_time == entry_time:
            btc += 0.5 * cash / p
            cash *= 0.5
            base_price = p
        else:
            price_change = (p - base_price) / base_price
            if price_change >= 0.02:
                sell_amount = 0.1 * (cash + btc * p) / p
                sell_amount = min(sell_amount, btc)
                btc -= sell_amount
                cash += sell_amount * p
                base_price = p
            elif price_change <= -0.02:
                buy_amount = 0.1 * (cash + btc * p)
                buy_btc = min(buy_amount / p, cash / p)
                btc += buy_btc
                cash -= buy_btc * p
                base_price = p
        position_history.append((current_time, p, cash, btc, cash + btc * p))
    result_df = pd.DataFrame(position_history, columns=["time", "price", "cash", "btc", "total_value"])
    result_df.set_index("time", inplace=True)
    final_value = cash + btc * df.loc[exit_time, "close"]
    profit = final_value - initial_cash
    roi = profit / initial_cash * 100
    print(f"期末总资产: {final_value:.2f} USDT")
    print(f"总收益: {profit:.2f} USDT")
    print(f"收益率: {roi:.2f}%")
    result_df["total_value"].plot(figsize=(12,6), title="账户总值曲线", grid=True)
    plt.ylabel("USDT")
    plt.tight_layout()
    plt.show()

# 主程序
df = download_april_data()
backtest(df)
