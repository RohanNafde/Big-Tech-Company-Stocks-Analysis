import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import math

BigTech = ['AAPL', 'DELL', 'HPQ', 'SSNLF', 'MSFT', 'ADBE', 'GOOGL', 'META', 'TWTR', 'SAP', 'ORCL', 'CRM', 'ZM', 'CSCO',
'IBM', 'TCEHY', 'AMZN', 'AMD', 'INTC', 'TSM', 'NVDA', 'QCOM', 'ASML', 'UBER','TSLA']
#Don't plot TWTR, META, TSLA, UBER, ZM, DELL, TCEHY, for Recession


for i in range(0,len(BigTech)): 

    fname = r"C:\IIT\DS203\Project\yfinance\\" + BigTech[i] + ".csv"
    df = pd.read_csv(fname)
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close']
                    )])

    # For info on x-axis ::  fig.update_traces(hovertext=None)

    fig.update_layout(xaxis_rangeslider_visible=False,
        title=BigTech[i],
        yaxis_title='in $')







    fig.show()