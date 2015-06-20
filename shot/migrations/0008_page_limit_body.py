# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shot', '0007_auto_20150604_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='limit_body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
