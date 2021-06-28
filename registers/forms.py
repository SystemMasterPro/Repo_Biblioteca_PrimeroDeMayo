from django import forms
from django.db.models import fields

from .models import *

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username', 'password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['dni','names','surnames','cycle','tecnology','image','phone','email']
        labels = {
            'dni': 'Cedula de Ciudadania',
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
        fields = ['student','book','deliver_date']
        labels = {
            'student': 'Estudiante',
            'book': 'Libro',
            'deliver_date': 'Fecha de Entrega'
        }