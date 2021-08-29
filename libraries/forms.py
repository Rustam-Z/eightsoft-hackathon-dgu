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
    
    # add the css class to form 
    def __init__(self, *args, **kwargs):
        super(LibraryRegionForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({'class' : 'form-control'})  
        
