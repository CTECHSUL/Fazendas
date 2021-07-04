from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .models import Fazenda, FazendaMedia
from .forms import FazendaForm, UploadMedia, SearchForm
from django.core.cache import cache
from .utils import deleteImagem, deleteVideo, deleteAudio
import filetype


def filtro_inicio(request):
    estado = request.GET.get("estado","")
    municipio = request.GET.get("municipio","")
    area_min = request.GET.get("area_min","")
    area_max = request.GET.get("area_max","")
    valor_min = request.GET.get("valor_min","")
    valor_max = request.GET.get("valor_max","")
    form = SearchForm(request.GET)
    erro = ""
    if request.POST:
        print("TESTE")
    fazendas = set()
    if form.is_valid():
        estado = form.cleaned_data["estado"]
        municipio = form.cleaned_data["municipio"]
        area_min = form.cleaned_data["area_min"].replace('.', '').replace(',', '')
        if area_min == "":
            area_min = 0
        area_max = form.cleaned_data["area_max"].replace('.', '').replace(',', '')
        if area_max == "":
            area_max = 1000000000
        valor_min = form.cleaned_data["valor_min"].replace('.', '').replace(',', '')
        if valor_min == "":
            valor_min = 0
        valor_max = form.cleaned_data["valor_max"].replace('.', '').replace(',', '')
        if valor_max == "":
            valor_max = 1000000000000
        
        estado_in = form.cleaned_data.get("estado")
        municipio_in = form.cleaned_data.get("municipio")
        area_in = form.cleaned_data.get("area_min")
        valor_in = form.cleaned_data.get("valor")
        filter_dict = {"estado": estado, 
                       "municipio": municipio,
                       "area_min": area_min,
                       "area_max": area_max,
                       "valor_min": valor_min,
                       "valor_max": valor_max}

        try:
            fazendas = Fazenda.objects.filter(estado__icontains=filter_dict["estado"],
                municipio__icontains=filter_dict["municipio"],
                area_total__gte=filter_dict["area_min"],
                area_total__lte=filter_dict["area_max"],
                valor__gte=filter_dict["valor_min"],
                valor__lte=filter_dict["valor_max"],)
        except Exception as erro:
            context = {'form': form,
                'fazendas': fazendas,
                'erro': erro}
            
            return render(request, "cadastro/filtro_inicio.html", context)

            print(erro)
            pass
            
    context = {'form': form,
                'fazendas': fazendas,}

    return render(request, "cadastro/filtro_inicio.html", context)


def inicio(request):
    fazendas = Fazenda.objects.all()
    fazenda_lista = []
    for fazenda in fazendas:
        fazenda_lista.append(fazenda)
   
    context = {'fazendas': fazenda_lista}

    return render(request, 'cadastro/inicio.html', context)


def fazenda_view(request, pk):
    midia = FazendaMedia.objects.all().filter(fazenda_id=pk)
    imagens = []
    videos = []
    audios = []

    for i in midia:
        if i.imagem != "":
            imagens.append(i.imagem)
        if i.video != "":
            videos.append(i.video)
        if i.audio != "":
            audios.append(i.audio)

    fazenda = Fazenda.objects.get(pk=pk)

    context = {'imagens': imagens,
                'videos': videos,
                'audios': audios,
                'fazenda': fazenda}

    return render(request, 'cadastro/fazenda_view.html', context)    


def cadastro(request):
    form = FazendaForm(request.POST or None)
    form.fields['valor'].widget.attrs = {'class': 'form-control mr-sm-2'}
    
    if form.is_valid():    
        form_id = form.save()
        cache.set(f"{request.META['CSRF_COOKIE']}", form_id, 300000)

        return redirect('upload_media')
    
    else:
        erro = form.errors.as_data()
        if erro != {}:
            print(erro)
            erro = r"ERRO NO FORMULÁRIO\nVERIFIQUE OS CAMPOS PREENCHIDOS"
            context = {'form': form,
                        'erro': erro}


            return render(request, 'cadastro/cadastro.html', context)
            pass
    
    context = {'form': form}

    return render(request, 'cadastro/cadastro.html', context)


def editar_cadastro(request, pk):
    obj = Fazenda.objects.get(pk=pk)
    cache.set(f"{request.META['CSRF_COOKIE']}", obj, 300000)
    form = FazendaForm(request.POST or None, instance=obj)
    form.fields['valor'].widget.attrs = {'class': 'form-control mr-sm-2'}
    midia = FazendaMedia.objects.all().filter(fazenda_id=pk)
    imagens = []
    videos = []
    audios = []
    
    for i in midia:
        if i.imagem != "":
            imagens.append(i)
        if i.video != "":
            videos.append(i)
        if i.audio != "":
            audios.append(i)

    if form.is_valid():
        form.save()
        
        return redirect(reverse('fazenda_view', kwargs={"pk":pk}))
    
    
    erro = form.errors.as_data()
    if erro != {}:
        print(erro)
        erro = r"ERRO NO FORMULÁRIO\nVERIFIQUE OS CAMPOS PREENCHIDOS"
        context = {'form':form,
            'imagens':imagens,
            'videos': videos,
            'audios': audios,
            'fazenda':obj,
            'erro': erro}
    else:
        context = {'form':form,
                    'imagens':imagens,
                    'videos': videos,
                    'audios': audios,
                    'fazenda':obj,}

    return render(request, 'cadastro/editar_cadastro.html', context)


def add_media(request, pk):
    cache.set(f"{request.META['CSRF_COOKIE']}", Fazenda.objects.get(pk=pk), 300000)
    return redirect('upload_media')


class UploadView(FormView):
    form_class = UploadMedia
    template_name = 'cadastro/upload_media.html'
    success_url = 'cadastro' #Não estou usando
    
    #Daria para validar o arquivo no form e direcionar por tipo no create... Usando um únifo form de arquivos no template
    def post(self, request, *args, **kwargs):
        obj = cache.get(f"{request.META['CSRF_COOKIE']}")
        print(obj)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        imagens = request.FILES.getlist('imagens')
        videos = request.FILES.getlist('videos')
        audios = request.FILES.getlist('audios')

        for i in imagens:
            imagem = filetype.guess(i)
            try:
                if imagem.MIME.split('/')[0] == 'image':
                    print("Upload de imagem.")
                else:
                    print("TIPO DE ARQUIVO NÃO PERMITIDO.")
                    return add_media(request, obj.pk)

            except Exception as erro:
                print("TIPO DE ARQUIVO NÃO PERMITIDO.")
                return add_media(request, obj.pk)
                pass

        for v in videos:
            video = filetype.guess(v)
            try:
                if video.MIME.split('/')[0] == 'video':
                    print("Upload de vídeo.")
                else:
                    print("TIPO DE ARQUIVO NÃO PERMITIDO.")
                    return add_media(request, obj.pk)

            except Exception as erro:
                print("TIPO DE ARQUIVO NÃO PERMITIDO.", erro)
                return add_media(request, obj.pk)
                pass

        for a in audios:
            audio = filetype.guess(a)
            try:
                if audio.MIME.split('/')[0] == 'audio':
                    print("Upload de áudio.")
                else:
                    print("TIPO DE ARQUIVO NÃO PERMITIDO.")
                    return add_media(request, obj.pk)

            except Exception as erro:
                print("TIPO DE ARQUIVO NÃO PERMITIDO.", erro)
                return add_media(request, obj.pk)
                pass
        

        if form.is_valid():
            for i in imagens:
                FazendaMedia.objects.create(fazenda_id=obj.pk, imagem=i)
            for v in videos:                
                FazendaMedia.objects.create(fazenda_id=obj.pk, video=v)
            for a in audios:
                FazendaMedia.objects.create(fazenda_id=obj.pk, audio=a)

            return redirect(reverse('fazenda_view', kwargs={"pk":obj.pk}))
        
        else:
            print(form.errors.as_data())
            return self.form_invalid(form)


def delete_imagem(request, id):
    imagem = FazendaMedia.objects.get(id=id)
    fazenda_id = imagem.fazenda_id
    deleteImagem(imagem.imagem)
    imagem.delete()


    return redirect(reverse('editar_cadastro', kwargs={"pk":fazenda_id}))

def delete_video(request, id):
    video = FazendaMedia.objects.get(id=id)
    fazenda_id = video.fazenda_id
    deleteVideo(video.video)
    video.delete()


    return redirect(reverse('editar_cadastro', kwargs={"pk":fazenda_id}))

def delete_audio(request, id):
    audio = FazendaMedia.objects.get(id=id)
    fazenda_id = audio.fazenda_id
    deleteAudio(audio.audio)
    audio.delete()


    return redirect(reverse('editar_cadastro', kwargs={"pk":fazenda_id}))