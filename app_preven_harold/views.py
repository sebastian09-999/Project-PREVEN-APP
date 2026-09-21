from django.shortcuts import render

from django.shortcuts import render

def categoria_rec_act(request):
    return render(request, 'categoria-rec-act.html')

def perfil_profecional(request):
    return render(request, 'perfil-profecional.html')

def sis_chat(request):
    return render(request, 'sis-chat.html')

def usuario(request):
    return render(request, 'usuario.html')
