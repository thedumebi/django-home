# Generated by Django 3.1.2 on 2020-10-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_remove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
