# Generated by Django 4.0.5 on 2022-07-26 13:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_collection_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('desc', ckeditor.fields.RichTextField(default='', verbose_name='desc')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product Extra',
                'verbose_name_plural': 'Product Extras',
            },
        ),
    ]
