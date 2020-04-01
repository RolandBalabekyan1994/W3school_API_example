# Generated by Django 2.0.12 on 2020-03-02 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.Employee'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shipper.Shipper'),
        ),
    ]