from django.db import models


class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios')
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)
    nivel_educativo = models.CharField(max_length=45)
    eps = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=255)
    rh = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class ContactoEmergencia(models.Model):
    idContacto_Emergencia = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contactos_emergencia')
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} (Contacto de {self.usuario.nombres})"


class HistorialChatbot(models.Model):
    idHistorial_chat = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial_chatbot')
    pregunta = models.TextField()
    respuesta = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return f"Chat de {self.usuario.nombres} - {self.fecha.strftime('%Y-%m-%d')}"


class Actividad(models.Model):
    idActividad = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='actividades')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Conexión con Especialidad que reside en app_preven_app
class Profesional(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_profesional')
    especialidad = models.ForeignKey('app_preven_app.Especialidad', on_delete=models.CASCADE)
    documento_identidad = models.CharField(max_length=20)
    credencial_profesional = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, default="Disponible")

    def __str__(self):
        return f"Dr(a). {self.usuario.apellidos}"


class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas_paciente')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='citas_medico')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default="Pendiente")

    def __str__(self):
        return f"Cita #{self.id} - Paciente: {self.usuario.nombres}"


class Horario_profesional(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='horarios')
    dias_semana = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    num_citas = models.IntegerField(default=1)

    def __str__(self):
        return f"Horario Dr(a). {self.profesional.usuario.apellidos} ({self.dias_semana})"


class Sala_chat(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='salas_chat')
    tema = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, default="Activo")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sala: {self.tema}"


class ParticipacionActividad(models.Model):
    idParticipacion_actividad = models.AutoField(primary_key=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='participaciones')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='participaciones_actividad')
    resultado = models.CharField(max_length=255)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.usuario.nombres} - {self.actividad.nombre}"