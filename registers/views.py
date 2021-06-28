from django.db.models import query
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

from django.urls import reverse_lazy

from .forms import *

from .models import *

from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView

from rest_framework import viewsets

from .serializers import *

from django.contrib import messages

# LOGIN
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
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'login.html', ctx)

# LOGOUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# HOME
@login_required(login_url='/')
def home_view(request):
    order = Order.objects.all()
    ctx = {'order':order}
    return render(request, 'index.html', ctx)

# STUDENT
class List_Student_View(ListView):
    model = Student
    template_name = 'Student/list_students.html'
    queryset = Student.objects.filter(state=True)
    context_object_name = 'students'

class New_Student_View(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'Student/new_student.html'
    success_url = reverse_lazy('view_list_students')

class Update_Student_View(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'Student/update_student.html'
    success_url = reverse_lazy('view_list_students')

class Delete_Student_View(DetailView):
    model = Student
    template_name = 'Student/delete_student.html'
    def post(self,request,pk,*args,**kwargs):
        object = Student.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_students')

# CATEGORIES
class List_Categories_View(ListView):
    model = Category
    template_name = 'Category/list_categories.html'
    queryset = Category.objects.filter(state=True)
    context_object_name = 'categories'

class New_Category_View(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Category/new_category.html'
    success_url = reverse_lazy('view_list_categories')

class Update_Category_View(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Category/update_category.html'
    success_url = reverse_lazy('view_list_categories')

class Delete_Category_View(DetailView):
    model = Category
    template_name = 'Category/delete_category.html'
    def post(self,request,pk,*args,**kwargs):
        object = Category.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_categories')

# BOOKS
class List_Books_View(ListView):
    model = Book
    template_name = 'Book/list_books.html'
    queryset = Book.objects.filter(state=True)
    context_object_name = 'books'

class New_Book_View(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'Book/new_book.html'
    success_url = reverse_lazy('view_list_books')

class Update_Book_View(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'Book/update_book.html'
    success_url = reverse_lazy('view_list_books')

class Delete_Book_View(DetailView):
    model = Book
    template_name = 'Book/delete_book.html'
    def post(self,request,pk,*args,**kwargs):
        object = Book.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_books')

# ORDERS
class List_Orders_View(ListView):
    model = Order
    template_name = 'Order/list_orders.html'
    queryset = Order.objects.filter(state=True)
    context_object_name = 'orders'

class New_Order_View(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'Order/new_order.html'
    success_url = reverse_lazy('view_list_orders')

class Update_Order_View(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'Order/update_order.html'
    success_url = reverse_lazy('view_list_orders')

class Delete_Order_View(DetailView):
    model = Order
    template_name = 'Order/delete_order.html'
    def post(self,request,pk,*args,**kwargs):
        object = Order.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_orders')


# CLASS REST framework

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer