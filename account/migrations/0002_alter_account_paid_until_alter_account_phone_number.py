# Generated by Django 4.1.5 on 2023-01-26 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='paid_until',
            field=models.DateField(default=datetime.date(2023, 1, 27)),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
