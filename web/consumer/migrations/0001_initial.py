# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sa_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=255, blank=True)),
                ('state', models.BooleanField(default=True)),
                ('creator_time', models.DateTimeField(auto_now=True)),
                ('group_locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sa_role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=255)),
                ('stat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sa_root',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('root_name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=255, blank=True)),
                ('creator_time', models.DateTimeField(auto_now=True)),
                ('stat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sa_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=20, blank=True)),
                ('userpwd', models.CharField(max_length=255)),
                ('user_locked', models.BooleanField(default=False)),
                ('stat', models.BooleanField(default=True)),
                ('login_ip', models.CharField(max_length=32, blank=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('role_id', models.ForeignKey(to='consumer.Sa_role')),
                ('user_group', models.ForeignKey(to='consumer.Sa_group')),
            ],
        ),
        migrations.AddField(
            model_name='sa_group',
            name='group_root',
            field=models.ForeignKey(to='consumer.Sa_root'),
        ),
    ]
