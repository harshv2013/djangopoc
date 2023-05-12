import requests
import json
from businessapp.models import Location, News, Weather
from workers import weather_update, news_update, weather_news_update


def my_cron_job(worker_name, location):
    worker = eval(worker_name)
    worker(location)