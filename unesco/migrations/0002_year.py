# Generated by Django 3.1.2 on 2020-11-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(null=True)),
            ],
        ),
    ]