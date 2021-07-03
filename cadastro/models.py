from django.db import models
from django.contrib import auth
from djmoney.models.fields import MoneyField


class Fazenda(models.Model):

    nome = models.CharField(
        max_length=50,
        help_text="Nome da fazenda."
    )

    municipio = models.CharField(
        max_length=100,
        help_text="Município."

    )

    estado = models.CharField(
        max_length=5,
        help_text="Estado."
    )

    area_total = models.IntegerField(
        help_text="Área total (Hectare)."
    )

    area_aberta = models.IntegerField(
        help_text="Área aberta (Hectare)."
    )

    cultura = models.CharField(
        max_length=255,
        help_text="Cultura."
    )
    infra = models.CharField(
        max_length=255,
        help_text="Características de infraestrutura."
    )

    maquinario = models.CharField(
        max_length=255,
        help_text="Maquinário (Trator, caminhão, carro e etc...)"
    )

    local_ref = models.CharField(
        max_length=255,
        help_text="Referências de localização."
    )

    coordenada = models.CharField(
        max_length=100,
        help_text="Coordenadas."

    )

    valor = MoneyField(
        max_digits=14, 
        decimal_places=2,
        default_currency='BRL'
    )

    obs = models.TextField(
        max_length=3000,
        help_text="Observações."

    )

    encaminhado = models.CharField(
        max_length=50,
        help_text="Encaminhado por."
    )

    oferta = models.CharField(
        max_length=50,
        help_text="Ofertada para."
    )


class FazendaMedia(models.Model):

    fazenda = models.ForeignKey(
        Fazenda,
        on_delete=models.CASCADE
    )    

    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='imagens/',
        
    )

    video = models.FileField(
        null=True,
        blank=True,
        upload_to='videos/',
        
    )

    audio = models.FileField(
        null=True,
        blank=True,
        upload_to='audios/',
        
    )