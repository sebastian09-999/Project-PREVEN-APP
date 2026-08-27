from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenido, name='bienvenido'),
    path('paciente/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('paciente/editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('paciente/eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),
]
