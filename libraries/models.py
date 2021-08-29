from django.db import models
from django.urls import reverse
import uuid
from categories.models import Category
# Create your models here.


class Library(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(verbose_name='kutubxona nomi', max_length=200, db_index=True)
    
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
    
    region = models.CharField(verbose_name='shahar yoki viloyatingizni tanlang',
                              max_length=255,
                              choices=REGIONS,
                              default='Tashkent')
    
    phone = models.CharField(verbose_name='telefon', max_length=255, blank=True)
    telegram = models.URLField(verbose_name='telegram URL', blank=True)
    image = models.ImageField(verbose_name='foto surat', upload_to='libraries/', blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Kutubxona'
        verbose_name_plural = 'Kutubxonalar 🏫'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_list_by_libraries', args=[str(self.slug)])
    
    
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    library = models.ForeignKey(Library,
                                 verbose_name='kutubxona',
                                 related_name='books',
                                 on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name='kitob nomi', max_length=255)
    author = models.CharField(verbose_name='muallif', max_length=255)
    image = models.ImageField(verbose_name='kitob rasmini yuklash',
                              upload_to='books/',
                              blank=True)
    description = models.TextField(verbose_name='tavsifi', blank=True)
    available = models.BooleanField(verbose_name='mavjud?', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,
                                 verbose_name='toifasi',
                                 related_name='library_books',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.library}"

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    class Meta:
        ordering = ('name', 'library')
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar 📚'