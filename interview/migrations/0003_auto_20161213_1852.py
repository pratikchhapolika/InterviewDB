# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20161213_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='question_company',
            field=models.CharField(max_length=200, choices=[(b'Google', b'Google'), (b'Facebook', b'Facebook'), (b'Microsoft', b'Microsoft'), (b'Amazon', b'Amazon'), (b'Quora', b'Quora'), (b'Salesforce', b'Salesforce')]),
        ),
    ]
