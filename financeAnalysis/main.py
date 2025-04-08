# This is a sample Python script.
import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare
import tushare as ts
import datetime
import dateutil

# # **创建 tushare 接口**
# pro = ts.pro_api('6174e1dabd17988b77370c95d1e049cb93b94ee62c1935e493e0b8a2')
#
# trade_cal=pro.trade_cal()
# print(trade_cal)
trade_cal=pd.read_csv("china_stock_market_calendar.csv")
#print(trade_cal)

CASH=100000
START_DATE='2016-01-07'
END_DATE='2022-01-31'

class Context:
     def __init__(self, cash, start_date, end_date):
         self.cash=cash
         self.start_date=start_date
         self.end_date=end_date
         self.position={}
         self.benchmark=None
         self.date_range=trade_cal[(trade_cal['isOpen']==1) & \
                                   (trade_cal['calendarDate']>=start_date) & \
                                   (trade_cal['calendarDate'] <= end_date)]['calendarDate'].values

         #self.dt=dateutil.parser.parse(start_date)
         self.dt=None


context=Context(CASH,START_DATE,END_DATE)

# context=Context(1000,'2016-01-01','2017-01-01')
# print(context.date_range)

class G:
    pass

g=G()

def set_benchmark(security):
    context.benchmark=security

def attibute_history(security,count,fields=('Open','Close','Low','High','Volume')):
    end_date=(context.dt-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    start_date=trade_cal[(trade_cal['isOpen']==1) & (trade_cal['calendarDate']<=end_date)][-count:].iloc[0,:]['calendarDate']
    #print(start_date,end_date)
    return  attribute_daterange_history(security,start_date,end_date,fields)

#attibute_history('601318',10)
def attribute_daterange_history(security,start_date,end_date,fields=('Open','Close','Low','High','Volume')):
  try:
    f=open(security + '.csv','r')
    df=pd.read_csv(f,index_col='Date',parse_dates=['Date']).loc[start_date:end_date,:]
  except FileNotFoundError:
    df=tushare.get_k_data(security,start_date,end_date)
  return df[list(fields)]

#print(attibute_history('601318',20))

# 今日の銘柄の価格を取るメソッド
def get_today_data(security):
    today=context.dt.strftime('%Y-%m-%d')
    try:
        f=open(security+'.csv','r')
        data=pd.read_csv(f,index_col='Date',parse_dates=['Date']).loc[today,:]
    except FileNotFoundError:
        data=tushare.get_k_data(security,today,today).iloc[0,:]
    except KeyError:
        data=pd.Series()
    #return data.round(3).apply(lambda x: f"{x:.3f}")
    return data.round(3)

# 下单
def _order(today_data,security,amount):
    #print(f"📊 今日数据: {today_data}")  # 调试信息
    if 'Open' not in today_data:
        print(today_data)
        print(f"⚠️ 数据缺失: {security} 没有 'Open' 列, 跳过交易")
        return
    p=today_data['Open']

    if len(today_data)==0:
        print("今日停牌")

    # 下单数量过大
    if context.cash - amount * p <0:
        amount=int(context.cash/p)
        print("现金不足，已调整为%d"%amount)

    # amount如果为负则是要卖出股票
    if amount % 100 !=0:
        if amount != -context.position.get(security,0):
            amount=int(amount/100)*100
            print("不是100的倍数，已调整为%d"%amount)

    if context.position.get(security,0) < -amount:
        amount=-context.position.get(security,0)
        print("卖出股票不能超过持仓数，已调整为%d"%amount)

    # 算出新的持仓
    context.position[security]=context.position.get(security,0) + amount

    # 更新现金，买入amount为正，钱减少；卖出amount为负，钱增加
    context.cash -= amount * p

    # 持仓数为零则删除改股键值
    if context.position[security] == 0:
        del context.position[security]

# _order(get_today_data('601318'),'601318',1000000000)
# print(context.position)
# _order(get_today_data('601318'),'601318',-500)
# print(context.position)

# 下单操作的四个方法
# 买卖股票数作为参数
def order(security, amount):
    today_data=get_today_data(security)
    _order(today_data,security,amount)

# 买卖到多少作为参数，amount不能为负
def order_target(security, amount):
    if amount < 0:
        print("数量不能为负，已调整成0")
        amount=0

    today_data= get_today_data(security)
    hold_amount=context.position.get(security,0)
    data_amount= amount-hold_amount
    _order(today_data,security,data_amount)

# 买多少钱的股票
def order_value(security, value):
    today_data=get_today_data(security)
    if today_data.empty:
        print(f"⚠️ 今日数据为空，跳过交易: {security}")
        return  # 直接跳过，防止 KeyError
    amount=int(value / today_data['Open'])
    _order(today_data,security,amount)

# 买到多少钱的股票
def order_target_value(security,value):
    today_data=get_today_data(security)
    if value < 0:
        print("价值不能为负，已调整为0")
        value=0

    hold_value=context.position.get(security,0) * today_data['Open']
    data_value=value-hold_value
    order_value(security,data_value)

# order('601318',100)
# order_value('600519',30000)
# print(context.position)

# order_target('601318',520)
# order_target_value('600519',30000)
# print(context.position)

def run():
    plt_df=pd.DataFrame(index=pd.to_datetime(context.date_range),columns=['value'])
    init_value=context.cash
    initialize(context)
    last_prize={}
    for dt in context.date_range:
        context.dt=dateutil.parser.parse(dt)
        handle_data(context)
        value=context.cash
        for stock in context.position:
            today_data=get_today_data(stock)
            if len(today_data)==0:
                p=last_prize[stock]
            else:
                p=today_data['Open']
                last_prize[stock]=p
            value += p*context.position[stock]
        plt_df.loc[dt,'value']=value
    plt_df['ratio']=(plt_df['value']-init_value) / init_value
    #print(plt_df['ratio'])

    bm_df=attribute_daterange_history(context.benchmark,context.start_date,context.end_date)
    bm_init=bm_df['Open'].iloc[0]
    plt_df['benchmark_ratio']=(bm_df['Open']-bm_init) / bm_init

    plt_df[['ratio','benchmark_ratio']].plot()
    plt.show()

def initialize(context):
    set_benchmark('601318')
    g.p1=5
    g.p2=60
    g.security='601318'

def handle_data(context):
    hist=attibute_history(g.security,g.p2)
    ma5=hist['Close'][g.p1:].mean()
    ma60=hist['Close'].mean()

    if ma5>ma60 and g.security not in context.position:
        order_value(g.security, context.cash)
    if ma5<ma60 and g.security in context.position:
        order_target(g.security,0)

run()





