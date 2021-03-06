# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sa_dpt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dptname', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=255)),
                ('stat', models.BooleanField(default=True)),
                ('creator_time', models.DateTimeField(auto_now=True)),
                ('dpt_locked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'sa_dpt',
            },
        ),
        migrations.CreateModel(
            name='Sa_role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=255)),
                ('stat', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'sa_role',
            },
        ),
        migrations.CreateModel(
            name='Sa_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=64)),
                ('userpwd', models.CharField(max_length=255)),
                ('user_locked', models.BooleanField(default=False)),
                ('stat', models.BooleanField(default=True)),
                ('login_ip', models.CharField(max_length=32)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('user_role', models.IntegerField(default=b'3')),
            ],
            options={
                'db_table': 'sa_user',
            },
        ),
    ]
