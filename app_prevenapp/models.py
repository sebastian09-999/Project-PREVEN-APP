from django.db import models

# 1. Tabla Usuario (Pacientes / Clientes)
class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, default="Activo")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# 2. Tabla Especialidad
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 3. Tabla Profesional (Relacionada con Usuario y Especialidad)
class Profesional(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_profesional')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='profesionales')
    documento_identidad = models.CharField(max_length=20)
    credencial_profesional = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, default="Disponible")

    def __str__(self):
        return f"Dr(a). {self.usuario.apellidos} - {self.especialidad.nombre}"

# 4. Tabla Cita (Relacionada con Usuario/Paciente y Profesional)
class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas_paciente')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='citas_medico')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default="Pendiente")

    def __str__(self):
        return f"Cita #{self.id} - Paciente: {self.usuario.nombres} con {self.profesional.usuario.apellidos}"

# 5. Tabla Horario_profesional (Relacionada con Profesional)
class Horario_profesional(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='horarios')
    dias_semana = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    num_citas = models.IntegerField(default=1)

    def __str__(self):
        return f"Horario Dr(a). {self.profesional.usuario.apellidos} ({self.dias_semana})"

# 6. Tabla Sala_chat (Relacionada con Profesional)
class Sala_chat(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='salas_chat')
    tema = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, default="Activa")

    def __str__(self):
        return f"Sala: {self.tema} - {self.profesional.usuario.apellidos}"