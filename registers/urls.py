from django import urls

from django.urls import include, path

from .views import *

from . import views

from rest_framework import routers

from django.contrib.auth.decorators import login_required

from registers.token import Login

router = routers.DefaultRouter()
router.register('login', views.LoginUserViewSet)
# Necesita un basename ya que no le especificamos en la vista
router.register('users', views.UserViewSet, basename = Users)
router.register('categories', views.CategoryViewSet)
router.register('books', views.BookViewSet)
router.register('orders', views.OrderViewSet)


urlpatterns = [
    # URLS PRINCIPALES
    path('', login_view, name='view_login'),
    path('home/', home_view, name='view_home'),
    path('logout/', logout_view, name='view_logout'),
    # URLS Usuarios
    path('home/list_users/', login_required(List_Users_View.as_view()), name='view_list_users'),
    path('home/list_users/suspend/', login_required(List_Users_Suspend_View.as_view()), name='view_list_users_suspend'),
    path('home/list_users/edit_user/<int:pk>/', login_required(Update_User_View.as_view()), name='view_edit_user'),
    path('home/list_users/disable_user/<int:pk>/', login_required(Disable_User_View.as_view()), name='view_disable_user'),
    path('home/list_users/enable_user/<int:pk>/', login_required(Enable_User_View.as_view()), name='view_enable_user'),
    path('new_user/',login_required(New_User_View.as_view()),name='view_new_user'),
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
    # URLS PEDIDOS
    path('home/list_orders/', login_required(List_Orders_View.as_view()), name='view_list_orders'),
    path('home/list_orders/edit_order/<int:pk>/', login_required(Update_Order_View.as_view()), name='view_edit_order'),
    path('home/list_orders/delete_order/<int:pk>/', login_required(Delete_Order_View.as_view()), name='view_delete_order'),
    path('new_order/',login_required(New_Order_View.as_view()),name='view_new_order'),
    # API-REST
    path('login/', Login.as_view(), name = 'login'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
