# Generated by Django 2.1.1 on 2018-09-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180926_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='due',
            field=models.DateField(),
        ),
    ]
