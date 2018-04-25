# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180314_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyсalc',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 22, 14, 58, 56, 753289)),
        ),
        migrations.AlterField(
            model_name='historyсalc',
            name='result',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 22, 14, 58, 56, 747284)),
        ),
    ]
