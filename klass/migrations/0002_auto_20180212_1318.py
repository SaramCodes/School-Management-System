# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-12 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasses',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
