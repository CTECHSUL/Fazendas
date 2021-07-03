<h1>Cadastro de fazendas</h1>

* Setup inicial com Django 3.2 (Python 3.8.6) e SQLite 3.12.2
* Criação de modelo de dados para o mapeamento de entidades em bancos de dados
* Desenvolvimento de operações de gerenciamento de fazendas (Cadastro(com upload de arquivos), leitura e atualização).

Para executar o projeto:

shell script
```
python3 -m pip install django
```
```
python3 -m pip install django-money
```
```
python3 -m pip install Pillow
```
```
git clone https://github.com/CTECHSUL/Fazendas
```
```
cd Fazendas
```
Editar o arquivo fazendas/settings.py para rodar em localhost
```
ALLOWED_HOSTS = ['192.168.0.13']
ALLOWED_HOSTS = []
```
Depois:
```
python3 manage.py runserver
```
Rodando em:
```
http://localhost:8080
```
<hr>
Referências do projeto:

* [Django](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/index.html)
* [Pillow](https://python-pillow.org/)
* [Bootsrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
* [Django Money](https://github.com/django-money/django-money)
* [FontAwasome](https://fontawesome.com/)
