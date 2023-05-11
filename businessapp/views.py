from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView

from datetime import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from businessapp.models import Snippet, Location, News, Weather
from businessapp.serializers import SnippetSerializer, \
    LocationSerializer, NewsSerializer, WeatherSerializer, \
    NewsWeatherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

##########################################################################
class LocationListCreate(APIView):
    """
    List all location, or create a new collection.
    """
    def get(self, request, format=None):
        locations = Location.objects.all()
        print('location===================',locations[0].__dict__)
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



##########################################################################


##########################################################################

##########################################################################
class NewsListCreate(APIView):
    """
    List all location, or create a new collection.
    """
    def get(self, request, format=None):
        locations = News.objects.all()
        print('location===================',locations[0].__dict__)
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
    Retrieve, update or delete a location instance.
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



##########################################################################

##########################################################################
class WeatherListCreate(APIView):
    """
    List all location, or create a new collection.
    """
    def get(self, request, format=None):
        locations = Weather.objects.all()
        print('location===================',locations[0].__dict__)
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
    Retrieve, update or delete a location instance.
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



##########################################################################

class NewsWeatherList(APIView):
    """
    List all location, or create a new collection.
    """
    def get(self, request, format=None):
        search_date = request.query_params.get('search_date')
        date_object = datetime.strptime(search_date, '%m-%d-%Y').date()
        context_data = {
            "search_date": date_object
        }
        print('search_date=================',type(date_object))
        # locations = Location.objects.all()
        locations = Location.objects.filter(name='Noida')
        print('location===================',locations[0].__dict__)
        serializer = NewsWeatherSerializer(locations, many=True)
        print('serializer.data============',serializer.data)
        return Response(serializer.data)
