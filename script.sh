#!/bin/bash

python manage.py reset_db --noinput
python manage.py clear_cache
python manage.py clean_pyc
find . -name '__pycache__' -type d -exec rm -r {} +
python manage.py makemigrations
python manage.py migrate
python manage.py create_users
python manage.py runserver
