
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fn_inicio),
    path('', include('app_prevenapp.urls')),
    path('app/', include('app_preven_app.urls')),
]
