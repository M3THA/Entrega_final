import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate





def inicio(request):
    return render(request, "blogApp/inicio.html")


#Vista de login

def login_usuario(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid:

            usuario= request.POST['nombre']
            contrasena= request.POST['clave']

            user= authenticate(nombre=usuario, clave=contrasena) 

            if user is not None:

                login(request, user)

                return render(request, "blogApp/inicio.html", {'mensaje':f"Inicio de sesion exitosa {usuario}"} )
            else: 
                
                return render(request, "blogApp/login.html", {'form': form,  'mensaje': f"Error, datos incorrectos"} )

        else:
            
            return render(request, "blogApp/inicio.html", {'mensaje': "Error, formulario erroneo"} )

    else:

        form = AuthenticationForm()

        return render(request, "blogApp/login.html", {'form': form})

# Vista de registro

def registro(request):

    if request.method == 'POST':

        form= UserCreationForm(request, data=request.POST)

        if form.is_valid():

            usuario= request.POST['usuario']

            form.save()
            return render(request, "blogApp/inicio.html", {'form':form, 'mensaje':f"Usuario creado: {usuario}"} )

    else:
        form= UserCreationForm()

    return render(request,'blogApp/registro.html', {'form': form} )
