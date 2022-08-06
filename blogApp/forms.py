from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blogApp.models import Blog_post




class User_register_form(UserCreationForm):

    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} 

    
class User_edit_form(UserCreationForm):

    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name= forms.CharField(max_length=50)
    first_name= forms.CharField(max_length=50)


    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name','first_name' ]
        help_texts = {k:"" for k in fields} 

class Crear_form(forms.ModelForm):
    class Meta:
        model= Blog_post
        fields= ['titulo', 'subtitulo','cuerpo','autor', 'imagen']

        widgets= {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }