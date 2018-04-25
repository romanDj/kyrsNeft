# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0013_auto_20180422_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyсalc',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historyсalc',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 22, 15, 4, 40, 410795)),
        ),
        migrations.AlterField(
            model_name='historyсalc',
            name='result',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 22, 15, 4, 40, 404792)),
        ),
    ]
