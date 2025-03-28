import requests

# Funktion zur Abfrage der Bright Sky API
def get_weather_data(lat, lon, start_date, end_date):
    url = "https://api.brightsky.dev/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "date": start_date,
        "last_date": end_date
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["weather"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []
