# Generated by Django 4.2 on 2023-05-02 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("businessapp", "0003_location_news_weather_delete_choice_delete_question"),
    ]

    operations = [
        migrations.RenameField(
            model_name="location",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="news",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="weather",
            old_name="created",
            new_name="created_at",
        ),
    ]
