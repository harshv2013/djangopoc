from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    news_data = models.TextField()
    location = models.ForeignKey(Location, related_name='news', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Weather(models.Model):
    weather_data = models.TextField()
    location = models.ForeignKey(Location,related_name='weathers' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class NewsWeather(models.Model):
    news_data = models.TextField()
    weather_data = models.TextField()
    location = models.ForeignKey(Location, related_name='newsweathers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)




