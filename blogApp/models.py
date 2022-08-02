from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

#ckeditor para poder editar post
from ckeditor.fields import RichTextField



class blog_post(models.Model):
    titulo= models.CharField(max_length=200, blank=True, null=True)
    subtítulo= models.TextField()
    cuerpo= RichTextField(blank=True, null=True)
    autor= models.CharField(max_length=20)
    fecha= models.DateField()
    imagen= models.ImageField(upload_to='media')

    def __str__(self):
        return f"Título: {self.titulo} - Subtítulo {self.subtítulo} - Cuerpo {self.cuerpo} - Autor {self.autor} - Imagen {self.imagen}"


class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank= True)



