# Generated by Django 3.1.7 on 2021-09-01 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_auto_20210901_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[('1', ''), ('2', ''), ('3', ''), ('4', ''), ('5', '')], default=0, max_length=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
