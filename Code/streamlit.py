import streamlit as st 
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
import streamlit_folium as sf
from streamlit_folium import st_folium
import calendar

st.title('Violation Vision: See the Bigger Picture of Parking Tickets')

df = pd.read_csv('Data\SYRParking Violations\Parking_Violations_-_2023_-_Present.csv')
parking_tickets = pd.DataFrame(df)

st.header('Background') 
st.write('The following data is a collection of parking violations in Syracuse, NY from 2023 to the present. The data includes the date and time of the violation, the location of the violation, the type of violation, and the fine amount. The data is collected from the City of Syracuse Open Data Portal.')
st.write(parking_tickets.head(15))

st.header('Exploring the Data')
col1, col2 = st.columns(2)

with col1:
    time_items = ["Days of Week", "Months by Week", "Time of Day"]
    st.write("Time Based Data") 
    str_choice = st.selectbox('Select a Time Value to Analyze', time_items)
    if str_choice == "Days of Week":
        st.image("Data\Graphs\Days_of_week_graph.jpg")
        st.write("The most tickets appear to be given out at the beginning of the week.")
    if str_choice == "Months by Week":
        st.image("Data\Graphs\Months_by_week_in_month.jpg")
        st.write("There appears to be a dip in the bumber of tickets given out during the summer months and December. Additionally, week 4 tends to be the most heavily ticketed week of each month.")
    if str_choice == "Time of Day":
        st.image("Data\Graphs\Time_of_issued_tickets.jpg")
        st.write("The timeframe from 9:00am to 12pm is the dominating timeframe to get a parking ticket but a significant amount")
    
    
with col2:
    price_items = ['Ticket Price Variance', "Ticket Price per Month"]
    st.write("Ticket Price Trends ")
    str_choice = st.selectbox('Select a Price Value to Analyze', price_items)

    if str_choice == 'Ticket Price Variance':
        st.image("Data\Graphs\Ticket_amount.jpg")
        st.write("The mnost common ticket price is $30")
    if str_choice == 'Ticket Price per Month':
        st.image("Data/Graphs/Price_of_ticket_per_month.png")
        st.write("Accross all months, prices of tickets appear to to be at their highest at the end of the month.")
    
st.header('What Type of Violations are Most Common?')
st.image("Data\Graphs\Figure_1.png")
st.write("The most common type of violation is an Overtime Parking Mon-Sat 9am-6pm CO15-383.")

st.header("Exploring the Sub-Divisions of Syracuse")
st.image("Data\Graphs\Graph_of_Syracuse_towns.png", caption = "Syracuse has 21 sub-divisions.")
st.image("Data\Graphs\Barplot_Tickets_per_town.png")
st.write("It appears that a heavy majority of tickets are given within the City of Syracuse with Salina in second, but however is significantly less than the City of Syracuse.")


        
    