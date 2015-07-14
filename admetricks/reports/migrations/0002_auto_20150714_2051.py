# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='advisor',
            field=models.CharField(max_length=255, null=True, db_column=b'avisador'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='banner',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign',
            field=models.CharField(max_length=255, null=True, db_column=b'campanya'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='impact',
            field=models.IntegerField(null=True, db_column=b'impacto'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='media',
            field=models.CharField(max_length=255, null=True, db_column=b'medio'),
        ),
    ]
