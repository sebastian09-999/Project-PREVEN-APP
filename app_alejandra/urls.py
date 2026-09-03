from django.urls import path
from . import views

app_name = 'app_alejandra'

urlpatterns = [
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('recursos/', views.lista_recursos, name='lista_recursos'),
    # Ruta para eliminar recurso dinámicamente según su ID
    path('recursos/eliminar/<int:id>/', views.eliminar_recurso, name='eliminar_recurso'),
    path('recursos/crear/', views.crear_recurso, name='crear_recurso'),
]