# Generated by Django 3.2.6 on 2021-08-29 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_name'),
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='library_books', to='categories.category', verbose_name='toifasi'),
            preserve_default=False,
        ),
    ]
