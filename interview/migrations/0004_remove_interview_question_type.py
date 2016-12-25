# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_auto_20161213_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='question_type',
        ),
    ]
