from django.urls import path
from blogApp import views
from blogApp.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
   path('', views.inicio, name='inicio'),

   #Vistas inicio de sesion, registo, logout

   path('login/', views.login_usuario, name= 'login'),
   path('registro/', views.registro, name= 'registro'),
   path('logout/', LogoutView.as_view(template_name= 'blogApp/logout.html'), name= 'logout'),
   path('editarPerfil/', views.editar_perfil, name= 'editarPerfil'),
   path('pages/', views.pages, name= 'pages'),

   #url tipo class darle slug a los posts
   path('<slug>', Post_detalle.as_view(), name='post'),

   #url para crear posts
   path('crear_post/', Crear_post.as_view(), name='crear_post'),
   
   path('editar_post/<slug>', Editar_post.as_view(), name='editar_post'),
   path('<slug>/eliminar', Eliminar_post.as_view(), name='eliminar_post'),

]