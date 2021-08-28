from django import forms
from .models import Library

REGIONS = (
    ('Tashkent', 'Tashkent'),
    ('Andijan', 'Andijan'),
    ('Bukhara', 'Bukhara'),
    ('Fergana', 'Fergana'),
    ('Jizzakh', 'Jizzakh'),
    ('Xorazm', 'Xorazm'),
    ('Namangan', 'Namangan'),
    ('Navoiy', 'Navoiy'),
    ('Qashqadaryo', 'Qashqadaryo'),
    ('Samarkand', 'Samarkand'),
    ('Surxondaryo', 'Surxondaryo'),
    ('Karakalpakstan', 'Karakalpakstan'),
)

class LibraryRegionForm(forms.ModelForm):
    region = forms.ChoiceField(choices=REGIONS,)
    class Meta:
        model = Library
        fields = [
            'region',
        ]

