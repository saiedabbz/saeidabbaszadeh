# Generated by Django 4.0.5 on 2022-08-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_order_id'),
        ('service', '0002_service_image_top'),
        ('contact', '0005_inquerytype_remove_contact_contact_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=1, max_length=64, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquery_product', to='product.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquery_service', to='service.service', verbose_name='service'),
        ),
    ]
