#!/bin/bash

python manage.py migrate
gunicorn website.wsgi:application --bind 0.0.0.0:$PORT
