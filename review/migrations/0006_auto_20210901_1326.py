# Generated by Django 3.1.7 on 2021-09-01 13:26

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20210901_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=9),
        ),
    ]