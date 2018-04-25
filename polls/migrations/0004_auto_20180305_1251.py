# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180305_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diametrybt',
            name='diametrYBTValue',
        ),
        migrations.AlterField(
            model_name='diametrybt',
            name='diametrYBT',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 12, 51, 27, 164689)),
        ),
    ]
