import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import math

BigTech = ['AAPL', 'DELL', 'HPQ', 'SSNLF', 'MSFT', 'ADBE', 'GOOGL', 'META', 'TWTR', 'SAP', 'ORCL', 'CRM', 'ZM', 'CSCO',
'IBM', 'TCEHY', 'AMZN', 'AMD', 'INTC', 'TSM', 'NVDA', 'QCOM', 'ASML', 'UBER','TSLA']
#Don't plot TWTR, META, TSLA, UBER, ZM, DELL, TCEHY, for Recession




fname = r"C:\IIT\DS203\Project\yfinance\AMDlongago.csv"
df = pd.read_csv(fname)
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close']
                )])

# For info on x-axis ::  fig.update_traces(hovertext=None)


fig.update_layout(xaxis_rangeslider_visible=False,
        title="AMD",
        yaxis_title='in $',
        shapes = [dict(
            x0='2018-09-09', x1='2022-10-10', y0=0, y1=1, xref='x', yref='paper',
            line_width=1.35)],
        annotations=[dict(
            x='2018-06-05', y=0.85, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Launch of Ryzen',
            font=dict(size=16))]
            # For info on x-axis  ::  ,hovermode="x"
        )



fig.add_annotation(x='2018-09-15', y= '30',
            text="Ryzen 2000 Series launched",
            showarrow=True,
            arrowhead=1,
            font=dict(size=16)
    )

fig.add_annotation(x='2014-02-15', y= '7',
            text="Neared Bankruptcy",
            showarrow=True,
            arrowhead=1,
            font=dict(size=16)
    )
    

fig.show()

#1996 - Fall due to AMD K5 CPU( 5K85/6 ) was below par, hag diya
#1997 - SLight increase 