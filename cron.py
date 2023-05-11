import requests
import json
from businessapp.models import Location, News, Weather
from workers import weather_update, news_update, weather_news_update

l = Location.objects.filter(name="Delhi").first()

url = "http://localhost:8000/businessapp/weathers/"

payload = json.dumps({
  "weather_data": "Its test weather data4s",
  "location": 1
})
headers = {
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)


def my_cron_job(worker_name, location):
    print('testing cron job harsh======================')
    # location_name = "Noida"
    # location_name = location
    # weather_update(location_name)
    # worker_name(location)
    worker = eval(worker_name)
    # weather_update(location)
    worker(location)
    # Weather.objects.create(weather_data="This is hv-test weather3", location=l)
    # response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)