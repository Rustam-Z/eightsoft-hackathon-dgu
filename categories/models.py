from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(verbose_name='toifa nomi', max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Toifa'
        verbose_name_plural = 'Toifalar 📕📗📘'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_list_by_category', args=[str(self.slug)])
