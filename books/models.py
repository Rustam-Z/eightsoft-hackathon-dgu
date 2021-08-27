import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from categories.models import Category


# Create your models here.


class BookHave(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category = models.ForeignKey(Category,
                                 verbose_name='toifasi',
                                 related_name='books_have',
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

    user = models.ForeignKey(
        get_user_model(),
        related_name='books_have',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_have_detail', args=[str(self.id)])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Mavjud Kitob'
        verbose_name_plural = 'Mavjud Kitoblar 📚➡️'
        
        
class BookNeed(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category = models.ForeignKey(Category,
                                 verbose_name='toifasi',
                                 related_name='books_need',
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name='kitob nomi', max_length=255)
    author = models.CharField(verbose_name='muallif', max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        get_user_model(),
        related_name='books_need',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_need_detail', args=[str(self.id)])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Kerakli Kitob'
        verbose_name_plural = 'Kerakli Kitoblar 📚⬅️'
