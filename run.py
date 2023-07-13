import os

# makemigrations
os.system("python manage.py makemigrations")

# migrate
os.system("python manage.py migrate")

# runserver
os.system("python manage.py runserver")