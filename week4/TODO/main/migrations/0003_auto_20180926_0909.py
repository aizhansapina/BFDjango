# Generated by Django 2.1.1 on 2018-09-26 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180926_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='due',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
