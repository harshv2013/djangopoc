from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from datetime import date, datetime
from businessapp.models import Location, News, Weather
from businessapp.serializers import LocationSerializer, \
    NewsSerializer, WeatherSerializer, \
    NewsWeatherSerializer, LocationNewsWeatherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
    
class LocationListCreate(APIView):
    """
    List all location, or create a new collection.
    """
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationRetriveUpdateDestroy(APIView):
    """
    Retrieve, update or delete a location instance.
    """
    def get_object(self, pk):
        try:
            # return Collection.objects.get(pk=pk)
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = LocationSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = LocationSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsListCreate(APIView):
    """
    List all news, or create new news.
    """
    def get(self, request, format=None):
        locations = News.objects.all()
        serializer = NewsSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsRetriveUpdateDestroy(APIView):
    """
    Retrieve, update or delete a news instance.
    """
    def get_object(self, pk):
        try:
            # return Collection.objects.get(pk=pk)
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = NewsSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = NewsSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WeatherListCreate(APIView):
    """
    List all weather, or create a new weather.
    """
    def get(self, request, format=None):
        locations = Weather.objects.all()
        serializer = WeatherSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherRetriveUpdateDestroy(APIView):
    """
    Retrieve, update or delete a weather instance.
    """
    def get_object(self, pk):
        try:
            # return Collection.objects.get(pk=pk)
            return Weather.objects.get(pk=pk)
        except Weather.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = WeatherSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = WeatherSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NewsWeatherList(APIView):
    """
    List all news weather.
    """
    def get(self, request, format=None):
        search_date = request.query_params.get('search_date')
        date_object = datetime.strptime(search_date, '%d-%m-%Y').date()
        context_data = {
            "search_date": date_object
        }
        locations = Location.objects.filter(name='Noida')
        serializer = NewsWeatherSerializer(locations, context=context_data, many=True)
        return Response(serializer.data)
    

class NewsWeatherList2(APIView):
    """
    List all news weather.
    # # """
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'index.html'


    def get(self, request, format=None):
        location_name = request.query_params.get('location_name')
        search_date = request.query_params.get('search_date')
        if search_date:
            date_object = datetime.strptime(search_date, '%d-%m-%Y').date()
        else:
            date_object = date.today()
        context_data = {
            "search_date": date_object
        }
        location = Location.objects.filter(name=location_name).first()
        serializer = LocationNewsWeatherSerializer(location, context=context_data)
        # return Response({'location': serializer.data})
        return Response(serializer.data) 
    
    

