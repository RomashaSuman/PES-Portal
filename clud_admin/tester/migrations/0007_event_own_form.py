# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0006_auto_20160305_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='own_form',
            field=models.URLField(null=True),
        ),
    ]