# Generated by Django 3.1.2 on 2020-11-13 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_auto_20201101_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Item name must be greater than one character')]),
        ),
    ]