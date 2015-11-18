# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=1500)),
                ('client_address', models.CharField(max_length=1500)),
                ('client_desc', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_title', models.CharField(max_length=1500)),
                ('menu_link', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('new_title', models.CharField(max_length=1500)),
                ('new_desc', models.CharField(max_length=1500)),
                ('new_date', models.DateField()),
                ('new_img', models.ImageField(upload_to=b'media/news/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=1500)),
                ('product_desc', models.CharField(max_length=1500)),
                ('product_img', models.ImageField(upload_to=b'media/products/')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=1500)),
                ('service_desc', models.CharField(max_length=1500)),
                ('service_url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_path', models.ImageField(upload_to=b'media/imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1500)),
                ('img', models.ImageField(upload_to=b'media/users/')),
            ],
        ),
    ]
