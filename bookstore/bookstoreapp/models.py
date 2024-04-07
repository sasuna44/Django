from django.db import models
from django.shortcuts import reverse , get_object_or_404
from category.models import Category

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    numberOfpages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/books/images',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True , blank=True, related_name='books')

    def __str__(self):
        return f'{self.title}'

    @property
    def show_url(self):
        url = reverse('book.show', args=[self.id])
        return url 

    @property
    def delete_url(self): 
        url = reverse('book.delete', args=[self.id])
        return url
    @property
    def update_url(self):
        url = reverse('book.update', args=[self.id])
        return url
    @property
    def image_url(self):
        return f'/media/{self.image}'
    @classmethod
    def get_book_by_id(cls , id):
        return get_object_or_404(cls, pk=id)

