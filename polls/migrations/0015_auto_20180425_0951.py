# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20180422_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyсalc',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 25, 9, 51, 47, 644918)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 25, 9, 51, 47, 640916)),
        ),
    ]
