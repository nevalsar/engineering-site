# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutes_db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web_links',
            name='fb_page',
        ),
        migrations.RemoveField(
            model_name='web_links',
            name='wiki_link',
        ),
    ]
