# Generated by Django 3.0.7 on 2020-09-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200917_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_lang',
            field=models.CharField(choices=[('', 'Sivuston nimi'), ('fi', 'Suomi'), ('ru', 'Venäjä'), ('en', 'Englanti'), ('es', 'Viro')], default='', max_length=20),
        ),
        migrations.AddConstraint(
            model_name='page',
            constraint=models.UniqueConstraint(fields=('page_name', 'page_lang'), name='unique_translations'),
        ),
    ]
