import requests

# Ваш API-ключ от Dadata
API_KEY = "b9bbe8cacad24b1e2a89c293e5985673b876efe5"
URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"



def get_cordinate(sity):
    API_KEY = "b9bbe8cacad24b1e2a89c293e5985673b876efe5"
    URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {API_KEY}"
    }
    payload = {
        "query": sity,
        "count": 1  # Получить только лучший вариант
    }

    response = requests.post(URL, headers=headers, json=payload)
    data = response.json()

    if data["suggestions"]:
        address_data = data["suggestions"][0]["data"]
        if "geo_lat" in address_data and "geo_lon" in address_data:
            lat = address_data["geo_lat"]  # Широта
            lon = address_data["geo_lon"]  # Долгота
            return({'lat':lat, 'lon':lon})
        else:
            return None
    else:
        return None