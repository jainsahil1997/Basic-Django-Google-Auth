# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps')),
            ],
        ),
    ]
