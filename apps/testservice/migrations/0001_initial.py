# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-08 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=32, unique=True)),
                ('case_id', models.CharField(max_length=32, null=True)),
                ('next_id', models.TextField(null=True)),
                ('left_next_id', models.TextField(null=True)),
                ('count', models.CharField(max_length=32, null=True)),
                ('times', models.CharField(max_length=32, null=True)),
                ('now_case_id', models.CharField(max_length=32, null=True)),
                ('now_sheet', models.CharField(max_length=64, null=True)),
                ('left_sheet', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, null=True)),
                ('mailaddress', models.CharField(max_length=64, null=True)),
                ('asr_state', models.CharField(max_length=32, null=True)),
                ('nlu_state', models.CharField(max_length=32, null=True)),
                ('nlp_state', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NlpCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=32, unique=True)),
                ('count', models.CharField(max_length=32, null=True)),
                ('nlp_true', models.IntegerField(default=0)),
                ('nlp_fail', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ResultPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=512)),
                ('tools_log_path', models.CharField(max_length=512, null=True)),
                ('result_path', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=32, unique=True)),
                ('case_id', models.CharField(max_length=32, null=True)),
                ('entry_name', models.CharField(max_length=32, null=True)),
                ('table_name', models.CharField(max_length=1024, null=True)),
                ('version_num', models.CharField(max_length=32, null=True)),
                ('state', models.CharField(max_length=32, null=True)),
                ('start_time', models.CharField(max_length=128, null=True)),
                ('speed', models.CharField(default='0%', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TestPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=1024, null=True)),
                ('table_path', models.CharField(blank=True, editable=False, max_length=512)),
            ],
        ),
    ]
