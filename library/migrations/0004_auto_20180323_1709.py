# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-23 15:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20180323_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_covers', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='filer.File'),
        ),
    ]