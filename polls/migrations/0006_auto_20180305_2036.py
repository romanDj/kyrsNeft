# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180305_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasingDiametr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('casingValue', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 20, 36, 33, 424526)),
        ),
    ]
