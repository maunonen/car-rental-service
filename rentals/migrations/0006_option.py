# Generated by Django 3.0.7 on 2020-10-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_rental_condition_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
            ],
        ),
    ]
