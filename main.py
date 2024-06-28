import requests
from twilio.rest import Client

api_key = "your api key"

account_sid = "your account sid"
auth_token = "your auth token"

parameter = {
    "lat": 21.152451,
    "lon": 79.080559,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()

will_rain = False
for x in range(0, 4):
    weather_data = response.json()["list"][x]["weather"][0]["id"]
    if weather_data < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It;s going to rainRemember bring an umbrella.",
        from_="+19789517779",
        to="+94721763352"
    )
    print(message.status)
