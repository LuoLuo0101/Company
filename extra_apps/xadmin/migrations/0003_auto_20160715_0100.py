# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin', '0002_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action_flag',
            field=models.CharField(max_length=32, verbose_name='action flag'),
        ),
    ]
