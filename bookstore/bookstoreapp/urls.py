from django.urls import path
from .views import AboutUs , ContactUs , Books , BookDetail

urlpatterns = [
    path('aboutus/',AboutUs , name='AboutUspage'),
    path('contactus/', ContactUs, name='ContactUspage'),
    path('books/', Books, name='Bookspage'),
    path('bookdails/<int:id>', BookDetail , name="BookDetails")
]
