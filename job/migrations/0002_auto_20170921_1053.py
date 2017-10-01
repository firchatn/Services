# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-21 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ville',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='cin',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.Ville'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='lastname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='phone',
            field=models.CharField(default=5, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='work',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.Service'),
            preserve_default=False,
        ),
    ]