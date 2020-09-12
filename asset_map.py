import json
import requests


import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import altair as alt








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


def load_map():
    #TODO

    st.title("Civic Day of Hacking Asset Map")

    sidebar_options()

    st.header("This is our asset map")

    map_lat = "MAR_LATITUDE"
    map_long = "MAR_LONGITUDE"




    df = pd.read_csv("data/full_ballot_data.csv", dtype={map_lat: float, map_long: float})
    # st.dataframe(df)
    st.write("")
    st.write("")

    first_lat = df[map_lat].mean()
    first_long = df[map_long].mean()

    m = folium.Map(location=[first_lat, first_long], zoom_start=16)

    # now place a marker for each row in df
    df.apply(
            lambda row: mark_map(row, m, map_lat, map_long, df.columns), axis=1
            )

    # might be able to hard code it here

    folium_static(m)


def main():

    #query_params = st.experimental_get_query_params()
    #key = query_params["key"][0]

    load_map()





if __name__ == "__main__":
    main()