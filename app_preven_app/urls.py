from django.urls import path
from . import views

urlpatterns = [
    path('insertar/', views.insertar_datos_prueba, name='insertar_datos'),
    path('panel/', views.ver_panel_completo, name='ver_panel_completo'),
]