from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preven-app/', include('app_preven.urls')),
    path('', views.fn_inicio),
    path('preven-app/', include('app_prevenapp.urls')),
    path('preven-app/', include('app_preven_app.urls')),
    path('preven-app/', include('app_preven_juliana.urls'))
]

