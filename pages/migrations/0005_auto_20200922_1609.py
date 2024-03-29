# Generated by Django 3.0.7 on 2020-09-22 16:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200918_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_name',
            field=models.CharField(choices=[('', 'Sivuston nimi'), ('AB', 'About'), ('NW', 'News'), ('CL', 'Car List'), ('CN', 'CONDITION'), ('PC', 'PRIVACY'), ('SV', 'SERVICES'), ('PM', 'PAYMENTS'), ('FQ', 'FAQ')], default='', max_length=20),
        ),
    ]
