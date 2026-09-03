from django.contrib import admin
from .models import Categoria, Recurso

# Registrar modelos para que aparezcan en el panel de administración
admin.site.register(Categoria)
admin.site.register(Recurso)