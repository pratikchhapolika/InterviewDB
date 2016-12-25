# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0010_auto_20161220_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='explanation',
            field=models.TextField(default=b'Explanation', max_length=500),
        ),
    ]
