# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(db_column=b'fecha')),
                ('advisor', models.CharField(max_length=255, db_column=b'avisador')),
                ('campaign', models.CharField(max_length=255, db_column=b'campanya')),
                ('media', models.CharField(max_length=255, db_column=b'medio')),
                ('impact', models.IntegerField(db_column=b'impacto')),
                ('banner', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'test',
            },
        ),
    ]
