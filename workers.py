from businessapp.models import Location, News, Weather, NewsWeather

from faker import Faker

# fake = Faker()

# l = Location.objects.filter(name="Delhi").first()

# Weather.objects.create(weather_data="This is hv-test weather", location=l)

def weather_update(location_name):
    location = Location.objects.filter(name=location_name).first()
    # weather_data = "This is hv-test weather"
    fake = Faker()
    weather_data = fake.sentence()
    Weather.objects.create(weather_data=weather_data, location=location)

def news_update(location_name):
    location = Location.objects.filter(name=location_name).first()
    # news="This is news_data1"
    # news_data=fake.text()
    generateNews = Faker()
    news = generateNews.text() 
    News.objects.create(news_data=news, location=location)

def weather_news_update(location_name):
    location = Location.objects.filter(name=location_name).first()
    # weather_data = fake.sentence()
    # news_data=fake.text()
    # news_data="test hv-news_data"
    # weather_data = "This is hv-test weather"
    generateNewsWeather = Faker()
    news = generateNewsWeather.text() 
    weather = generateNewsWeather.sentence()
    NewsWeather.objects.create(news_data=news, weather_data=weather, location=location)
