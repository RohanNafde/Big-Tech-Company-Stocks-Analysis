import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

BigTech = ['AAPL', 'DELL', 'HPQ', 'SSNLF', 'MSFT', 'ADBE', 'GOOGL', 'META', 'TWTR', 'SAP', 'ORCL', 'CRM', 'ZM', 'CSCO',
'IBM', 'TCEHY', 'AMZN', 'AMD', 'INTC', 'TSM', 'NVDA', 'QCOM', 'ASML', 'UBER','TSLA']
#Don't plot TWTR, META, TSLA, UBER, ZM, DELL, TCEHY, for Recession




fname = r"C:\IIT\DS203\Project\yfinance\\SAP.csv"
df = pd.read_csv(fname)


fname1= r"C:\IIT\DS203\Project\yfinance\\ORCL.csv"
df1 = pd.read_csv(fname1)

fig = make_subplots(rows=2, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.02)

fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],name="SAP",increasing_line_color= 'purple', decreasing_line_color= 'gray'),
               row=1,col=1)

fig.add_trace(go.Candlestick(x=df['Date'],
                open=df1['Open'],
                high=df1['High'],
                low=df1['Low'],
                close=df1['Close'],name="ORCL"),
               row=1,col=1)

fig.update_layout(xaxis_rangeslider_visible=False,
        title="SAP vs ORACLE",
        yaxis_title='in $'
        )
fig.show()



#1996 - Fall due to AMD K5 CPU( 5K85/6 ) was below par, hag diya
#1997 - SLight increase 