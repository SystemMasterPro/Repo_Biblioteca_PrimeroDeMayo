from django import urls
from django.urls import include, path

from .views import *

from . import views

from rest_framework import routers, urlpatterns

from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('categories', views.CategoryViewSet)
router.register('books', views.BookViewSet)
router.register('orders', views.OrderViewSet)


urlpatterns = [
    # URLS PRINCIPALES
    path('', login_view, name='view_login'),
    path('home/', home_view, name='view_home'),
    path('logout/', logout_view, name='view_logout'),
    # URLS ESTUDIANTE
    path('home/list_students/', login_required(List_Student_View.as_view()), name='view_list_students'),
    path('home/list_students/edit_student/<int:pk>/', login_required(Update_Student_View.as_view()), name='view_edit_student'),
    path('home/list_students/delete_student/<int:pk>/', login_required(Delete_Student_View.as_view()), name='view_delete_student'),
    path('new_student/',login_required(New_Student_View.as_view()),name='view_new_student'),
    # URLS CATEGORIAS
    path('home/list_categories/', login_required(List_Categories_View.as_view()), name='view_list_categories'),
    path('home/list_categories/edit_category/<int:pk>/', login_required(Update_Category_View.as_view()), name='view_edit_category'),
    path('home/list_categories/delete_category/<int:pk>/', login_required(Delete_Category_View.as_view()), name='view_delete_category'),
    path('new_category/',login_required(New_Category_View.as_view()),name='view_new_category'),
    # URLS LIBROS
    path('home/list_books/', login_required(List_Books_View.as_view()), name='view_list_books'),
    path('home/list_books/edit_book/<int:pk>/', login_required(Update_Book_View.as_view()), name='view_edit_book'),
    path('home/list_books/delete_book/<int:pk>/', login_required(Delete_Book_View.as_view()), name='view_delete_book'),
    path('new_book/',login_required(New_Book_View.as_view()),name='view_new_book'),
    # URLS ORDENES
    path('home/list_orders/', login_required(List_Orders_View.as_view()), name='view_list_orders'),
    path('home/list_orders/edit_order/<int:pk>/', login_required(Update_Order_View.as_view()), name='view_edit_order'),
    path('home/list_orders/delete_order/<int:pk>/', login_required(Delete_Order_View.as_view()), name='view_delete_order'),
    path('new_order/',login_required(New_Order_View.as_view()),name='view_new_order'),
    # API-REST
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]