from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
comp = ['AAPL','MSFT','TSM','NVDA','CRM','ADBE','INTC','ASML','CSCO','ORCL','QCOM','META','AMZN','GOOGL','TWTR']
for i in comp:
	data = pdr.get_data_yahoo(i, start="2020-01-01", end="2020-12-31")
	data.to_csv(i + ".csv")