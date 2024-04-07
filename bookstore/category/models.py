from django.db import models
# Create your models here.
from django.shortcuts import reverse , get_object_or_404    

class Category(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    description = models.CharField(max_length=200 , null=True , blank=True)
    
    def __str__(self):
        return f"{self.name}"
    @classmethod
    def get_all_categories(cls):
        Categories = cls.objects.all()
        return Categories
    @classmethod
    def get_category_by_id(cls, id):
        return get_object_or_404(cls, pk=id)
    @property
    def show_url(self):
        url = reverse('category.show', args=[self.id])
        return url