# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwares',
            name='companylogo',
            field=models.ImageField(upload_to='nedia/companylogos'),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='productimage',
            field=models.ImageField(upload_to='media/softwares/productimages'),
        ),
    ]
