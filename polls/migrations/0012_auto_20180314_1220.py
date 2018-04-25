# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180314_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyсalc',
            name='davl',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='historyсalc',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 14, 12, 20, 1, 212929)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 14, 12, 20, 1, 209928)),
        ),
    ]
