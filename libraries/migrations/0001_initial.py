# Generated by Django 3.2.6 on 2021-08-27 14:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='kutubxona nomi')),
                ('region', models.CharField(choices=[('Tashkent', 'Tashkent'), ('Andijan', 'Andijan'), ('Bukhara', 'Bukhara'), ('Fergana', 'Fergana'), ('Jizzakh', 'Jizzakh'), ('Xorazm', 'Xorazm'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ('Samarkand', 'Samarkand'), ('Surxondaryo', 'Surxondaryo'), ('Karakalpakstan', 'Karakalpakstan')], default='Tashkent', max_length=255, verbose_name='shahar yoki viloyatingizni tanlang')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='telefon')),
                ('telegram', models.URLField(blank=True, verbose_name='telegram URL')),
                ('image', models.ImageField(blank=True, upload_to='libraries/', verbose_name='foto surat')),
            ],
            options={
                'verbose_name': 'Kutubxona',
                'verbose_name_plural': 'Kutubxonalar 🏫',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='kitob nomi')),
                ('author', models.CharField(max_length=255, verbose_name='muallif')),
                ('image', models.ImageField(blank=True, upload_to='books/', verbose_name='kitob rasmini yuklash')),
                ('description', models.TextField(blank=True, verbose_name='tavsifi')),
                ('available', models.BooleanField(default=True, verbose_name='mavjud?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='libraries.library', verbose_name='kutubxona')),
            ],
            options={
                'verbose_name': 'Kitob',
                'verbose_name_plural': 'Kitoblar 📚',
                'ordering': ('name', 'library'),
            },
        ),
    ]