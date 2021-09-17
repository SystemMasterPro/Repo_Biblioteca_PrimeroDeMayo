from django.contrib import admin
from django.db.models import fields

from .models import *

from import_export import resources

from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserForm, UserFormEdit

from django.contrib.auth.hashers import make_password

class UserAdmin(BaseUserAdmin):
    form = UserFormEdit
    add_form = UserForm

    list_display = ('username','names','phone')
    list_filter = ('user_admin',)
    fieldsets = (
    (None,{'fields':('username','password')}),
        ('Informacion', {'fields': ('names', 'surnames', 'cycle', 'tecnology', 'image_user', 'email')}),
    ('Permisos',{'fields':('user_admin','user_active')}),
    )
    search_fields = ['username',]
    ordering = ('names',)
    filter_horizontal = ()

class LibrarianResource(resources.ModelResource):
    class Meta:
        model = Librarian

class LibrarianAdmin(ImportExportModelAdmin):
    list_display = ('name','role')
    readonly_fields = ('created', 'updated')
    resource_class = LibrarianResource

class SecretaryResource(resources.ModelResource):
    class Meta:
        model = Secretary

class SecretaryAdmin(ImportExportModelAdmin):
    list_display = ('name','role')
    readonly_fields = ('created', 'updated')
    resource_class = SecretaryResource

class UsersResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        password = row['password']
        row['password'] = make_password(password)

    class Meta:
        model = Users
        fields = ('id','username', 'names', 'surnames', 'cycle','tecnology', 'phone', 'email', 'password')

class UsersAdmin(ImportExportModelAdmin, BaseUserAdmin):
    form = UserFormEdit
    add_form = UserForm
    list_display = ('username','names','surnames','cycle','tecnology','image_user','phone','email','password')
    list_filter = ('user_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informacion', {'fields': ('names', 'surnames','cycle', 'tecnology', 'email')}),
        ('Permisos', {'fields': ('user_admin', 'user_active')}),
    )
    readonly_fields = ('created', 'updated')
    search_fields = ['username','names']
    ordering = ('names',)
    filter_horizontal = ()
    resource_class = UsersResource

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id','name', 'state')

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name','state')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = CategoryResource

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ('id','title','author','stock','category__name',)

class BookAdmin(ImportExportModelAdmin):
    list_display = ('id','title','author','state','stock','image_book','category')
    readonly_fields = ('created', 'updated')
    search_fields = ['title','author']
    resource_class = BookResource

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ('id','user__username', 'book__title', 'deliver_date',)

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id','user','book','state','deliver_date')
    readonly_fields = ('created', 'updated')
    search_fields = ['id']
    resource_class = OrderResource

# admin.site.register(Users,UserAdmin)
admin.site.register(Librarian,LibrarianAdmin)
admin.site.register(Secretary,SecretaryAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin)
