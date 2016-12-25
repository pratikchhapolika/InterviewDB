# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0009_auto_20161215_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='question_input',
            field=models.TextField(default=b'Input of the question', max_length=250),
        ),
        migrations.AddField(
            model_name='interview',
            name='question_output',
            field=models.TextField(default=b'Output of the question', max_length=500),
        ),
    ]
