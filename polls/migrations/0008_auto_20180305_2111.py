# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180305_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoringDiametr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('boring', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BoringWithCasing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('boring', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.BoringDiametr')),
                ('casing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.CasingDiametr')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 21, 11, 39, 884154)),
        ),
    ]
