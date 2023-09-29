from django.urls import path


from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'AutenticacionApp'

urlpatterns = [

    path('', views.registro, name="Registro"),

    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:id_usuario>/actualizar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/<int:id_usuario>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    
]

