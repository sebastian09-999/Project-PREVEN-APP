from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from datetime import date
from .models import (Rol, Categoria, Usuario, ContactoEmergencia, 
                     HistorialChatbot, Actividad, ParticipacionActividad)

# 1. Crear Roles (Necesario para Usuario)
def crear_roles(request):
    roles = [
        Rol(nombre='Administrador'),
        Rol(nombre='Usuario'),
        Rol(nombre='Profesional'),
        Rol(nombre='Invitado'),
    ]
    Rol.objects.bulk_create(roles)
    return HttpResponse("Roles creados exitosamente.")

# 2. Crear Categorías (Necesario para Actividad)
def crear_categorias(request):
    categorias = [
        Categoria(nombre='Terapia Física'),
        Categoria(nombre='Salud Mental'),
        Categoria(nombre='Nutrición'),
        Categoria(nombre='Recreación'),
        Categoria(nombre='Evaluación'),
    ]
    Categoria.objects.bulk_create(categorias)
    return HttpResponse("Categorías creadas exitosamente.")

# 3. Crear Usuarios
def crear_usuarios(request):
    # Obtenemos un rol existente para asociarlo (Asegúrate de ejecutar crear_roles primero)
    rol_usuario = Rol.objects.filter(nombre='Usuario').first()
    
    if not rol_usuario:
        return HttpResponse("Error: Debes crear los roles primero.")

    usuarios = [
        Usuario(rol=rol_usuario, nombres='Juan', apellidos='Perez', correo='juan@mail.com', telefono='3001234567', edad=25, sexo='M', nivel_educativo='Universitario', eps='Sura', contrasena='1234', rh='O+', estado='Activo'),
        Usuario(rol=rol_usuario, nombres='Maria', apellidos='Gomez', correo='maria@mail.com', telefono='3007654321', edad=30, sexo='F', nivel_educativo='Secundaria', eps='Sanitas', contrasena='1234', rh='A+', estado='Activo'),
        Usuario(rol=rol_usuario, nombres='Carlos', apellidos='Lopez', correo='carlos@mail.com', telefono='3109876543', edad=40, sexo='M', nivel_educativo='Postgrado', eps='Compensar', contrasena='1234', rh='B-', estado='Inactivo'),
        Usuario(rol=rol_usuario, nombres='Ana', apellidos='Diaz', correo='ana@mail.com', telefono='3201239876', edad=22, sexo='F', nivel_educativo='Técnico', eps='Salud Total', contrasena='1234', rh='O-', estado='Activo'),
        Usuario(rol=rol_usuario, nombres='Luis', apellidos='Ramirez', correo='luis@mail.com', telefono='3154567890', edad=28, sexo='M', nivel_educativo='Universitario', eps='Sura', contrasena='1234', rh='AB+', estado='Activo'),
    ]
    Usuario.objects.bulk_create(usuarios)
    return HttpResponse("Usuarios creados exitosamente.")

# 4. Crear Contactos de Emergencia
def crear_contactos(request):
    usuario_base = Usuario.objects.first()

    contactos = [
        ContactoEmergencia(usuario=usuario_base, nombre='Pedro Perez', telefono='3010000001', correo='pedro@mail.com'),
        ContactoEmergencia(usuario=usuario_base, nombre='Marta Gomez', telefono='3010000002', correo='marta@mail.com'),
        ContactoEmergencia(usuario=usuario_base, nombre='Jose Lopez', telefono='3010000003', correo='jose@mail.com'),
        ContactoEmergencia(usuario=usuario_base, nombre='Diana Diaz', telefono='3010000004', correo='diana@mail.com'),
        ContactoEmergencia(usuario=usuario_base, nombre='Andres Ramirez', telefono='3010000005', correo='andres@mail.com'),
    ]
    ContactoEmergencia.objects.bulk_create(contactos)
    return HttpResponse("Contactos de emergencia creados exitosamente.")

# 5. Crear Historial Chatbot
def crear_historial_chat(request):
    usuario_base = Usuario.objects.first()
    ahora = timezone.now()

    historiales = [
        HistorialChatbot(usuario=usuario_base, pregunta='¿Cómo agendo cita?', respuesta='Puedes hacerlo desde el menú principal.', fecha=ahora),
        HistorialChatbot(usuario=usuario_base, pregunta='¿Cuáles son los horarios?', respuesta='Atendemos de 8am a 5pm.', fecha=ahora),
        HistorialChatbot(usuario=usuario_base, pregunta='Necesito hablar con un médico', respuesta='Te transferiré con un especialista.', fecha=ahora),
        HistorialChatbot(usuario=usuario_base, pregunta='¿Dónde están ubicados?', respuesta='Estamos en la sede central.', fecha=ahora),
        HistorialChatbot(usuario=usuario_base, pregunta='Olvidé mi contraseña', respuesta='Ve a la opción recuperar clave.', fecha=ahora),
    ]
    HistorialChatbot.objects.bulk_create(historiales)
    return HttpResponse("Historiales de chat creados exitosamente.")

# 6. Crear Actividades
def crear_actividades(request):
    categoria_base = Categoria.objects.first()

    actividades = [
        Actividad(categoria=categoria_base, nombre='Caminata', descripcion='Caminar 30 mins', objetivos='Mejorar cardio', instrucciones='Paso ligero', nivel_dificultad='Bajo', recursos_multimedia='video1.mp4', frecuencia='Diaria', duracion='30 min', fecha=date.today(), creado_por=1),
        Actividad(categoria=categoria_base, nombre='Meditación', descripcion='Respiración', objetivos='Reducir estrés', instrucciones='Cerrar ojos', nivel_dificultad='Bajo', recursos_multimedia='audio1.mp3', frecuencia='Diaria', duracion='15 min', fecha=date.today(), creado_por=1),
        Actividad(categoria=categoria_base, nombre='Yoga', descripcion='Estiramientos', objetivos='Flexibilidad', instrucciones='Sigue el video', nivel_dificultad='Medio', recursos_multimedia='yoga.mp4', frecuencia='Semanal', duracion='45 min', fecha=date.today(), creado_por=1),
        Actividad(categoria=categoria_base, nombre='Lectura', descripcion='Leer artículo', objetivos='Educación', instrucciones='Leer completo', nivel_dificultad='Bajo', recursos_multimedia='doc.pdf', frecuencia='Semanal', duracion='20 min', fecha=date.today(), creado_por=1),
        Actividad(categoria=categoria_base, nombre='Cuestionario', descripcion='Test de estado', objetivos='Evaluación', instrucciones='Responder honestamente', nivel_dificultad='Bajo', recursos_multimedia='form.link', frecuencia='Mensual', duracion='10 min', fecha=date.today(), creado_por=1),
    ]
    Actividad.objects.bulk_create(actividades)
    return HttpResponse("Actividades creadas exitosamente.")

# 7. Crear Participación en Actividades
def crear_participaciones(request):
    usuario_base = Usuario.objects.first()
    actividad_base = Actividad.objects.first()
    ahora = timezone.now()

    participaciones = [
        ParticipacionActividad(actividad=actividad_base, usuario=usuario_base, resultado='Completado', fecha=ahora),
        ParticipacionActividad(actividad=actividad_base, usuario=usuario_base, resultado='Incompleto', fecha=ahora),
        ParticipacionActividad(actividad=actividad_base, usuario=usuario_base, resultado='Pendiente', fecha=ahora),
        ParticipacionActividad(actividad=actividad_base, usuario=usuario_base, resultado='Completado con éxito', fecha=ahora),
        ParticipacionActividad(actividad=actividad_base, usuario=usuario_base, resultado='Abandonado', fecha=ahora),
    ]
    ParticipacionActividad.objects.bulk_create(participaciones)
    return HttpResponse("Participaciones creadas exitosamente.")


#Función mostrar datos en página

def ver_todo(request):
    context = {
        'usuarios': Usuario.objects.all(),
        'actividades': Actividad.objects.all(),
        'contactos': ContactoEmergencia.objects.all(),
        'historiales': HistorialChatbot.objects.all(),
        'participaciones': ParticipacionActividad.objects.all(),
    }
    return render(request, 'ver_todo.html', context)


def registro_usuario(request):
    if request.method == 'POST':
        # Capturar datos del formulario HTML
        rol_id = request.POST.get('rol')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        nivel_educativo = request.POST.get('nivel_educativo')
        eps = request.POST.get('eps')
        contrasena = request.POST.get('contrasena')
        rh = request.POST.get('rh')
        estado = request.POST.get('estado', 'Activo')

        # Buscar la instancia del Rol seleccionado
        rol_instancia = Rol.objects.get(idRol=rol_id)

        # Crear y guardar el nuevo Usuario en la base de datos
        Usuario.objects.create(
            rol=rol_instancia,
            nombres=nombres,
            apellidos=apellidos,
            correo=correo,
            telefono=telefono,
            edad=edad,
            sexo=sexo,
            nivel_educativo=nivel_educativo,
            eps=eps,
            contrasena=contrasena,
            rh=rh,
            estado=estado
        )

        return redirect('ver_todo')  # Redirige a la vista deseada tras guardar

    # Si la petición es GET, enviamos los roles para el select
    roles = Rol.objects.all()
    return render(request, 'registro.html', {'roles': roles})