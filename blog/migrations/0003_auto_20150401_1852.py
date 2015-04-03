# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150401_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
