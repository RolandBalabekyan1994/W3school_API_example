# Generated by Django 2.0.12 on 2020-03-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20200302_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('exav', 'exav'), ('gnac', 'gnac'), ('trav', 'beruma')], max_length=15, null=True, verbose_name='status'),
        ),
    ]
