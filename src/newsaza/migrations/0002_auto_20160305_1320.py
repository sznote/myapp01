# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsaza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='zipcode',
            field=models.IntegerField(max_length=10),
        ),
    ]
