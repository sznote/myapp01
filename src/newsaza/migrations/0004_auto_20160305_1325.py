# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsaza', '0003_auto_20160305_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='zipcode',
            field=models.IntegerField(verbose_name=[8, 9]),
        ),
    ]
