# Generated by Django 4.2.4 on 2023-08-17 15:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VMS', '0005_alter_vms_records_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vms_records',
            name='v_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Vehicle Description'),
        ),
        migrations.AlterField(
            model_name='vms_records',
            name='v_model',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Vehicle Model'),
        ),
        migrations.AlterField(
            model_name='vms_records',
            name='v_number',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only Numbers & Characters')], verbose_name='Vehicle Number'),
        ),
        migrations.AlterField(
            model_name='vms_records',
            name='v_type',
            field=models.CharField(blank=True, choices=[('TWO WHEELER', 'Two'), ('THREE WHEELER', 'Three'), ('FOUR WHEELER', 'Four')], max_length=200, null=True, verbose_name='Vehicle Type'),
        ),
    ]
