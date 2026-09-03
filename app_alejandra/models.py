from django.db import models

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class Recurso(models.Model):
    idRecurso = models.AutoField(primary_key=True)
    Categoria_idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Tipo = models.CharField(max_length=45)
    Fecha = models.DateField()
    Creado_por = models.IntegerField()

    def __str__(self):
        return self.Titulo