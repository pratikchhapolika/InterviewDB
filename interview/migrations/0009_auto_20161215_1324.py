# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0008_auto_20161215_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='question_description',
            field=django_markdown.models.MarkdownField(default=b'Default question'),
        ),
    ]
