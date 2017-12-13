# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20171124_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='../../static/media/images/news/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='../../static/media/images/products/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
