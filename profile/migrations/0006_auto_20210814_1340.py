# Generated by Django 3.1.7 on 2021-08-14 13:40

from django.db import migrations, models
import django_countries.fields
import profile.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_auto_20210712_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(default='DE', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True, validators=[profile.validators.validate_county]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[profile.validators.validate_phone_number]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[profile.validators.validate_postal_code]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, max_length=80, null=True, validators=[profile.validators.validate_alpha_numeric]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[profile.validators.validate_city]),
        ),
    ]
