# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180305_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiametrYBT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('diametrYBTValue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DolotoDiametr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MinDiametr', models.DecimalField(max_digits=5, decimal_places=2)),
                ('MaxDiametr', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 12, 7, 4, 923659)),
        ),
        migrations.AddField(
            model_name='diametrybt',
            name='diametrYBT',
            field=models.ForeignKey(to='polls.DolotoDiametr'),
        ),
    ]
