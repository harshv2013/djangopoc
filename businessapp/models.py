from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)



from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

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




