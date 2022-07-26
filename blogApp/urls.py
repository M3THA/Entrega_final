from django.urls import path
from blogApp import views
from blogApp.views import *

urlpatterns = [
   
   path('inicio/', views.inicio, name='inicio'),

   #Vistas inicio de sesion, registo

   path('login/', views.login_usuario, name= 'login'),
   path('registro/', views.registro, name= 'registro'),



]