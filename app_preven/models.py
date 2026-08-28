from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.documento})"

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad}"

class CitaPrevento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    diagnostico = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cita: {self.paciente.nombre} con {self.doctor.nombre}"
    