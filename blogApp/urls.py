from django.urls import path
from blogApp import views
from blogApp.views import *
from django.contrib.auth.views import LogoutView

#class en view para pages (modo distinto para listar posts)
from .views import blog_post

urlpatterns = [
   
   path('', views.inicio, name='inicio'),

   #Vistas inicio de sesion, registo, logout

   path('login/', views.login_usuario, name= 'login'),
   path('registro/', views.registro, name= 'registro'),
   path('logout/', LogoutView.as_view(template_name= 'blogApp/logout.html'), name= 'logout'),
   path('editarPerfil/', views.editar_perfil, name= 'editarPerfil'),
   
   #url tipo class para listar pages
   


]