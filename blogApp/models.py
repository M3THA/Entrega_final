from django.db import models
from django.contrib.auth.models import User

#ckeditor para poder editar post
from ckeditor_uploader.fields import RichTextUploadingField

#slug para agregar un id rápido para los posts
from autoslug import AutoSlugField

#para asignar al usuario como autor del post
from django.contrib.auth import get_user_model

User= get_user_model()

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil= models.ImageField(upload_to="media")

class Blog_post(models.Model):
    titulo= models.CharField(max_length=50, blank=True, null=True)
    slug= AutoSlugField(populate_from= 'titulo')
    subtitulo= models.TextField(max_length=70, blank=True, null=True)
    cuerpo= RichTextUploadingField(blank=True, null=True)
    autor= models.CharField(max_length=20)
    fecha= models.DateField(auto_now_add= True)
    imagen= models.ImageField(upload_to='media')

    def __str__(self):
        return f"Título: {self.titulo}  - Autor {self.autor} - Fecha {self.fecha}"

