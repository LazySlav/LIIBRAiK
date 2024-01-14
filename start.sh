#!/bin/bash

python django/manage.py makemigrations LIIBRAiK
python django/manage.py migrate
python django/manage.py runserver 0.0.0.0:8000 --insecure