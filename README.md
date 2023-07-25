# django-backend

## day after day building this thing

1. Docker container
    1.  docker build -t my-backend-insights-app . 
    2.  docker run -p 8000:8000 -it --rm -v "$PWD":/home/ --name my-backend-running-app my-backend-insights-app
    3.  docker exec -it 7d10f8a2560b  bash
    4.  virtualenv -p $(which python3) venv

2. guidance
    1.  https://www.youtube.com/watch?v=adQaOQmtYEg&t=143s
    2.  https://docs.djangoproject.com/en/4.2/intro/tutorial01/
    3.  https://blog.logrocket.com/django-rest-framework-create-api/
    4.  https://www.youtube.com/watch?v=i5JykvxUk_A
    4.  django-admin startproject server .
    5.  python manage.py migrate
    6.  python manage.py createsuperuser
    7.  python manage.py runserver 0.0.0.0:8000
    8.  http://127.0.0.1:8000/admin/
    9.  python manage.py makemigrations server
    10. python manage.py migrate  
    5.  cd server
    5.  django-admin startapp server_api
    7.  



    9.  docker cp 7d10f8a2560b:/home/my-app  $(pwd)/v1/


