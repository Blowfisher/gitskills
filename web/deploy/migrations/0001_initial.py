# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sa_deploy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name', models.CharField(max_length=32)),
                ('key_name', models.CharField(max_length=32)),
                ('value_name', models.CharField(max_length=32)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'sa_deploy',
            },
        ),
    ]
