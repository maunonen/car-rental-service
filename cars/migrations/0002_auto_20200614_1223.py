# Generated by Django 3.0.7 on 2020-06-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='barnd',
            new_name='brand',
        ),
        migrations.AddField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('WG', 'Wagon'), ('SV', 'SUV'), ('HB', 'Hatchback'), ('SD', 'Sedan')], default='WG', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('DI', 'Diesel'), ('PE', 'Petrol'), ('EL', 'Electric'), ('HY', 'Hybrid')], default='PE', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('AU', 'Automatic'), ('MN', 'Manual')], default='MN', max_length=10),
        ),
    ]
