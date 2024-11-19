from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [ "book_name", "book_desc", "book_image"]

        labels = {
            'book_name' : "Enter Name",
            'book_desc' : "book description",
            'book_image' :"book image"
        }

        widgets = {
            'book_name': forms.TextInput(attrs={'class':'form-control'}),
            'book_desc' :forms.Textarea(attrs={'class':'form-control'}),
            'book_image': forms.FileInput(attrs={'class': 'form-control'})
        }