from django.shortcuts import render
from django.http import HttpResponse
# Importa la especialidad local de esta carpeta
from .models import Especialidad

# Importa el resto de los modelos desde la app principal
from app_prevenapp.models import Usuario, Profesional, Cita, Horario_profesional, Sala_chat

def insertar_datos_prueba(request):
    u1 = Usuario.objects.create(nombres="Carlos", apellidos="Pérez", correo="carlos.perez@gmail.com", telefono="3001234567", estado="Activo")
    u2 = Usuario.objects.create(nombres="María", apellidos="Gómez", correo="maria.gomez@gmail.com", telefono="3119876543", estado="Activo")
    u3 = Usuario.objects.create(nombres="Juan", apellidos="Rodríguez", correo="juan.rodriguez@gmail.com", telefono="3205554433", estado="Activo")
    u4 = Usuario.objects.create(nombres="Ana", apellidos="Martínez", correo="ana.martinez@gmail.com", telefono="3150001122", estado="Activo")

    e1 = Especialidad.objects.create(nombre="Psicología Clínica")
    e2 = Especialidad.objects.create(nombre="Psiquiatría")

    p1 = Profesional.objects.create(usuario=u1, especialidad=e1, documento_identidad="1098765432", credencial_profesional="PSI-9921", estado="Disponible")
    p2 = Profesional.objects.create(usuario=u2, especialidad=e2, documento_identidad="1054321987", credencial_profesional="PSQ-4412", estado="Disponible")

    Cita.objects.create(usuario=u3, profesional=p1, fecha="2026-09-01", hora="09:00:00", estado="Confirmada")
    Cita.objects.create(usuario=u4, profesional=p2, fecha="2026-09-02", hora="11:30:00", estado="Pendiente")

    Horario_profesional.objects.create(profesional=p1, dias_semana="Lunes a Miércoles", hora_inicio="08:00:00", hora_fin="14:00:00", num_citas=6)
    Horario_profesional.objects.create(profesional=p2, dias_semana="Jueves y Viernes", hora_inicio="10:00:00", hora_fin="18:00:00", num_citas=8)

    Sala_chat.objects.create(profesional=p1, tema="Manejo del Estrés", descripcion="Espacio para compartir técnicas de autocuidado.", estado="Activa")
    Sala_chat.objects.create(profesional=p2, tema="Orientación en Salud Mental", descripcion="Sesiones grupales sobre bienestar integral.", estado="Activa")

    return HttpResponse("¡ÉXITO! Se han cargado registros de prueba completos en las 6 tablas.")

def ver_panel_completo(request):
    usuarios = Usuario.objects.all()
    especialidades = Especialidad.objects.all()
    profesionales = Profesional.objects.all()
    citas = Cita.objects.all()
    horarios = Horario_profesional.objects.all()
    salas = Sala_chat.objects.all()

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Consultorio & Prevención Médica - Panel</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body { background-color: #f6f4f9; font-family: 'Plus Jakarta Sans', sans-serif; color: #332a40; padding-bottom: 50px; }
            .navbar-clinic { background: linear-gradient(135deg, #7c5cbf 0%, #a282e0 100%); color: white; padding: 20px 0; box-shadow: 0 4px 15px rgba(124, 92, 191, 0.15); border-bottom: 3px solid #e9dff7; }
            .card-clinic { background: #ffffff; border: 1px solid #e9dff7; border-radius: 14px; box-shadow: 0 4px 12px rgba(124, 92, 191, 0.05); margin-bottom: 30px; overflow: hidden; }
            .card-header-clinic { background-color: #f2ebfb; color: #583396; font-weight: 700; font-size: 1.05rem; padding: 14px 20px; border-bottom: 1px solid #e9dff7; display: flex; align-items: center; gap: 8px; }
            .table { margin-bottom: 0; }
            .table th { background-color: #faf7fd; color: #6b4c9a; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 2px solid #e9dff7; }
            .table td { vertical-align: middle; border-color: #f2ebfb; font-size: 0.92rem; }
            .badge-violet { background-color: #e9dff7; color: #583396; font-weight: 600; padding: 6px 12px; border-radius: 8px; }
            .badge-active { background-color: #d1fae5; color: #065f46; font-weight: 600; padding: 6px 12px; border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="navbar-clinic mb-4">
            <div class="container d-flex justify-content-between align-items-center">
                <div>
                    <h2 class="m-0 fw-bold">🏥 Consultorio PrevenApp</h2>
                    <small style="opacity: 0.9;">Sistema Integral de Gestión Médica y Salud</small>
                </div>
                <span class="badge bg-white text-dark px-3 py-2 rounded-pill shadow-sm">Panel Administrativo</span>
            </div>
        </div>

        <div class="container">
            <div class="card-clinic">
                <div class="card-header-clinic">👤 Registros de Pacientes / Usuarios</div>
                <div class="card-body p-0">
                    <table class="table table-hover">
                        <thead><tr><th>ID</th><th>Nombres</th><th>Apellidos</th><th>Correo Electrónico</th><th>Teléfono</th><th>Estado</th></tr></thead>
                        <tbody>"""
    for u in usuarios:
        html += f"<tr><td><b>#{u.idUsuario}</b></td><td>{u.nombres}</td><td>{u.apellidos}</td><td>{u.correo}</td><td>{u.telefono}</td><td><span class='badge-active'>{u.estado}</span></td></tr>"
    html += """
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card-clinic">
                <div class="card-header-clinic">🩺 Especialidades Médicas</div>
                <div class="card-body p-0">
                    <table class="table table-hover">
                        <thead><tr><th>ID</th><th>Especialidad</th></tr></thead>
                        <tbody>"""
    for e in especialidades:
        html += f"<tr><td><b>#{e.id}</b></td><td>{e.nombre}</td></tr>"
    html += """
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card-clinic">
                <div class="card-header-clinic">👨‍⚕️ Personal Médico y Especialistas</div>
                <div class="card-body p-0">
                    <table class="table table-hover">
                        <thead><tr><th>ID</th><th>Especialista</th><th>Área</th><th>Documento ID</th><th>Credencial</th><th>Estado</th></tr></thead>
                        <tbody>"""
    for p in profesionales:
        html += f"<tr><td><b>#{p.id}</b></td><td>{p.usuario.nombres} {p.usuario.apellidos}</td><td><span class='badge-violet'>{p.especialidad.nombre}</span></td><td>{p.documento_identidad}</td><td>{p.credencial_profesional}</td><td><span class='badge-active'>{p.estado}</span></td></tr>"
    html += """
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card-clinic">
                <div class="card-header-clinic">📅 Agenda de Citas Médicas</div>
                <div class="card-body p-0">
                    <table class="table table-hover">
                        <thead><tr><th>ID</th><th>Paciente</th><th>Médico Tratante</th><th>Fecha</th><th>Hora</th><th>Estado</th></tr></thead>
                        <tbody>"""
    for c in citas:
        html += f"<tr><td><b>#{c.id}</b></td><td>{c.usuario.nombres} {c.usuario.apellidos}</td><td>Dr(a). {c.profesional.usuario.apellidos}</td><td>{c.fecha}</td><td>{c.hora}</td><td><span class='badge-violet'>{c.estado}</span></td></tr>"
    html += """
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card-clinic">
                <div class="card-header-clinic">⏰ Horarios de Atención Médica</div>
                <div class="card-body p-0">
                    <table class="table table-hover">
                        <thead><tr><th>ID</th><th>Médico</th><th>Jornada</th><th>Entrada</th><th>Salida</th><th>Citas Disp.</th></tr></thead>
                        <tbody>"""
    for h in horarios:
        html += f"<tr><td><b>#{h.id}</b></td><td>Dr(a). {h.profesional.usuario.apellidos}</td><td>{h.dias_semana}</td><td>{h.hora_inicio}</td><td>{h.hora_fin}</td><td><b>{h.num_citas}</b></td></tr>"
    html += """
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card-clinic">
                <div class="card-header-clinic">💬 Telemedicina y Consultas en Línea</div>
                <div class="card-body p-0">
                    <table class="table table-hover">
                        <thead><tr><th>ID</th><th>Especialista a Cargo</th><th>Tema de Consulta</th><th>Descripción</th><th>Estado</th></tr></thead>
                        <tbody>"""
    for s in salas:
        html += f"<tr><td><b>#{s.id}</b></td><td>Dr(a). {s.profesional.usuario.apellidos}</td><td><b>{s.tema}</b></td><td>{s.descripcion}</td><td><span class='badge-active'>{s.estado}</span></td></tr>"
    html += """
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)