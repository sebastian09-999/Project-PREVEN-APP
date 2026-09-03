from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Recurso

# Vista para crear un recurso de prueba rápidamente
def crear_recurso(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tipo = request.POST.get('tipo')
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        
        categoria = Categoria.objects.get(pk=categoria_id)
        Recurso.objects.create(
            Titulo=titulo,
            Tipo=tipo,
            Fecha=fecha,
            Descripcion=descripcion,
            Categoria_idCategoria=categoria
        )
        return redirect('app_alejandra:lista_recursos')
    
    categorias = Categoria.objects.all()
    return render(request, 'app_alejandra/crear_recurso.html', {'categorias': categorias})