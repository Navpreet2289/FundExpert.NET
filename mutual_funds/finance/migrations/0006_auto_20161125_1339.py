# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-25 13:39
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_financesector_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financesector',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='parsed_name', unique=True),
        ),
    ]
