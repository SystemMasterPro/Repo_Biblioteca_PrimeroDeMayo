from django.db import models

from django.contrib.auth.models import User

from django.utils.safestring import mark_safe

class Librarian(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    role = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Secretary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

def url_student(self, filename):
    route = "static/images/Students/%s/%s" % (self.names, str(filename))
    return route

Tecnologies = [
    ('TECNOLOGIA SUPERIOR EN DESARROLLO DE SOFTWARE', 'TECNOLOGIA SUPERIOR EN DESARROLLO DE SOFTWARE'),
    ('TECNOLOGIA SUPERIOR EN CONTABILIDAD', 'TECNOLOGIA SUPERIOR EN CONTABILIDAD'),
]

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField()
    names = models.CharField(max_length=150)
    surnames = models.CharField(max_length=150)
    cycle = models.IntegerField()
    tecnology = models.CharField(max_length=100,choices=Tecnologies,default='available')
    image = models.ImageField(upload_to=url_student)
    state = models.BooleanField('State', default=True)
    phone = models.IntegerField()
    email = models.EmailField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def image_student(self):
        return mark_safe('<a href="/%s" ><img src="/%s" height="50px" width="50px" /></a>' % (self.image, self.image))
    image_student.allow_tags = True

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['names']

    def __str__(self):
        return self.names

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

def url_book(self, filename):
    route = "static/images/Books/%s/%s" % (self.title, str(filename))
    return route

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    state = models.BooleanField('State',default=True)
    image = models.ImageField(upload_to=url_book)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def image_book(self):
        return mark_safe('<a href="/%s" ><img src="/%s" height="50px" width="50px" /></a>' % (self.image, self.image))
    image_book.allow_tags = True

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['title']

    def __str__(self):
        return self.title

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    state = models.BooleanField('State',default=True)
    deliver_date = models.DateField('Deliver Date')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['id']