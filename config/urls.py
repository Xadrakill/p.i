from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import *
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='index'),
    path('Cidades/', CidadesView.as_view(), name='cidades'),
    path('criar-conta/', CriarContaView.as_view(), name='criar-conta'), 
    path('viagens/', views.viagens_view, name='viagens'),
    path('perfil/', perfil_view, name='perfil'),
    path('perfil/editar/', editar_perfil_view, name='editar_perfil'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)