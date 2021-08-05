from django import forms
from django.db.models import fields

from .models import *

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Users
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username','names','surnames','cycle','tecnology','image','phone','email']
        labels = {
            'username': 'Cedula de Ciudadania',
            'names': 'Nombres Completos',
            'surnames': 'Apellidos Completos',
            'cycle': 'Ciclo Actual',
            'tecnology': 'Carrera',
            'image': 'Fotografia',
            'phone': 'Numero Telefonico',
            'email': 'Correo Electronico'
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nombre'
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','image','category']
        labels = {
            'title': 'Titulo del Libro',
            'author': 'Autor',
            'image': 'Portada',
            'category': 'Categoria'
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','book','deliver_date']
        labels = {
            'user': 'Estudiante',
            'book': 'Libro',
            'deliver_date': 'Fecha de Entrega'
        }