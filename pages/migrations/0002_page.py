# Generated by Django 3.0.7 on 2020-09-17 12:02

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.CharField(choices=[('', 'Sivuston nimi'), ('AB', 'About'), ('NW', 'News'), ('CL', 'Car List'), ('CN', 'CONDITION'), ('PC', 'PRIVACY'), ('SV', 'SERVICES')], default='', max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(default=True)),
                ('news_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
