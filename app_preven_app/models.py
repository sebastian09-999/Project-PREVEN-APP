from django.db import models

# 1. Tabla Usuario (Conectada a la parte de tu compañero)
# Si tu compañero crea esta tabla en otra app, solo cambias la referencia
class Usuario(models.Model):
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# 2. Tabla Especialidad
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# 3. Tabla Profesional (Tabla CENTRAL)
class Profesional(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    documento_identidad = models.CharField(max_length=20)
    credencial_profesional = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Profesional: {self.usuario.nombres} - {self.especialidad}"


# 4. Tabla Cita
class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Cita {self.fecha} - {self.profesional}"


# 5. Tabla Horario_profesional
class Horario_profesional(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    dias_semana = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    num_citas = models.IntegerField()
    notificaciones_activas = models.BooleanField(default=True)

    def __str__(self):
        return f"Horario: {self.profesional}"


# 6. Tabla Sala_chat
class Sala_chat(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sala: {self.tema}"