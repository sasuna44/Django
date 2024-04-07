from django.urls import path
from .views import AboutUs, ContactUs, Books_index ,BookDetails , BookDelete ,Book_Create ,Book_Update
from category.views import login_view
urlpatterns = [
    path('aboutus/', AboutUs, name='AboutUspage'),
    path('contactus/', ContactUs, name='ContactUspage'),
    path('', Books_index, name="Books.index"),
    path('<int:id>', BookDetails, name="book.show"),
    path('<int:id>/delete',BookDelete, name="book.delete"),
    path('create/', Book_Create, name="Book.create"),
    path('<int:id>/update', Book_Update, name="book.update"),
    path('category/', login_view, name="login.index"),

]
