# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180115_0630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='glavnaya',
            options={'verbose_name': 'Главная'},
        ),
    ]