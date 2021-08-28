# Generated by Django 3.2.2 on 2021-08-28 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210827_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('username',), 'verbose_name': 'User', 'verbose_name_plural': 'Foydalanuvchilar 👨\u200d👨\u200d👧\u200d👦'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='accounts/', verbose_name='foto surat'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='telefon raqamingiz'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.CharField(choices=[('Tashkent', 'Tashkent'), ('Andijan', 'Andijan'), ('Bukhara', 'Bukhara'), ('Fergana', 'Fergana'), ('Jizzakh', 'Jizzakh'), ('Xorazm', 'Xorazm'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ('Samarkand', 'Samarkand'), ('Surxondaryo', 'Surxondaryo'), ('Karakalpakstan', 'Karakalpakstan')], default='Tashkent', max_length=255, verbose_name='shahar yoki viloyatingizni tanlang'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram',
            field=models.URLField(blank=True, verbose_name='telegram URL'),
        ),
    ]