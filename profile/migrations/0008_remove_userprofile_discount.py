# Generated by Django 3.2.7 on 2021-09-06 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0007_userprofile_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='discount',
        ),
    ]