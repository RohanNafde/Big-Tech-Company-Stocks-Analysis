import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import math

agg = pd.read_csv(r"C:\IIT\DS203\Project\agg.csv") 

fig = go.Figure(data=[go.Candlestick(x=agg['Date'],
                open=agg['Open'],
                high=agg['High'],
                low=agg['Low'],
                close=agg['Close'])])


fig.update_layout(xaxis_rangeslider_visible=False,
        title='Aggregate Share Prices',
        yaxis_title='in $',
        shapes = [dict(
            x0='2007-07-05', x1='2009-05-10', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2007-07-15', y=0.5, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='2008 Recession',font=dict(size=18))]
            # For info on x-axis  ::  ,hovermode="x"
        )

decline = fig.add_annotation(x='2022-03-25', y= '18000',
            text="2022 Stock Decline",
            showarrow=True,
            arrowhead=1,
            font=dict(size=18),
            align="center",
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
    )

decline.update_annotations(hovertext="Feb 2022: Russia-Ukraine War + Financial Instabilty => 2022 Deline")


covid = fig.add_annotation(x='2020-03-30', y= '8050',
            text="Covid Outbreak",
            showarrow=True,
            arrowhead=1,
            font=dict(size=18),
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
    )


brexit = fig.add_annotation(x='2016-01-30', y= '4000',
            text="Brexit Announced",
            showarrow=True,
            arrowhead=1,
            font=dict(size=18),
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
    )


fig.show()