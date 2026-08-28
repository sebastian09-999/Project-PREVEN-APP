from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal / Inicio
    path('', views.lista_servicios, name='bienvenido'),

    # Rutas para el modelo de datos
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('inquietudes/', views.lista_inquietudes, name='lista_inquietudes'),
    path('recursos/', views.lista_recursos, name='lista_recursos'),
    path('favoritos/', views.lista_recursos_favoritos, name='lista_recursos_favoritos'),
    path('tips/', views.lista_tips, name='lista_tips'),
]