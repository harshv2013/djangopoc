# Generated by Django 4.2 on 2023-05-12 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("businessapp", "0007_newsweather"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Snippet",
        ),
    ]