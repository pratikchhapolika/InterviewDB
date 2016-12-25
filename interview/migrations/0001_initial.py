# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_title', models.CharField(max_length=500)),
                ('question_description', models.CharField(default=b'Default question', max_length=2000)),
                ('question_company', models.CharField(max_length=200)),
                ('question_type', models.CharField(max_length=500)),
                ('url', models.SlugField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
