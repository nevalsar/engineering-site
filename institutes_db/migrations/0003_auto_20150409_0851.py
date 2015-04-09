# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutes_db', '0002_auto_20150407_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designated_at',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.ForeignKey(to='institutes_db.Department')),
            ],
            options={
                'verbose_name_plural': 'Designated_ats',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designation_name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='designated_at',
            name='desig',
            field=models.ForeignKey(to='institutes_db.Designation'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='designated_at',
            unique_together=set([('desig', 'dept')]),
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='approves',
            options={'verbose_name_plural': 'Approves'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='founding_history',
            options={'verbose_name_plural': 'Founding_Histories'},
        ),
        migrations.AlterModelOptions(
            name='offer_statistics',
            options={'verbose_name_plural': 'Offer_Statistics'},
        ),
        migrations.AlterModelOptions(
            name='offers',
            options={'verbose_name_plural': 'Offers'},
        ),
        migrations.AlterModelOptions(
            name='web_links',
            options={'verbose_name_plural': 'Web_Links'},
        ),
    ]
