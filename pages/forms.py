from django import forms
from books.models import BookHave

class BookHaveCreateForm(forms.ModelForm):
    class Meta:
        model = BookHave
        fields = [
            'category',
            'name',
            'author',
            'description',
            'image',
        ]