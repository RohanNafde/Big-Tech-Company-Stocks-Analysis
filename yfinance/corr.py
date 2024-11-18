import pandas as pd
from pandas_datareader import data
import numpy as np
import random as rnd
import datetime

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

# plotly
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cufflinks as cf
cf.go_offline()

# web scraping
import requests
import bs4
import csv
import json 
import re
from io import StringIO

stock_list = ['AAPL', 'DELL', 'HPQ', 'SSNLF', 'MSFT', 'ADBE', 'GOOGL', 'META', 
            'TWTR', 'SAP', 'ORCL', 'CRM', 'ZM', 'CSCO', 'IBM', 'TCEHY', 'AMZN', 
            'AMD', 'INTC', 'TSM', 'NVDA', 'QCOM', 'ASML','UBER', 'TSLA']

opening_df = pd.DataFrame()
monthly_opening = pd.DataFrame()

for name in stock_list:
    # read files
    fname = r"C:\IIT\DS203\Project\yfinance\\" + name + ".csv"
    df = pd.read_csv(fname)

    opening_df[name] = df['Open']

Matrix = opening_df.corr(method='pearson')
fig, ax = plt.subplots()
sns.heatmap(abs(Matrix), annot=False)
plt.show()