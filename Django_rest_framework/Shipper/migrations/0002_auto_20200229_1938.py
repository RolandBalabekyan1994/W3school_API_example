# Generated by Django 2.0.12 on 2020-02-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shipper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipper',
            name='ShipperName',
            field=models.CharField(max_length=64, verbose_name='ShipperName'),
        ),
    ]