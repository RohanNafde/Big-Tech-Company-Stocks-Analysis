import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import math

BigTech = ['AAPL', 'DELL', 'HPQ', 'SSNLF', 'MSFT', 'ADBE', 'GOOGL', 'META', 'TWTR', 'SAP', 'ORCL', 'CRM', 'ZM', 'CSCO',
'IBM', 'TCEHY', 'AMZN', 'AMD', 'INTC', 'TSM', 'NVDA', 'QCOM', 'ASML', 'UBER','TSLA']
#Don't plot TWTR, META, TSLA, UBER, ZM, DELL, TCEHY, for Recession




fname = r"C:\IIT\DS203\Project\yfinance\\ZM.csv"
df = pd.read_csv(fname)
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close']
                )])

# For info on x-axis ::  fig.update_traces(hovertext=None)


fig.update_layout(xaxis_rangeslider_visible=False,
        title="Zoom",
        yaxis_title='in $'
        )



fig.add_annotation(x='2020-04-10', y= '160',
            text="Covid Outbreak",
            showarrow=True,
            arrowhead=1,
            font=dict(size=16)
    )

fig.add_annotation(x='2020-10-15', y= '565',
            text="Peak of Wave 1",
            showarrow=True,
            arrowhead=1,
            font=dict(size=16)
    )
    

fig.show()

#1996 - Fall due to AMD K5 CPU( 5K85/6 ) was below par, hag diya
#1997 - SLight increase 