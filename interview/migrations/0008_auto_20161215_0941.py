# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0007_auto_20161214_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='question_company',
            field=models.CharField(max_length=200),
        ),
    ]
