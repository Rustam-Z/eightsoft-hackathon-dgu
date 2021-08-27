from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify 

# Create your models here.


class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=200, unique=True, null=True)
    phone = models.CharField(verbose_name='telefon raqamingiz', max_length=255, blank=True)
    telegram = models.URLField(verbose_name='telegram URL', blank=True)
    image = models.ImageField(verbose_name='foto surat', upload_to='accounts/', blank=True)
    
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ('username',)
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar 👨‍👨‍👧‍👦'
