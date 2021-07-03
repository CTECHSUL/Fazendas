from django import forms
from djmoney.forms import MoneyField
from django.forms import ModelForm, Form

from .models import Fazenda, FazendaMedia
import re

estados = (('',''),('AC','Acre AC'),('AL','Alagoas AL'),('AP','Amapá AP'),
            ('AM','Amazonas AM'),('BA','Bahia BA'),('CE','Ceará CE'),
            ('DF','Distrito Federal DF'),('ES','Espírito Santo ES'),
            ('GO','Goiás GO'),('MA','Maranhão MA'),('MT','Mato Grosso MT'),
            ('MS','Mato Grosso do Sul MS'),('MG','Minas Gerais MG'),('PA','Pará PA'),
            ('PB','Paraíba PB'),('PR','Paraná PR'),('PE','Pernambuco PE'),('PI','Piauí PI'),
            ('RJ','Rio de Janeiro RJ'),('RN','Rio Grande do Norte RN'),
            ('RS','Rio Grande do Sul RS'),('RO','Rondônia RO'),('RR','Roraima RR'),
            ('SC','Santa Catarina SC'),('SP','São Paulo SP'),('SE','Sergipe SE'),
            ('TO','Tocantins TO'))

culturas = (('Lavoura','Lavoura'),('Pecuária','Pecuária'),('Dupla Aptidão','Dupla Aptidão'))

class FazendaForm(ModelForm):
    class Meta:
        model = Fazenda
        fields = ('nome', 'municipio', 'estado', 
                'area_total', 'area_aberta',
                'cultura', 'infra', 'maquinario',
                'local_ref', 'coordenada', 'valor',
                'obs', 'encaminhado', 'oferta')

    nome = forms.CharField(label='nome', widget=forms.TextInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))
    
    municipio = forms.CharField(label='municipio', widget=forms.TextInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'})) 

    estado = forms.CharField(label='estado', widget=forms.Select({
        "style": "font-size: large",
        'class':'form-control mr-sm-2'},
        choices=estados))

    area_total = forms.IntegerField(label='area_total',widget=forms.NumberInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))

    area_aberta = forms.IntegerField(label='area_aberta',widget=forms.NumberInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))

    cultura = forms.CharField(label='cultura', widget=forms.Select(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'},
        choices=culturas))

    infra = forms.CharField(label='infra', widget=forms.Textarea(
        attrs={ "autocomplete":"off", 
        "style": "font-size: large",
        'class':'form-control mr-sm-2',
        'cols': '30',
        'rows': '4'}))

    maquinario = forms.CharField(label='maquinario', widget=forms.Textarea(
        attrs={ "autocomplete":"off", 
        "style": "font-size: large",
        'class':'form-control mr-sm-2',
        'cols': '30',
        'rows': '4'}))

    local_ref = forms.CharField(label='local_ref', widget=forms.TextInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))
    
    coordenada = forms.CharField(label='coordenada', widget=forms.TextInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))
    
    valor = forms.Form('valor',)

    obs = forms.CharField(label='obs', widget=forms.Textarea(
        attrs={ "autocomplete":"off", 
        "style": "font-size: large",
        'class':'form-control mr-sm-2',
        'cols': '30',
        'rows': '4' }))
    
    encaminhado = forms.CharField(label='encaminhado', widget=forms.TextInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))

    oferta = forms.CharField(label='oferta', widget=forms.TextInput(
        attrs={ "autocomplete":"off", "style": "font-size: large",
        'class':'form-control mr-sm-2'}))


class UploadMedia(forms.Form):
    class Meta:
        model = FazendaMedia
        fields = ('imagem', 'video', 'audio')

    imagens = forms.FileField(label='imagem', required=False, 
        widget=forms.ClearableFileInput(attrs={'multiple': True,}))
    
    videos = forms.FileField(label='video', required=False, 
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    audios = forms.FileField(label='audio', required=False, 
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

class SearchForm(forms.Form):
    
    estado = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control',}), #'style':r'padding-left: calc(50% - 1em)' Para momdile
        choices=estados, 
        initial="",
        required=False)
    
    municipio = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mr-sm-2',
        'autocomplete':'off',}),
        required=False)

    area_min = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mr-sm-2',
        'autocomplete': 'off',}), 
        required=False)

    area_max = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mr-sm-2',
        'autocomplete': 'off',
        'oninput':"this.form.range_area_max.value=this.value"}), 
        required=False)
    
    valor_min = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mr-sm-2',
        'autocomplete': 'off',}),
        required=False)

    valor_max = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mr-sm-2', 
        'autocomplete': 'off',}),
        required=False,
        )