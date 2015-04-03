# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='article_html',
            field=models.TextField(editable=False, default=datetime.datetime(2015, 4, 1, 18, 42, 2, 345928)),
            preserve_default=False,
        ),
    ]
