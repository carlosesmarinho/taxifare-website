import streamlit as st

#import datetime
import pandas as pd
import requests
import numpy as np



'''
### Taxifare Prediction
'''


def get_map_data():

    return pd.DataFrame(
            np.random.randn(5, 2) / [50, 50] + [40.7831, -73.9712],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)

#1. Pickup datetime:
pickup_datetime = st.text_input('Pickup datetime:', '2014-07-06 19:18:00')

#2. Pickup longitude:
pickup_longitude  = st.number_input('Insert the pickup longitude', -73.950655, format="%.6f")

#3. Pickup latitude:
pickup_latitude  = st.number_input('Insert the pickup latitude', 40.783282, format="%.6f")

#4. Dropoff longitude:
dropoff_longitude  = st.number_input('Insert the dropoff longitude', -73.984365, format="%.6f")

#5. Dropoff latitude:
dropoff_latitude  = st.number_input('Insert the dropoff latitude', 40.769802, format="%.6f")

#6. Person count:
def get_select_box_data():

    return pd.DataFrame({
          'passenger_count': list(range(1, 6))
          })

df = get_select_box_data()

passenger_count  = st.selectbox('Choose passenger number for the ride:', df['passenger_count'])

filtered_df = df[df['passenger_count'] == passenger_count]

passenger_count = int(filtered_df.iloc[0,0])


url = 'https://taxifare.lewagon.ai/predict'


if st.button('Get Fare'):
    # print is visible in the server output, not in the page
    print('Getting fare..!')
    st.write('Getting fare..! 🧙‍♂️')

    params = {
        "pickup_datetime": str(pickup_datetime),
          "pickup_longitude": str(pickup_longitude),
          "pickup_latitude": str(pickup_latitude),
          "dropoff_longitude": str(dropoff_longitude),
          "dropoff_latitude": str(dropoff_latitude),
          "passenger_count": str(passenger_count)
          }

    # Converte os parâmetros para um formato de URL (query string)
    query_params = "&".join([f"{key}={value}" for key, value in params.items()])
    full_url = f"{url}?{query_params}"

    response = requests.get(full_url)  # Agora, enviamos via GET

    if response.status_code == 200:
        prediction = response.json().get("fare", "No prediction found")
        st.success(f"Fare: {prediction}")
    else:
        st.write(response.status_code)
        st.error("Error: Could not get a response from the API")

else:
    st.write('Please, input the requested information above')
