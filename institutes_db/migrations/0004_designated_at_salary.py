# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutes_db', '0003_auto_20150409_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='designated_at',
            name='salary',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
