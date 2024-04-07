from django.shortcuts import render
from django.shortcuts import get_object_or_404 , redirect , reverse  
from django.urls import reverse
from django.http import HttpResponse
from .models import Category
from .forms import CategoryForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def welcoming (request):
    return HttpResponse("<h1>Welcome to Categories <3 </h1>")
def category_index(request):
    categories = Category.get_all_categories()
    return render(request, 'category/main.html', { 'categories': categories})

def category_details(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'category/show.html', {'category': category})

def Category_Create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('category.main')
        
    return render(request, 'category/create.html', {'form': form})

def Catergory_Update(request, id):
    book = Category.get_category_by_id(id) 
    form = CategoryForm(instance=book)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('category.main')
    
    return render(request, 'category/edit.html', {'form': form})
    
def delete_category(request, id):
    book = Category.get_category_by_id(id)
    book.delete()
    return redirect('category.main')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None:
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('category.main')
            else:
                messages.error(request, 'Invalid password.')
        else:
            messages.error(request, 'User does not exist.')

    return render(request, 'category/index.html')