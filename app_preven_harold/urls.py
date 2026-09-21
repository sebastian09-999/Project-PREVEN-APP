from django.urls import path
from . import views

urlpatterns = [
    path('categoria-rec-act/', views.categoria_rec_act, name='categoria_rec_act'),
    path('perfil-profecional/', views.perfil_profecional, name='perfil_profecional'),
    path('sis-chat/', views.sis_chat, name='sis_chat'),
    path('usuario/', views.usuario, name='usuario'),
]