# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180305_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='DolotoWithYBT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('doloto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.DolotoDiametr')),
            ],
        ),
        migrations.AlterField(
            model_name='diametrybt',
            name='diametrYBT',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='diametrybt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 3, 5, 13, 22, 4, 899111)),
        ),
        migrations.AddField(
            model_name='dolotowithybt',
            name='ybt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.DiametrYBT'),
        ),
    ]
