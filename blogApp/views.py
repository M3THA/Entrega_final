import re
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate





def inicio(request):
    return render(request, "blogApp/inicio.html")


#Vista de login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contrasena= form.cleaned_data.get('password')

            user= authenticate(username=usuario, password=contrasena) 

            if user is not None:

                login(request, user)

                return render(request, "blogApp/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )
            else: 
                
                return render(request, "blogApp/inicio.html", {"mensaje": "Error, datos incorrectos"} )

        else:
            
            return render(request, "blogApp/inicio.html", {"mensaje": "Error, formulario erroneo"} )

    form = AuthenticationForm()

    return render(request, "blogApp/login.html", {'form': form})