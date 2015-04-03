# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150401_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='article',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_html',
        ),
    ]
