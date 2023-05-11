from django.urls import path
from .views import index,LocationListCreate, LocationRetriveUpdateDestroy, \
    NewsListCreate, NewsRetriveUpdateDestroy, \
    WeatherListCreate, WeatherRetriveUpdateDestroy, \
    NewsWeatherList, NewsWeatherList2



from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from businessapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path('locations/', LocationListCreate.as_view()),
    path('locations/<int:pk>/', LocationRetriveUpdateDestroy.as_view()),

    path('news/', NewsListCreate.as_view()),
    path('news/<int:pk>/', NewsRetriveUpdateDestroy.as_view()),


    path('weathers/', WeatherListCreate.as_view()),
    path('weathers/<int:pk>/', WeatherRetriveUpdateDestroy.as_view()),

    path('newsweather/', NewsWeatherList.as_view()),
    path('newsweather2/', NewsWeatherList2.as_view()),

    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)