# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20180305_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='diametrybt',
            name='weightYBT',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 22, 8, 29, 61763)),
        ),
    ]
