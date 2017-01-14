# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-18 21:30
from __future__ import unicode_literals

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Finance classes',
            },
        ),
        migrations.CreateModel(
            name='FinanceSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('cumulative_usd', models.CharField(blank=True, max_length=300, null=True, verbose_name='Cumulative in USD')),
                ('cumulative_eur', models.CharField(blank=True, max_length=300, null=True, verbose_name='Cumulative in EUR')),
                ('discrete_usd', models.CharField(blank=True, max_length=300, null=True, verbose_name='Discrete in USD')),
                ('discrete_eur', models.CharField(blank=True, max_length=300, null=True, verbose_name='Discrete in EUR')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('finance_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sectors', to='finance.FinanceClass')),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320, unique=True, verbose_name='имя фонда')),
                ('fund_manager', models.CharField(blank=True, max_length=320, null=True)),
                ('is_published', models.BooleanField(default=False, help_text="Tick to make this entry live Note that administrators (like yourself) are allowed to preview inactive entries whereas the general public aren't.")),
                ('is_parcing', models.BooleanField(default=False, help_text='using for parsing')),
                ('bloombreg_ticker', models.CharField(max_length=320, unique=True, validators=[django.core.validators.RegexValidator('^\\w*:[A-Z]{2}$')], verbose_name='тикер на Bloomberg')),
                ('isin_ticker', models.CharField(max_length=320, unique=True, validators=[django.core.validators.RegexValidator('^\\w*:(USD|EUR)$')], verbose_name='тикер ISIN')),
                ('ms_rating', model_utils.fields.StatusField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=100, no_check_for_status=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='дата запуска фонда')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('currency', model_utils.fields.StatusField(blank=True, choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=100, no_check_for_status=True, null=True)),
                ('total_assets', models.DecimalField(blank=True, decimal_places=3, max_digits=19, null=True, verbose_name='total assets')),
                ('range_52_weeks', models.CharField(blank=True, max_length=320, null=True, verbose_name='52Wk Range ')),
                ('return_1_year', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='1 Yr Return')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('finance_sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to='finance.FinanceSector')),
                ('management_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to='company.ManagementCompany')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NAV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='NAV')),
                ('date', models.DateField(verbose_name='дата')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='navs', to='finance.Fund')),
            ],
            options={
                'get_latest_by': 'date',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='TopFundHolding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True)),
                ('name', models.CharField(max_length=320)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topfundholdings', to='finance.Fund')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='nav',
            unique_together=set([('date', 'fund')]),
        ),
    ]
