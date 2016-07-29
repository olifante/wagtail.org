# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 12:00
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')

    ContentType.objects.filter(app_label='features', model='bullet').delete()
    ContentType.objects.filter(app_label='core', model='bullet').update(app_label='features', model='bullet')

    ContentType.objects.filter(app_label='features', model='featureaspect').delete()
    ContentType.objects.filter(app_label='core', model='featureaspect').update(app_label='features', model='featureaspect')

    ContentType.objects.filter(app_label='features', model='featurepagefeatureaspect').delete()
    ContentType.objects.filter(app_label='core', model='featurepagefeatureaspect').update(app_label='features', model='featurepagefeatureaspect')

    ContentType.objects.filter(app_label='features', model='featurepage').delete()
    ContentType.objects.filter(app_label='core', model='featurepage').update(app_label='features', model='featurepage')

    ContentType.objects.filter(app_label='features', model='featureindexpagemenuoption').delete()
    ContentType.objects.filter(app_label='core', model='featureindexpagemenuoption').update(app_label='features', model='featureindexpagemenuoption')

    ContentType.objects.filter(app_label='features', model='featureindexpage').delete()
    ContentType.objects.filter(app_label='core', model='featureindexpage').update(app_label='features', model='featureindexpage')


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('core', '0032_auto_20160729_1044'),
    ]

    operations = [
        migrations.RunPython(forwards_func),

        migrations.SeparateDatabaseAndState(
            state_operations=[

                migrations.RemoveField(
                    model_name='bullet',
                    name='snippet',
                ),
                migrations.RemoveField(
                    model_name='featureaspect',
                    name='screenshot',
                ),
                migrations.RemoveField(
                    model_name='featureindexpage',
                    name='page_ptr',
                ),
                migrations.RemoveField(
                    model_name='featureindexpagemenuoption',
                    name='link',
                ),
                migrations.RemoveField(
                    model_name='featureindexpagemenuoption',
                    name='page',
                ),
                migrations.RemoveField(
                    model_name='featurepage',
                    name='listing_image',
                ),
                migrations.RemoveField(
                    model_name='featurepage',
                    name='page_ptr',
                ),
                migrations.RemoveField(
                    model_name='featurepage',
                    name='social_image',
                ),
                migrations.RemoveField(
                    model_name='featurepagefeatureaspect',
                    name='feature_aspect',
                ),
                migrations.RemoveField(
                    model_name='featurepagefeatureaspect',
                    name='page',
                ),
                migrations.DeleteModel(
                    name='Bullet',
                ),
                migrations.DeleteModel(
                    name='FeatureAspect',
                ),
                migrations.DeleteModel(
                    name='FeatureIndexPage',
                ),
                migrations.DeleteModel(
                    name='FeatureIndexPageMenuOption',
                ),
                migrations.DeleteModel(
                    name='FeaturePage',
                ),
                migrations.DeleteModel(
                    name='FeaturePageFeatureAspect',
                ),
            ],
            database_operations=[],
        )
    ]
