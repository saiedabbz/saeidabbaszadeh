# Generated by Django 4.0.5 on 2022-08-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='quantity',
            field=models.BooleanField(blank=True, null=True, verbose_name='quantity'),
        ),
    ]
