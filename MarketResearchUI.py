#Stock market dashboard to show some stock charts and their last one year data

#Import the libraries

import streamlit as st
import pandas as pd
from PIL import Image

#add a title and an Image

st.write("""
# stock market UI and **graphs** for last one year
""")

image =  Image.open("C:/Users/deepa/PycharmProjects/pythonProject/image.jpg")
st.Image(Image, use_column_width=True)

#create a sidebar header
st.sidebar.header('User Imput')

#create a function to get the users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "07-Feb-2020")
    end_date = st.sidebar.text_input("End Date", "07-Feb-2021")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "ECLX")
    return start_date, end_date, stock_symbol

#create a function to get company name

def get_company_name(symbol):
    if symbol == 'ECLX':
        return 'ECLERX'
    elif symbol == 'INFY':
        return 'INFOSYS'
    elif symbol == 'SBI':
        return 'SBIN'
    elif symbol == 'TATA':
        return 'TATAMOTORS'
    elif symbol == 'TCS':
        return 'TATA CONSULTANCY SERVICES'
    else
        'None'
        
#Create a funtion to get the data seta nd time frame

def get_data(symbol, start, end):

    #Load the data
    if symbol.upper()== 'ECLX':
        df=pd.read_csv("C:/Users/deepa/PycharmProjects/pythonProject/Quote-Equity-ECLERX-EQ-07-02-2020-to-07-02-2021.csv")
    elif symbol.upper() == 'INFY':
        df = pd.read_csv("C:/Users/deepa/PycharmProjects/pythonProject/Quote-Equity-INFY-EQ-07-02-2020-to-07-02-2021.csv")
    elif symbol.upper() == 'SBI':
        df = pd.read_csv("C:/Users/deepa/PycharmProjects/pythonProject/Quote-Equity-SBIN-EQ-07-02-2020-to-07-02-2021.csv")
    elif symbol.upper() == 'TATA':
        df = pd.read_csv("C:/Users/deepa/PycharmProjects/pythonProject/Quote-Equity-TATAMOTORS-EQ-07-02-2020-to-07-02-2021.csv")
    elif symbol.upper() == 'TCS':
        df = pd.read_csv("C:/Users/deepa/PycharmProjects/pythonProject/Quote-Equity-TCS-EQ-07-02-2020-to-07-02-2021.csv")
    else:
        df = pd.Dataframe(columns = ['Date', "series ","OPEN ","HIGH ","LOW ","PREV. CLOSE ","ltp ","close ","vwap ","52W H ","52W L ","VOLUME ","VALUE", "NO OF TRADERS"])

    #get the date range

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #set the start and end index

    start_row= 0
    end_row= 0

    for i in range(0, len(df)):
        if start <=pd.to_datetime(df['Date'][i] ):
            start_row=i
            break

    #start from the bottom of the dateset
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 -j
            break

    #set the index to be the date
    df = df.set_index(pd.datetimeindex(['Date'].values))

    return df.iloc[start_row:end_row +1, :]

#Get the users input
start, end, symbol = get.input()

#get the data
df = get_data(symbol,start, end)

#get the compnay name
company_name = get_company_name(symbol.upper())

#display the close price

st.header(company_name+" Close Price\n")
st.line_chart(df['close'])

#display the volume

st.header(company_name+ "Volume\n")
st.line_chart(df['Volume'])

#get the statistics
st1.header('Data Statistics')
st.write(df.describe())

