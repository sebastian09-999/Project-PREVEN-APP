from django.contrib import admin
from .models import Paciente, Doctor, CitaPrevento

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(CitaPrevento)
