<h1>Cadastro de fazendas</h1>

* Setup Django 3.2 (Python 3.8.6).
* Creation of a data model for mapping entities in databases.
* Development of farm management operations (Registration (with file upload), reading and updating).

Run:

shell script
```
python3 -m pip install django django-money Pillow filetype
```
```
git clone https://github.com/CTECHSUL/Fazendas
```
```
cd Fazendas
```
Edit fazendas/settings.py to run on localhost
```
ALLOWED_HOSTS = ['192.168.0.13']
ALLOWED_HOSTS = []
```
Run:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
<hr>
Referências do projeto:

* [Django](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/index.html)
* [Pillow](https://python-pillow.org/)
* [filetype](https://github.com/h2non/filetype.py)
* [Bootsrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
* [Django Money](https://github.com/django-money/django-money)
* [FontAwasome](https://fontawesome.com/)
