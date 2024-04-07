from django import forms
from bookstoreapp.models import Books
from category.models import Category


class BookForm(forms.ModelForm):
    Category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category'),
    class Meta:
        model = Books
        fields = ['title', 'author', 'price', 'numberOfpages', 'image' ,'category']
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'price': 'Price',
            'numberOfpages': 'Number of Pages',
            'image': 'Book Image',
            'category': 'Category',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control text-start mb-3', 'placeholder': 'Enter title'}),
            'author': forms.TextInput(attrs={'class': 'form-control text-start mb-3', 'placeholder': 'Enter author'}),
            'price': forms.NumberInput(attrs={'class': 'form-control text-start mb-3', 'placeholder': 'Enter price'}),
            'numberOfpages': forms.NumberInput(attrs={'class': 'form-control text-start mb-3', 'placeholder': 'Enter number of pages'}),
            'image': forms.FileInput(attrs={'class': 'form-control text-start mb-3'}),
            'category': forms.Select(attrs={'class': 'form-control text-start mb-3'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        Category = cleaned_data.get('category')
        if not Category:
            raise forms.ValidationError('Please select a category')

    def clean_title(self):  
        title = self.cleaned_data['title']
        if self.instance.pk is None:
            title_found = Books.objects.filter(title__iexact=title).exists()
            if title_found:
                raise forms.ValidationError('A book with this title already exists')
        return title

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError('Please Add Image of the book !')
        return image
    def clean_author(self):
        author = self.cleaned_data['author']
        if not author:
            raise forms.ValidationError('Please Enter the name of the Author of the book !')
        if len(author) < 4:
                raise forms.ValidationError('Author name must be at least 4 characters long !')
        return author
    def clean_price(self):
        price = self.cleaned_data['price']
        if not price:
            raise forms.ValidationError('Please Enter the price of the book !')
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0 !')
        return price
    def clean_numberOfpages(self):
        numberOfpages = self.cleaned_data['numberOfpages']
        if not numberOfpages:
            raise forms.ValidationError('Please Enter the number of pages of the book !')
        if numberOfpages <= 0:
            raise forms.ValidationError('Number of pages must be greater than 0 !')
        return numberOfpages
    