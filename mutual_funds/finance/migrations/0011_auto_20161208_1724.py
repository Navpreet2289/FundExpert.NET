# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-08 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_fund_investment_strategy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nav',
            options={'get_latest_by': 'date', 'ordering': ('date',)},
        ),
    ]