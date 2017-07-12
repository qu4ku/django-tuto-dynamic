# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=2048)),
            ],
        ),
    ]
