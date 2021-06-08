# Generated by Django 3.1.3 on 2021-02-01 15:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210201_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('windows_anons', models.TextField(max_length=250, verbose_name='Анонс')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('windows_full', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст статьи')),
            ],
        ),
        migrations.DeleteModel(
            name='Product_dors',
        ),
        migrations.DeleteModel(
            name='Product_window',
        ),
    ]
