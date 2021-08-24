from django import forms

from django.db.models import fields

from .models import *

from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput())

    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Users
        fields = ['username', 'password']

class UserForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username','names','surnames','cycle','tecnology','image','phone','email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError("No coinciden las contraseñas")
        return password2

    def save(self,commit=True):
        user = super(UserForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserFormEdit(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Users
        fields = ['username','password','names','surnames','cycle','tecnology','image','phone','email']

    def clean_password(self):
        return self.initial['password']

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

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','book','deliver_date']
        labels = {
            'user': 'Estudiante',
            'book': 'Libro',
            'deliver_date': 'Fecha de Entrega'
        }
        widgets = {

            'deliver_date': DateTimeInput(attrs={'class': 'form-control'}),

        }
