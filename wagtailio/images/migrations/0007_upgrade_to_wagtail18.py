# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-22 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_upgrade_to_wagtail17_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wagtailiorendition',
            name='filter_spec',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='wagtailiorendition',
            unique_together=set([('image', 'filter_spec', 'focal_point_key')]),
        ),
    ]