# Generated by Django 3.0.7 on 2020-07-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200702_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='use_purpose',
            field=models.CharField(choices=[('PR', 'Omaan käyttöön'), ('TX', 'Taxi')], default='PR', max_length=10),
        ),
    ]