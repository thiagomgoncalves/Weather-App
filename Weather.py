import requests
import streamlit as st


# Streamlit app title
st.title("Weather")

# User input for city name
city = st.text_input("Cidade:")

# Make API call to weather API
if city:
    # API endpoint and parameters
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "aebc4e75af3e60585255ce6f06afea5c",
        "lang":"pt",
        "units":"metric"
    }

    # Send GET request to the API
    response = requests.get(url, params=params)
    data = response.json()

    # Extract temperature information from JSON response
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        # Display weather information to the user
        st.write(f"Temperatura em {city}: {temperature}°C")
        st.write(f"Sensação: {feels_like}°C")
        st.write(f"Descrição: {description}")
    else:
        st.write("Error: Unable to retrieve weather information.")