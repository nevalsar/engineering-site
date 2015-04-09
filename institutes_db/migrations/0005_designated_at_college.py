# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutes_db', '0004_designated_at_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='designated_at',
            name='college',
            field=models.ForeignKey(default=1, to='institutes_db.College'),
            preserve_default=False,
        ),
    ]
