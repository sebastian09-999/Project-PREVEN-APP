from django.shortcuts import render
from .models import Categoria, Servicio, Inquietudes, Recurso, RecursoFavorito, Tip

# 1. Vista para listar Categorías
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'app_preven/categorias.html', {'categorias': categorias})

# 2. Vista para listar Servicios
def lista_servicios(request):
    servicios = Servicio.objects.select_related('categoria').all()
    return render(request, 'app_preven/servicios.html', {'servicios': servicios})

# 3. Vista para listar Inquietudes
def lista_inquietudes(request):
    inquietudes = Inquietudes.objects.select_related('usuario', 'categoria').all()
    return render(request, 'app_preven/inquietudes.html', {'inquietudes': inquietudes})

# 4. Vista para listar Recursos
def lista_recursos(request):
    recursos = Recurso.objects.select_related('categoria', 'creado_por').all()
    return render(request, 'app_preven/recursos.html', {'recursos': recursos})

# 5. Vista para listar Recursos Favoritos (del usuario logueado)
def lista_recursos_favoritos(request):
    if request.user.is_authenticated:
        favoritos = RecursoFavorito.objects.filter(usuario=request.user).select_related('recurso', 'recurso__categoria')
    else:
        favoritos = RecursoFavorito.objects.none()
    return render(request, 'app_preven/recursos_favoritos.html', {'favoritos': favoritos})

# 6. Vista para listar Tips y Recomendaciones
def lista_tips(request):
    tips = Tip.objects.select_related('categoria', 'profesional').all()
    return render(request, 'app_preven/tips.html', {'tips': tips})
