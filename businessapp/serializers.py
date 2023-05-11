
from rest_framework import serializers
from businessapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Location, News, Weather

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
        search_text = self.context.get('search_text')
        # tasks = Task.objects.filter(collection=obj)
        # TODO 1. Sorting 2. pagination 3. UnitTest
        news = News.objects.filter(location=obj).order_by("-created_at")
        if search_text:
            news = news.filter(name__icontains=search_text)
        # tasks = Task.objects.all()
        serializer = NewsSerializer(instance=news, many=True)
        return serializer.data