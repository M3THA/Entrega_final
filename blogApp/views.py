
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from requests import post

from blogApp.forms import User_register_form, User_edit_form
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.urls import reverse_lazy




def inicio(request):
    return render(request, "blogApp/inicio.html")


#Vista de login

def login_usuario(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid:

            usuario= request.POST['username']
            contrasena= request.POST['password']

            user= authenticate(username=usuario, password=contrasena) 

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

        form= User_register_form(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']

            form.save()
            return render(request, "blogApp/inicio.html", {'form':form, 'mensaje':f"Usuario creado: {username}"} )

    else:
        form= User_edit_form()

    return render(request,'blogApp/registro.html', {'form': form} )

# Vista de editar perfil

@login_required
def editar_perfil(request):
    
    usuario= request.user

    if request.method == 'POST':
        formulario= User_edit_form(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()

            return render(request, 'blogApp/inicio.html', {'usuario':usuario, 'mensaje': 'Perfil editado con exito'})
    else:
        formulario= User_edit_form(instance=usuario)
    return render (request, 'blogApp/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})


#Función para pages, con paginador 
def pages(request):
    posteos= Blog_post.objects.all()
    page= request.GET.get("page")
    paginator=Paginator(posteos, 2)
    try:
        posteos= paginator.page(page)
    except PageNotAnInteger:
        posteos= paginator.page(1)
    except EmptyPage:
        posteos= paginator.page(paginator.num_pages)

    return render(request, "blogApp/pages.html", {'posteos':posteos}, )

#def vista_post(request):
    
    #return render(request, "blogApp/post.html")
 
class Post_detalle(DetailView):
    model= Blog_post
    template_name= "blogApp/post.html"
    slug_field= "slug"


class Crear_post(CreateView):
    model= Blog_post
    template_name= 'blogApp/crear_post.html'
    fields= ['titulo', 'subtitulo','cuerpo','autor', 'imagen']

class Editar_post(UpdateView):
    model= Blog_post
    template_name= 'blogApp/editar_post.html'
    fields= ['titulo', 'subtitulo','cuerpo','autor', 'imagen']

class Eliminar_post(DeleteView):
    model= Blog_post
    template_name= 'blogApp/borrar_post.html'
    success_url= reverse_lazy('pages')