from django import forms

from django.db.models import fields
from django.forms import widgets

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
        widgets = {
            'username':forms.TextInput(attrs={
                'placeholder': 'Ingrese el numero de cedula ecuatoriana'
            }),
            'names': forms.TextInput(attrs={
                'placeholder': 'Nombres Completos'
            }),
            'surnames': forms.TextInput(attrs={
                'placeholder': 'Apellidos Completos'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder':'Omita el 0 inicial de su numero celular. Ejemplo:962093738'
            }),
            'email': forms.TextInput(attrs={
                'placeholder':'Ingrese el correo electronico'
            })
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        suma = 0
        for i in range(len(username)-1):
            x = int(username[i])
            if i % 2 == 0:
                x = x *2
                if x > 9:
                    x = x - 9
            suma = suma + x
        if suma%10 != 0:
            result = 10 - (suma%10)
            if int(username[-1]) == result:
                return username
            else:
                raise forms.ValidationError("Cedula No VALIDA!")
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        contador = 0
        for i in range(len(phone)):
            contador = contador + 1
        if contador == 9:
            for x in range(len(phone)):
                t = int(phone[0])
                if t == 9:
                    return phone
                else:
                    raise forms.ValidationError("Telefono No VALIDO!")

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
        widgets = {
            'names': forms.TextInput(attrs={
                'placeholder': 'Nombres Completos'
            }),
            'surnames': forms.TextInput(attrs={
                'placeholder': 'Apellidos Completos'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Omita el 0 inicial de su numero celular. Ejemplo:962093738'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Ingrese el correo electronico'
            })
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        suma = 0
        for i in range(len(username)-1):
            x = int(username[i])
            if i % 2 == 0:
                x = x * 2
                if x > 9:
                    x = x - 9
            suma = suma + x
        if suma % 10 != 0:
            result = 10 - (suma % 10)
            if int(username[-1]) == result:
                return username
            else:
                raise forms.ValidationError("Cedula No VALIDA!")

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        contador = 0
        for i in range(len(phone)):
            contador = contador + 1
        if contador == 9:
            for x in range(len(phone)):
                t = int(phone[0])
                if t == 9:
                    return phone
                else:
                    raise forms.ValidationError("Telefono No VALIDO!")

    def clean_password(self):
        return self.initial['password']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nombre'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder':'Ingrese el nombre para la categoria'
            })
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'image', 'stock', 'category']
        labels = {
            'title': 'Titulo del Libro',
            'author': 'Autor',
            'image': 'Portada',
            'stock':'Cantidad',
            'category': 'Categoria'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Nombre del libro'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Autor del libro'
            })
        }

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book','deliver_date']
        labels = {
            'book': 'Libro',
            'deliver_date': 'Fecha de Entrega'
        }
        widgets = {
            'deliver_date': DateTimeInput(attrs={'class': 'form-control'}),
        }
