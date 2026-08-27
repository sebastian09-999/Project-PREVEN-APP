from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, CitaPrevento
from .forms import PacienteForm

# Consultar / Listar
def bienvenido(request):
    pacientes = Paciente.objects.all()
    citas = CitaPrevento.objects.all()
    return render(request, 'app_preven/mainpreven.html', {
        'pacientes': pacientes,
        'citas': citas
    })

# Crear
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = PacienteForm()
    return render(request, 'app_preven/form_paciente.html', {'form': form, 'titulo': 'Crear Paciente'})

# Actualizar
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'app_preven/form_paciente.html', {'form': form, 'titulo': 'Editar Paciente'})

# Eliminar
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('bienvenido')
    return render(request, 'app_preven/confirmar_eliminar.html', {'paciente': paciente})
