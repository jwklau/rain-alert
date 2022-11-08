import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("/Users/jenniferlau/Python/EnvironmentVariables/.env")

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = float(os.getenv("RainAppMyLat"))
MY_LONG = float(os.getenv("RainAppMyLong"))
API_KEY = os.getenv("RainAppAPIKey")
account_sid = os.getenv("RainAppAccountSid")
auth_token = os.getenv("RainAppAuthToken")

TEST_NUM = os.getenv("TestNum")
MY_MOBILE = os.getenv("MyMobile")
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"

}
response = requests.get(url=OWM_ENDPOINT, params= parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in range(12):
    condition_code = weather_data["hourly"][hour]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=TEST_NUM,
        to=MY_MOBILE
    )
    print(message.status)