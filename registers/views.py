from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate

from django.urls import reverse_lazy

from rest_framework import status

from rest_framework.response import Response

from .forms import *

from .models import *

from django.views.generic import ListView, UpdateView, CreateView, DetailView

from rest_framework import viewsets

from .serializers import *

from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from registers.authentication_models import Authenticate

from django.db.models import Q


# ******************************************** LOGIN ADMIN O DASHBOARD **************************************************************
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active and user.user_admin:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                messages.error(request, 'No tienes permisos de admin!')
            messages.error(request, 'DATOS INVALIDOS!')
        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'login.html', ctx)

# ******************************************** LOGOUT ADMIN O DASHBOARD *************************************************************
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# ******************************************** HOME ADMIN O DASHBOARD **************************
@login_required(login_url='/')
def home_view(request):
    return render(request, 'index.html')

# BUSQUEDA USUARIOS
def search_view(request):
    search = request.GET.get("buscar")
    queryset = []
    print(queryset)
    if search:
        queryset = Users.objects.filter(
            Q(username__icontains=search) |
            Q(names__icontains=search)
        ).distinct()
    elif search is '':
        messages.add_message(request, messages.WARNING, "SIN RESULTADOS")
    else:
        queryset = []
    return render(request, 'Users/search_user.html', {'data': queryset})

# BUSQUEDA LIBROS
def search_view_books(request):
    search = request.GET.get("buscar")
    queryset = []
    print(queryset)
    if search:
        queryset = Book.objects.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search)
        ).distinct()
    elif search is '':
        messages.add_message(request, messages.WARNING, "SIN RESULTADOS")
    else:
        queryset = []
    return render(request, 'Book/search_book.html', {'data': queryset})

# BUSQUEDA PEDIDOS
def search_view_orders(request):
    search = request.GET.get("buscar")
    queryset = []
    print(queryset)
    if search:
        queryset = Order.objects.filter(
            Q(book__icontains=search) |
            Q(user__icontains=search)
        ).distinct()
    elif search is '':
        messages.add_message(request, messages.WARNING, "SIN RESULTADOS")
    else:
        queryset = []
    return render(request, 'Order/search_order.html', {'data': queryset})
    
# ********************************************* VISTAS BASADAS EN CLASES PARA EL ADMIN O DASHBOARD *******************************************************
# *** CLASE USUARIO ***
# LISTAR TODOS LOS USUARIOS
class List_Users_View(ListView):
    model = Users
    template_name = 'Users/list_users.html'
    queryset = Users.objects.filter(user_active=True)
    context_object_name = 'users'

# LISTAR USUARIOS SUSPENDIDOS
class List_Users_Suspend_View(ListView):
    model = Users
    template_name = 'Users/list_users_suspend.html'
    queryset = Users.objects.filter(user_active=False)
    context_object_name = 'users'

# CREAR USUARIO
class New_User_View(SuccessMessageMixin, CreateView):
    model = Users
    form_class = UserForm
    template_name = 'Users/new_user.html'
    success_url = reverse_lazy('view_list_users')
    success_message = "Usuario creado con exito!"

    def form_invalid(self, form):
        messages.add_message(self.request,messages.ERROR,"Usuario o Password mal ingresados!!!")
        return redirect('view_list_users')

# ACTUALIZAR USUARIO
class Update_User_View(SuccessMessageMixin,UpdateView):
    model = Users
    form_class = UserFormEdit
    template_name = 'Users/update_user.html'
    success_url = reverse_lazy('view_list_users')
    success_message = "Usuario actualizado"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, "Usuario ya registrado!!!")
        return redirect('view_list_users')

# DESABILITAR UN USUARIO EN EL ADMIN O DASHBOARD
class Disable_User_View(DetailView):
    model = Users
    template_name = 'Users/disable_user.html'
    def post(self,request,pk,*args,**kwargs):
        object = Users.objects.get(id=pk)
        object.user_active = False
        object.save()
        return redirect('view_list_users')
# HABILITAR USUARIO EN EL ADMIN O DASHBOARD
class Enable_User_View(DetailView):
    model = Users
    template_name = 'Users/enable_user.html'
    def post(self,request,pk,*args,**kwargs):
        object = Users.objects.get(id=pk)
        object.user_active = True
        object.save()
        return redirect('view_list_users')

# *** CLASE CATEGORIAS ***
# LISTAR TODAS LAS CATEGORIAS
class List_Categories_View(ListView):
    model = Category
    template_name = 'Category/list_categories.html'
    queryset = Category.objects.filter(state=True)
    context_object_name = 'categories'
# CREAR NUEVA CATEGORIA
class New_Category_View(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Category/new_category.html'
    success_url = reverse_lazy('view_list_categories')
    success_message = "Categoria creada con exito!"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Categoria YA REGISTRADA!!")
        return redirect('view_list_categories')

# ACTUALIZAR CATAEGORIA
class Update_Category_View(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Category/update_category.html'
    success_url = reverse_lazy('view_list_categories')
    success_message = "Categoria actualizada"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, "Categoria EXISTENTE!!")
        return redirect('view_list_categories')

# DESABILITAR CATEGORIA EN EL ADMIN O DASHBOARD
class Delete_Category_View(DetailView):
    model = Category
    template_name = 'Category/delete_category.html'
    def post(self,request,pk,*args,**kwargs):
        object = Category.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_categories')

# *** CLASE LIBROS ***
# LISTAR TODOS LOS LIBROS
class List_Books_View(ListView):
    model = Book
    template_name = 'Book/list_books.html'
    queryset = Book.objects.filter(state=True)
    context_object_name = 'books'
# CREAR NUEVO LIBRO
class New_Book_View(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'Book/new_book.html'
    success_url = reverse_lazy('view_list_books')
    success_message = "Libro creado con exito"
# ACTUALIZAR LIBRO
class Update_Book_View(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'Book/update_book.html'
    success_url = reverse_lazy('view_list_books')
    success_message = "Libro actualizado"
# DESABILITAR LIBRO EN EL ADMIN O DASHBOARD
class Delete_Book_View(DetailView):
    model = Book
    template_name = 'Book/delete_book.html'
    def post(self,request,pk,*args,**kwargs):
        object = Book.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_books')

# *** CLASE PEDIDOS ***
# LISTAR PEDIDOS
class List_Orders_View(ListView):
    model = Order
    template_name = 'Order/list_orders.html'
    queryset = Order.objects.filter(state=True)
    context_object_name = 'orders'

# PEDIDOS ARCHIVADOS
class List_Order_Archivate_View(ListView):
    model = Order
    template_name = 'Order/archivate_orders.html'
    queryset = Order.objects.filter(state=False)
    context_object_name = 'orders'

# NUEVO PEDIDO
class New_Order_View(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'Order/new_order.html'
    success_url = reverse_lazy('view_list_orders')
# ACTUALIZAR PEDIDO
class Update_Order_View(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'Order/update_order.html'
    success_url = reverse_lazy('view_list_orders')
    success_message = "Pedido Actualizado"
# DESABILITAR PEDIDO EN EL ADMIN O DASHBOARD
class Delete_Order_View(DetailView):
    model = Order
    template_name = 'Order/delete_order.html'
    def post(self,request,pk,*args,**kwargs):
        object = Order.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_orders')

# ************************************************************** DJANGO REST FRAMEWORK **********************************************************************************

# ********************************************************* VISTAS BASADAS EN CLASES *******************************************************************************************

# **** VISTA LOGIN FRONTEND CON TOKEN ****

class LoginUserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserTokenSerializer

# **** CLASE USUARIO ****

class UserViewSet(Authenticate, viewsets.ModelViewSet):

    # SERIALIZABLE DEL MODELO USUARIO
    serializer_class = UserSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(user_active = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, user_active = True).first()

    # Sobreescribimos las funciones que utilizaremos en las peticiones HTTP

    # LISTAR
    def list(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(user_serializer.data,status=status.HTTP_200_OK)

    # CREAR
    def create(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario creado con exito!'},status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # ACTUALIZAR
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            user_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR
    def destroy(self,request,pk=None):
        user_serializer = self.get_queryset().filter(id=pk).first()
        if user_serializer:
            user_serializer.user_active = False
            user_serializer.save()
            return Response({'message':'Usuario eliminado correctamente!'},status=status.HTTP_200_OK)
        return Response({'message':'No existe un usuario con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

# **** CLASE CATEGORIA ****
class CategoryViewSet(Authenticate,viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# *** CLASE LIBRO ***
class BookViewSet(Authenticate, viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# *** CLASE PEDIDO ***
class OrderViewSet(Authenticate,viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
