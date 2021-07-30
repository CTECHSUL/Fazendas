from django.apps import AppConfig
from django.contrib.admin import apps

class CadastroConfig(AppConfig):
    name = 'cadastro'

class CadastroAdminConfig(apps.AdminConfig):
    default_site = 'admin.FazendasAdminSite'