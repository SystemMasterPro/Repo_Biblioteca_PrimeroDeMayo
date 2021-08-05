from django.contrib import admin

from .models import *

from import_export import resources

from import_export.admin import ImportExportModelAdmin

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
    class Meta:
        model = Users

class UsersAdmin(ImportExportModelAdmin):
    list_display = ('username','names','surnames','cycle','tecnology','image_user','phone','email')
    readonly_fields = ('created', 'updated')
    search_fields = ['username','names']
    resource_class = UsersResource

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name','state')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = CategoryResource

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):
    list_display = ('id','title','author','state','image_book','category')
    readonly_fields = ('created', 'updated')
    search_fields = ['title','author']
    resource_class = BookResource

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id','user','book','state','deliver_date')
    readonly_fields = ('created', 'updated')
    search_fields = ['id']
    resource_class = OrderResource


admin.site.register(Librarian,LibrarianAdmin)
admin.site.register(Secretary,SecretaryAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin)