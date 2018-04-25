# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180305_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='historyСalc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 14, 12, 4, 5, 863464))),
                ('result', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 14, 12, 4, 5, 859459)),
        ),
    ]
