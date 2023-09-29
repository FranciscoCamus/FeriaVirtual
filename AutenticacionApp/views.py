from django.shortcuts import render, redirect, redirect, get_object_or_404

from django.contrib.auth import login, authenticate

from .forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages




# Create your views here.

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            #redirigir al Home
            return redirect(to="Home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'registration/lista_usuarios.html', {'usuarios': usuarios})


@login_required
def crear_usuario(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario creado con éxito.')
            return redirect('AutenticacionApp:lista_usuarios')
    else:
        formulario = CustomUserCreationForm()
    return render(request, 'registration/formulario_usuario.html', {'formulario': formulario})


@login_required
def actualizar_usuario(request, id_usuario):
    usuario = User.objects.get(pk=id_usuario)
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="AutenticacionApp:lista_usuarios")
    else:
        formulario = CustomUserCreationForm(instance=usuario)
    return render(request, 'registration/formulario_usuario.html', {'formulario': formulario})


def eliminar_usuario(request, id_usuario):
    if request.method == 'GET':
        usuario = get_object_or_404(User, id=id_usuario)
        usuario.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('AutenticacionApp:lista_usuarios')
    
    return redirect('Home')
