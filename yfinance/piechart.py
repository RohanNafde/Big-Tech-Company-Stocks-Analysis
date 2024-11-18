import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import math
import numpy as np





#marketcap = np.empty(len(all),dtype = float)
#market cap for 2022, November. Volume * Closing Price for 09, November 2022


# for i in range(0,len(all)):
#     fname = r"C:\Users\Varad Deshpande\Desktop\DS203 Project\ds203_tech_stocks\BigTech\\" + all[i] + ".csv"
#     df = pd.read_csv(fname)
#     marketcap[i] = (df.iloc[df.shape[0]-1,4] * df.iloc[df.shape[0]-1,6])/1E9


#Data from : https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/
#as on 27-11-22

marketcap = [2356,1844,1261,952,569,422,405,331,301,295,238,223,214,199,198,160,155,153,138,132,129,127,121,110]
all = ['AAPL','MSFT','GOOGLE','AMZN','TSLA','TSMC','NVDA','TCEHY','SSNLF','META','ASML'
,'ORCL','AVGO','BABA','CSCO','TXN','ADBE','CRM','QCOM','IBM','SAP','NFLX','AMD','INTC','INTU']
fig = go.Figure()
fig.add_trace(go.Pie(values=marketcap,labels=all, pull=[0.1, 0, 0, 0, 0], hole=.35))
fig.update_traces(textinfo='percent+label',textposition='inside',hoverinfo='value+label')
fig.update_layout(height=800,title_text='Market Capital,in Billions(November, 2022)')
fig.show()