from rest_framework import serializers

from .models import *

# ************************************* SERIALIZADORES PARA LOGIN ******************************************************************

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'names',
            'phone',
        )

# ************************************* SERIALIZADORES PARA USUARIOS ******************************************************************

# *** SERIALIZADOR PARA CREAR, ACTUALIZAR Y ELIMINAR USUARIOS ***
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    # Encriptamos la contraseña al guardar un nuevo usuario
    def create(self,validated_data):
        user = Users(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Encriptamos la contraseña al actualizar un usuario(si en caso no lo esta)
    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

# *** SERIALIZADOR PARA LISTAR USUARIOS ***
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
    # Optimizamos la consulta que llega de la vista para listar los usuarios, trayendo solo los necesarios
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'names': instance['names'],
            'email': instance['email'],
            'password': instance['password']
        }

# ************************************* SERIALIZADORES PARA CATEGORIAS ******************************************************************

# *** SERIALIZADOR PARA CREAR, ACTUALIZAR Y ELIMINAR CATEGORIAS ***
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# ************************************* SERIALIZADORES PARA LIBROS ******************************************************************

# *** SERIALIZADOR PARA CREAR, ACTUALIZAR Y ELIMINAR LIBROS ***
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# ************************************* SERIALIZADORES PARA PEDIDOS ******************************************************************

# *** SERIALIZADOR PARA CREAR, ACTUALIZAR Y ELIMINAR PEDIDOS ***
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
