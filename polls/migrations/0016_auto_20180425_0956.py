# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20180425_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AlterField(
            model_name='historyсalc',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 4, 25, 9, 56, 25, 830799)),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
