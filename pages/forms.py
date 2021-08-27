from django import forms
from books.models import BookHave, BookNeed

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
        widgets = {
                'category': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Full Name'}),
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Django for Professionals'}),
                'author': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'William S. Vincent'}),
                'description': forms.TextInput(
                    attrs={'class' : 'form-control', 'placeholder' : '...'}),
                # image
            }
        

class BookNeedCreateForm(forms.ModelForm):
    class Meta:
        model = BookNeed
        fields = [
            'category',
            'name',
            'author',
        ]