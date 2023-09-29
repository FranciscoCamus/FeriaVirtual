from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):

    return render(request, "FeriaVirtualApp/home.html")



def tienda(request):

    return render(request, "FeriaVirtualApp/tienda.html")

def blog(request):

    return render(request, "FeriaVirtualApp/blog.html")

def contacto(request):

    return render(request, "FeriaVirtualApp/contacto.html")