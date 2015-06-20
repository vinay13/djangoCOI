# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0002_photo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pic',
            field=models.ImageField(width_field=500, upload_to=b'images/'),
        ),
    ]
