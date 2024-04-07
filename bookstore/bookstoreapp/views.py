from django.shortcuts import render
from django.http import HttpResponse
import json 
from .models import Books
from django.shortcuts import get_object_or_404 , redirect , reverse  
from django.urls import reverse
from  bookstoreapp.forms import BookForm 
from category.models import Category

# Data for books 
books = [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'numberOfPages': 100,
        'author': 'F. Scott Fitzgerald',
        'price': 10,
        'image': 'images1.jpg'
        
    },
    {
        'id': 2,
        'title': '1984',
        'numberOfPages': 100,
        'author': 'George Orwell',
        'price': 10,
        'image': 'images2.jpg'
    },
    {
        'id': 3,
        'title': 'To Kill a Mockingbird',
        'numberOfPages': 100,
        'author': 'Harper Lee',
        'price': 10,
        'image': 'images3.jpg'
    }
]

def AboutUs(request):
    return render(request, 'crud/aboutus.html')

def ContactUs(request):
    return render(request, 'crud/contactus.html')

def Books_index(request):
    books = Books.objects.all()
    return render(request, 'crud/index.html', context={'books': books})

def BookDetails(request, id):
    # book = Books.objects.get(id=id)
    book =get_object_or_404(Books, id=id)
    return render(request, 'crud/bookDetail.html', context={'book': book})

def BookDelete(request, id):
    book =get_object_or_404(Books, id=id)
    book.delete()
    url = reverse('Books.index')
    return redirect(url)


def BookCreate(request):
    if request.method == 'POST':
        if request.FILES:
            image = request.FILES['image']
        else:
            image = 'default.jpg'
        title = request.POST['title']
        numberOfPages = request.POST['numberOfpages']
        author = request.POST['author']
        price = request.POST['price']
        image = request.FILES['image']
        book = Books(title=title, numberOfpages=numberOfPages, author=author, price=price, image=image)
        book.save()
        url = reverse('Books.index')
        return redirect(url)
    return render(request, 'crud/create.html')

def BookUpdate(request, id):
    book = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        if request.FILES:
            image = request.FILES['image']
            book.image = image
        
        book.title = request.POST['title']
        book.numberOfPages = request.POST['numberOfpages']
        book.author = request.POST['author']
        book.price = request.POST['price']
        

        
        book.save()
        url = reverse('Books.index')
        return redirect(url)
    return render(request, 'crud/update.html', context={'book': book})






#############
## create book using forms

def Book_Create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('Books.index')
        
    return render(request, 'crud/create.html', {'form': form})

       

###3 update books using forms
def Book_Update(request, id):
    book = Books.get_book_by_id(id) 
    form = BookForm(instance=book)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('Books.index')
    
    return render(request, 'crud/update.html', {'form': form})
    
###### 
