from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='servicios')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=255)
    horario = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inquietudes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inquietudes')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='inquietudes')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return self.titulo

class Recurso(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='recursos')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=45)
    fecha = models.DateField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recursos_creados')

    def __str__(self):
        return self.titulo

class RecursoFavorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recursos_favoritos')
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE, related_name='favorito_por')
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'recurso')

    def __str__(self):
        return f"{self.usuario.username} - {self.recurso.titulo}"

class Tip(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='tips')
    profesional = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tips_publicados')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivos_enlaces = models.CharField(max_length=255, blank=True, null=True)
    fuente = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    #profesional (error)
class Profesional(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profesionales')
    # Apunta a la otra app como indica el error anterior:
    especialidad = models.ForeignKey('app_preven_app.Especialidad', on_delete=models.CASCADE, related_name='profesionales')
    registro_profesional = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - Especialista"