from django.contrib import admin
from .models import BookHave, BookNeed

# Register your models here.


@admin.register(BookHave)
class BookHaveAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'author',
        'category',
        'available',
        'created',
    ]

    list_filter = [
        'available',
        'created',
    ]

    list_editable = ['available']
    
    
@admin.register(BookNeed)
class BookNeedAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'author',
        'category',
        'created',
    ]

    list_filter = [
        'created',
    ]
