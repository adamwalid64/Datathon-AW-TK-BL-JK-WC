import pandas as pd 
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
import streamlit_folium as sf
from streamlit_folium import st_folium
import matplotlib.pyplot as plt


parkingVioData = pd.read_csv('Data\SYRParking Violations\Parking_Violations_-_2023_-_Present.csv')
df = pd.DataFrame(parkingVioData)
print(parkingVioData.head())
print(parkingVioData.columns)

parkingVioData.plot()


subdata = {
    "Name": [
        "City of Syracuse",
        "Onondaga Nation Reservation",
        "Town of Camillus",
        "Town of Cicero",
        "Town of Clay",
        "Town of De Witt",
        "Town of Elbridge",
        "Town of Fabius",
        "Town of Geddes",
        "Town of LaFayette",
        "Town of Lysander",
        "Town of Manlius",
        "Town of Marcellus",
        "Town of Onondaga",
        "Town of Otisco",
        "Town of Pompey",
        "Town of Salina",
        "Town of Skaneateles",
        "Town of Spafford",
        "Town of Tully",
        "Town of Van Buren"
    ],
    "Latitude": [
        43.0481,
        42.9545,
        43.0390,
        43.1759,
        43.1850,
        43.0387,
        43.0348,
        42.8417,
        43.0734,
        42.8981,
        43.1617,
        43.0026,
        42.9820,
        42.9784,
        42.8412,
        42.8881,
        43.1131,
        42.9467,
        42.8120,
        42.7998,
        43.1256
    ],
    "Longitude": [
        -76.1474,
        -76.1444,
        -76.3041,
        -76.1256,
        -76.1728,
        -76.0723,
        -76.4391,
        -75.9896,
        -76.2102,
        -76.1041,
        -76.3323,
        -75.9766,
        -76.3413,
        -76.1784,
        -76.2455,
        -76.0063,
        -76.1938,
        -76.4294,
        -76.3155,
        -76.1063,
        -76.3650
    ]
}

subdivisions = pd.DataFrame(subdata)





