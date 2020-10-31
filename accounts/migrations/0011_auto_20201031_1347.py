# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-31 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201031_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='imageupload',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tags'),
        ),
    ]