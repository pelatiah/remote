# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('i_remote', '0003_remotedesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteDesignTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_remote', models.CharField(max_length=200)),
                ('detail_specification', models.TextField()),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('remote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remotedesign', to='i_remote.RemoteDesign')),
            ],
        ),
    ]
