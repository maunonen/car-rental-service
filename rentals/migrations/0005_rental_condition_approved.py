# Generated by Django 3.0.7 on 2020-10-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_rental_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='condition_approved',
            field=models.BooleanField(default=False),
        ),
    ]
