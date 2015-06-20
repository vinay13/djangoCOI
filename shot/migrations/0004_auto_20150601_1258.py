# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shot', '0003_auto_20150601_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='page',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
