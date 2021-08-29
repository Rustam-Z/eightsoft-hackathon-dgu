from django.contrib import admin
from .models import Library, Book

# Register your models here.


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
    list_filter = [
        'region',
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'author',
        'library',
        'category',
        'available',
    ]

    list_filter = [
        'available',
        'created',
    ]

    list_editable = ['available']