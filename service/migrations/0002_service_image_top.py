# Generated by Django 4.0.5 on 2022-07-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image_top',
            field=models.ImageField(blank=True, null=True, upload_to='collections/', verbose_name='image_top'),
        ),
    ]
