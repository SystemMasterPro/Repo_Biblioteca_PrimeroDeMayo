from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils.safestring import mark_safe

from django.conf import settings

from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def create_user(self,email,username,names,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')
        if not names:
            raise ValueError('El usuario debe tener un nombre!')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            names = names
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, names, password):
        user = self.create_user(
            email = email,
            username=username,
            names=names,
            password=password
        )

        user.user_admin = True
        user.save()
        return user

def url_user(self, filename):
    route = "static/images/Users/%s/%s" % (self.names, str(filename))
    return route


Tecnologies = [
    ('TECNOLOGIA SUPERIOR EN DESARROLLO DE SOFTWARE',
    'TECNOLOGIA SUPERIOR EN DESARROLLO DE SOFTWARE'),
    ('TECNOLOGIA SUPERIOR EN CONTABILIDAD', 'TECNOLOGIA SUPERIOR EN CONTABILIDAD'),
    ('Docente','Docente'),
]

Level = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('Egresado','Egresado'),
    ('Docente','Docente'),
]

class Users(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Numero de cedula', unique=True,max_length=10)
    names = models.CharField('Nombres',max_length=150,blank=True,null=True)
    surnames = models.CharField('Apellidos',max_length=150,blank=True, null=True)
    cycle = models.CharField('Ciclo', max_length=100,choices=Level, default='available')
    tecnology = models.CharField('Tecnologia',max_length=100,choices=Tecnologies,default='available')
    image = models.ImageField('Imagen',upload_to=url_user,blank=True, null=True)
    user_active = models.BooleanField(default=True, verbose_name='usuario activo')
    user_admin = models.BooleanField(default=False, verbose_name='usuario administrador')
    phone = models.IntegerField('Telefono',blank=True, null=True)
    email = models.EmailField('Correo', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    historical = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','names']

    def __str__(self):
        return self.names

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.user_admin

    def image_user(self):
        return mark_safe('<a href="/%s" ><img src="/%s" height="80px" width="80px"/></a>' % (self.image, self.image))
    image_user.allow_tags = True

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['names']


class Librarian(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.OneToOneField(to= settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField('Rol Desempeñado',max_length=100,default='Bibliotecari@')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'bibliotecario'
        verbose_name_plural = 'bibliotecarios'
        ordering = ['name']


class Secretary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.OneToOneField(to = settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField('Rol Desempeñado',max_length=100, default='Secretari@')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'secretaria'
        verbose_name_plural = 'secretarias'
        ordering = ['name']

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre',max_length=100)
    state = models.BooleanField('Estado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

def url_book(self, filename):
    route = "static/images/Books/%s/%s" % (self.title, str(filename))
    return route

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Titulo',max_length=150)
    author = models.CharField('Autor',max_length=150)
    state = models.BooleanField('Estado',default=True)
    image = models.ImageField('Imagen', upload_to=url_book, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def image_book(self):
        return mark_safe('<a href="/%s" ><img src="/%s" height="50px" width="50px" /></a>' % (self.image, self.image))
    image_book.allow_tags = True

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'
        ordering = ['title']

    def __str__(self):
        return self.title

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    state = models.BooleanField('Estado',default=True)
    deliver_date = models.DateTimeField('Fecha de Entrega')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']
