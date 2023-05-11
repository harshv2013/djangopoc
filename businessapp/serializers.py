
from rest_framework import serializers
from businessapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Location, News, Weather, NewsWeather

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        # fields = '__all__'
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
    # weathers  = serializers.SerializerMethodField()
    # newss = serializers.StringRelatedField(many=True)

    # news = NewsSerializer(many=True, read_only=True)
    # weathers = WeatherSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('name', 'created_at','news')
        # fields = ('name', 'created_at')

    # def get_news(self, obj):
    #     print('obj======',obj.news)
    #     return obj
    
    # def get_weathers(self, obj):
    #     return obj
    
    def get_news(self, obj):
        search_date = self.context.get('search_date')
        # tasks = Task.objects.filter(collection=obj)
        # TODO 1. Sorting 2. pagination 3. UnitTest
        news = News.objects.filter(location=obj).order_by("-created_at")
        print('search_date in serializer=======>>>>',search_date)
        if search_date:
            news = news.filter(created_at__date=search_date)
        # tasks = Task.objects.all()
        serializer = NewsSerializer(instance=news, many=True)
        return serializer.data
    
#####################################################################

class NewsWeatherSerializer2(serializers.ModelSerializer):
    class Meta:
        model = NewsWeather
        fields = ['id', 'news_data', 'weather_data','created_at']


class LocationNewsWeatherSerializer(serializers.ModelSerializer):
    weathernews = serializers.SerializerMethodField()
    # weathers  = serializers.SerializerMethodField()
    # newss = serializers.StringRelatedField(many=True)

    # news = NewsSerializer(many=True, read_only=True)
    # weathers = WeatherSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id','name', 'created_at','weathernews')
        # fields = ('name', 'created_at')

    # def get_news(self, obj):
    #     print('obj======',obj.news)
    #     return obj
    
    # def get_weathers(self, obj):
    #     return obj
    
    def get_weathernews(self, obj):
        search_date = self.context.get('search_date')
        # tasks = Task.objects.filter(collection=obj)
        # TODO 1. Sorting 2. pagination 3. UnitTest
        newsweather = NewsWeather.objects.filter(location=obj).order_by("-created_at")
        print('search_date in serializer=======>>>>',search_date)
        if search_date:
            news = newsweather.filter(created_at__date=search_date)
        # tasks = Task.objects.all()
        serializer = NewsWeatherSerializer2(instance=news, many=True)
        return serializer.data