# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dpt_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dptname', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('userdesc', models.CharField(max_length=64)),
                ('stat', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'dpt_user',
            },
        ),
    ]
