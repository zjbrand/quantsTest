import yfinance as yf
data = yf.download("001318.SZ", start="2020-01-01", end="2023-01-01")
data.to_csv("000001SZ.csv")