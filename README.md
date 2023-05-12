# djangopoc
## Clone the project.
### Create .env file.
### Add these in .env file.
### WORKER_NAME=<weather_news_update> Example: weather_update, news_update, weather_news_update
### LOCATION=<location name> Example: Delhi
### START_TIME=<cron time > Example:  0 12 * * * (cron job time as 12 noon)

### Run this command after any changes in cron job: python manage.py crontab add

### Run the migrations : python manage.py migrate

### Run the project: python manage.py runserver