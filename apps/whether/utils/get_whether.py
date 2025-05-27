import requests
from datetime import datetime

# Базовые параметры API


def whether (dict):
    url = "https://api.open-meteo.com/v1/forecast"
    latitude = dict.get('lat')
    longitude = dict.get('lon')

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": 3,
        "timezone": "auto",
        "temperature_unit": "celsius",

    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather_list = []
        for i in range(0, len(data["hourly"]["time"]), 4):
            time = data["hourly"]["time"][i]
            temp = data["hourly"]["temperature_2m"][i]
            dt = datetime.strptime(time, "%Y-%m-%dT%H:%M")
            formatted_time = dt.strftime("%d.%m %H:%M")
            weather_list.append([formatted_time, temp])

        return weather_list

    except Exception as e:
        return None