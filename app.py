import streamlit as st

#import datetime
import pandas as pd
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

#1. Date and time:
#pickup_datetime  = st.date_input(
#    "Pickup datetime:",
 #   datetime.datetime(2019, 7, 6, 8, 45))
#st.write('Pickup date is:', pickup_datetime )

pickup_datetime = st.text_input('Pickup datetime:', '2014-07-06 19:18:00')

#st.write('Pickup date is', pickup_datetime)


#2. Pickup longitude:
pickup_longitude  = st.number_input('Insert the pickup longitude', -73.950655, format="%.6f")
#st.write('Pickup longitude is ', pickup_longitude )

#3. Pickup latitude:
pickup_latitude  = st.number_input('Insert the pickup latitude', 40.783282, format="%.6f")
#st.write('Pickup latitude is ', pickup_latitude )

#4. Dropoff longitude:
dropoff_longitude  = st.number_input('Insert the dropoff longitude', -73.984365, format="%.6f")
#st.write('Dropoff longitude is ', dropoff_longitude )

#5. Dropoff latitude:
dropoff_latitude  = st.number_input('Insert the dropoff latitude', 40.769802, format="%.6f")
#st.write('Dropoff latitude is ', dropoff_latitude )

#6. Person count:
def get_select_box_data():

    return pd.DataFrame({
          'passenger_count': list(range(1, 6))
          })

df = get_select_box_data()

passenger_count  = st.selectbox('Choose passenger number for the ride:', df['passenger_count'])

filtered_df = df[df['passenger_count'] == passenger_count]

passenger_count = int(filtered_df.iloc[0,0])

#st.write('total passenger is :', passenger_count)



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''



if st.button('Get Fare'):
    # print is visible in the server output, not in the page
    print('Getting fare..!')
    st.write('Getting fare..! 🎉')

    params = {
        "pickup_datetime": str(pickup_datetime),
          "pickup_longitude": str(pickup_longitude),
          "pickup_latitude": str(pickup_latitude),
          "dropoff_longitude": str(dropoff_longitude),
          "dropoff_latitude": str(dropoff_latitude),
          "passenger_count": str(passenger_count)
          }

    #response = requests.post(url, headers=params)

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
    st.write('Please, input the requested information')
