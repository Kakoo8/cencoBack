
Iniciar Virtual Environment:
```

$ cd Scripts
$ activate
```
volvemos a la carpeta raiz del proyecto
```
(env)$ cd ..
(env)$ cd  djangoWeather

```
Instalar Dependencias:

```
(env)$ pip install -r requerimientos.txt
```


Desplegamos la aplicacion
```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
En otro entorno virual nos dirigimos a la carpeta djangoWeather y activamos Celery
```
celery -A djangoWeather beat -l INFO
```