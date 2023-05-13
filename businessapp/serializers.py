
from rest_framework import serializers
from businessapp.models import Location, News, Weather, NewsWeather


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'created_at']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'news_data', 'created_at', 'location']

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'weather_data', 'created_at', 'location']

class NewsWeatherSerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField()
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('name', 'created_at','weather','news')
        
    
    def get_news(self, obj):
        search_date = self.context.get('search_date')
        news = News.objects.filter(location=obj).order_by("-created_at")
        if search_date:
            news = news.filter(created_at__date=search_date)
        serializer = NewsSerializer(instance=news, many=True)
        return serializer.data
    
    def get_weather(self, obj):
        search_date = self.context.get('search_date')
        weather = Weather.objects.filter(location=obj)
        if search_date:
            weather = weather.filter(created_at__date=search_date)
        serializer = WeatherSerializer(instance=weather.last())
        return serializer.data

class NewsWeatherSerializer2(serializers.ModelSerializer):
    class Meta:
        model = NewsWeather
        fields = ['id', 'news_data', 'weather_data','created_at']


class LocationNewsWeatherSerializer(serializers.ModelSerializer):
    weathernews = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('id','name', 'created_at','weathernews')

    
    def get_weathernews(self, obj):
        search_date = self.context.get('search_date')
        newsweather = NewsWeather.objects.filter(location=obj).order_by("-created_at")
        if search_date:
            news = newsweather.filter(created_at__date=search_date)
        serializer = NewsWeatherSerializer2(instance=news, many=True)
        return serializer.data