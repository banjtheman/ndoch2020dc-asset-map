import json
import requests


import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import altair as alt



@st.cache
def load_csv(csv_path):
    return pd.read_csv(csv_path)




def mark_map(row, m, map_lat, map_long, cols):

    curr_lat = row[map_lat]
    curr_long = row[map_long]

    tooltip_string = ""

    for col in cols:
        tooltip_string += "<b>" + str(col) + ": </b>" + str(row[col]) + "<br>"

    folium.Marker(
        [curr_lat, curr_long], popup=tooltip_string, tooltip=tooltip_string
    ).add_to(m)




def sidebar_options():
    #TODO what options do we want to have here
    st.sidebar.header("Hello")


def get_assets():
    #TODO

    #Get the data from the dc drop box
    return 0


def load_map(assets):
    #TODO

    st.title("Civic Day of Hacking Asset Map")

    sidebar_options()


    st.header("This is our asset map")

    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    tooltip = "Liberty Bell"
    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)


    # now place a marker for each row in df
    # df.apply(
    #     lambda row: mark_map(row, m, map_lat, map_long, df.columns), axis=1
    #         )


    # call to render Folium map in Streamlit
    folium_static(m)


def main():

    #query_params = st.experimental_get_query_params()
    #key = query_params["key"][0]

    assets = get_assets()
    load_map(assets)





if __name__ == "__main__":
    main()