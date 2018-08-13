# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-23 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('book_author', models.CharField(max_length=255)),
                ('book_review', models.TextField()),
                ('book_cover', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='book_covers', to=settings.FILER_IMAGE_MODEL)),
                ('book_file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='filer.File')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]