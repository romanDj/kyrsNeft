# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180305_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasingWithYBT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('casing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.CasingDiametr')),
                ('ybt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.DiametrYBT')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 20, 50, 58, 451480)),
        ),
    ]
