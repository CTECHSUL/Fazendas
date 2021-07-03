from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar_cadastro/<int:pk>', views.editar_cadastro, name='editar_cadastro'),
    path('upload_media/', views.UploadView.as_view(), name='upload_media'),
    path('upload_media/<int:pk>', views.add_media, name='add_media'),
    path('delete_imagem/<int:id>', views.delete_imagem, name='delete_imagem'),
    path('delete_video/<int:id>', views.delete_video, name='delete_video'),
    path('delete_audio/<int:id>', views.delete_audio, name='delete_audio'),
    path('fazenda_view/<int:pk>', views.fazenda_view, name='fazenda_view'),
    path('', views.filtro_inicio, name='inicio'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)