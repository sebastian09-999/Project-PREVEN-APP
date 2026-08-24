from django.db import models

# Create your models here.


# Se agregan las clases Rol y Categoria porque Usuario y Actividad dependen de ellas (llaves foráneas).
class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
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

class ContactoEmergencia(models.Model):
    idContacto_Emergencia = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)

class HistorialChatbot(models.Model):
    idHistorial_chat = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.TextField()
    respuesta = models.TextField()
    fecha = models.DateTimeField()

class Actividad(models.Model):
    idActividad = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    objetivos = models.TextField()
    instrucciones = models.TextField()
    nivel_dificultad = models.CharField(max_length=20)
    recursos_multimedia = models.CharField(max_length=255)
    frecuencia = models.CharField(max_length=45)
    duracion = models.CharField(max_length=20)
    fecha = models.DateField()
    creado_por = models.IntegerField() 

class ParticipacionActividad(models.Model):
    idParticipacion_actividad = models.AutoField(primary_key=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=255)
    fecha = models.DateTimeField()