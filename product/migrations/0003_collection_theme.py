# Generated by Django 4.0.5 on 2022-07-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='theme',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Theme'),
        ),
    ]
