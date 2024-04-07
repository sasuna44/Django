from django.urls import path
from .views import welcoming, category_index , category_details, Category_Create, Catergory_Update, delete_category, login_view


urlpatterns = [
    path('cat' , welcoming , name = 'welcoming'),
    path('main', category_index, name = 'category.main'),
    path('create', Category_Create, name = 'category.create'),
    path('<int:id>', category_details, name = 'category.show'),
    path('update/<int:id>', Catergory_Update, name = 'category.update'),
    path('delete/<int:id>', delete_category, name = 'category.delete'),
    path('' , login_view , name='login')
  
]
