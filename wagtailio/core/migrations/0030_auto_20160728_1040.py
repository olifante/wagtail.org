# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 10:40
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')

    ContentType.objects.filter(app_label='newsletter', model='newsletterpage').delete()
    ContentType.objects.filter(app_label='core', model='newsletterpage').update(app_label='newsletter', model='newsletterpage')

    ContentType.objects.filter(app_label='newsletter', model='newsletterindexpage').delete()
    ContentType.objects.filter(app_label='core', model='newsletterindexpage').update(app_label='newsletter', model='newsletterindexpage')

    ContentType.objects.filter(app_label='newsletter', model='newsletteremailaddress').delete()
    ContentType.objects.filter(app_label='core', model='newsletteremailaddress').update(app_label='newsletter', model='newsletteremailaddress')


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('core', '0029_auto_20160728_0914'),
    ]

    operations = [
        migrations.RunPython(forwards_func),

        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='NewsletterEmailAddress',
                ),
                migrations.RemoveField(
                    model_name='newsletterindexpage',
                    name='page_ptr',
                ),
                migrations.RemoveField(
                    model_name='newsletterpage',
                    name='page_ptr',
                ),
                migrations.DeleteModel(
                    name='NewsletterIndexPage',
                ),
                migrations.DeleteModel(
                    name='NewsletterPage',
                ),
            ],
            database_operations=[],
        )
    ]
