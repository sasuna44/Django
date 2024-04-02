from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'aboutus.html')

def ContactUs(request):
    return render(request, 'contactus.html')

def Books(request):
    return render(request, 'index.html',  {'books': books})


def BookDetail(request, id):
    filtered_books = [book for book in books if book['id'] == id]
    
    if len(filtered_books) > 0:
        book = filtered_books[0]
        return render(request, 'bookDetail.html', {'book': book})
    else:
        return HttpResponse("Book not found")
