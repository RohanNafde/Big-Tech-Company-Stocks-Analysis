from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
comp = ['AAPL','MSFT','TSM','NVDA','CRM','ADBE','INTC','ASML','CSCO','ORCL','QCOM','AVGO','ACN','TXN','SAP','SHOP',
'IBM','AMD','NOW','SQ','FIS','INTU','UBER','FISV','AMAT','MU','INFY','LRCX','VMW','ADSK','TEAM','DELL','ADI','WDAY',
'NXPI','CTSH','ERIC','DOCU','PLTR','KLAC','APH','TEL','U','MCHP','STM','SNPS','CRWD','SPLK','CDNS','MRVL','OKTA',
'HPQ','MSI','PANW','GLW','DDOG','ANSS','WIT','RNG','FTV','PAYC','SWKS','COUP','VRSN','GRMN','KEYS','FLT',
'NET','ANET','CAJ','ZBRA','ZS','FTNT','EPAM','CDW','GIB','TER','SSNC','ZI','UMC','BR','HUBS','QRVO','CHKP','AKAM','TYL','UI','ZEN','CTXS','TRMB','AVLR','STX','SSNLF',
'GOOGL','META','TWTR','ZM','TCEHY','AMZN','TSLA']

for i in comp:
	data = pdr.get_data_yahoo(i, start="2006-01-01", end="2022-11-10")
	data.to_csv(i + ".csv")
