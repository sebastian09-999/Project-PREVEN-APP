from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crear-roles/', views.crear_roles, name='crear_roles'),
    path('crear-categorias/', views.crear_categorias, name='crear_categorias'),
    path('crear-usuarios/', views.crear_usuarios, name='crear_usuarios'),
    path('crear-contactos/', views.crear_contactos, name='crear_contactos'),
    path('crear-historial-chat/', views.crear_historial_chat, name='crear_historial_chat'),
    path('crear-actividades/', views.crear_actividades, name='crear_actividades'),
    path('crear-participaciones/', views.crear_participaciones, name='crear_participaciones'),
]