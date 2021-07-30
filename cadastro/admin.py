from django.contrib import admin
from cadastro.models import Fazenda, FazendaMedia

class FazendaAdmin(admin.ModelAdmin):
    list_display = ('municipio', 'estado', 'area_total', 'area_aberta', 'valor', 'encaminhado')
    list_filter = ('encaminhado', 'oferta')
    search_fields = ('estado', 'municipio', 'encaminhado')

admin.site.register(Fazenda, FazendaAdmin)
admin.site.register(FazendaMedia)