from django.contrib import admin


class FazendasAdminSite(admin.AdminSite):
    title_header = 'Fazendas Admin'
    site_header = 'Fazendas Painel'
    index_title = 'Fazendas Painel'
