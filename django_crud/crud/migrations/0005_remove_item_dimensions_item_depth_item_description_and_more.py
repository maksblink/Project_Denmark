# Generated by Django 5.1.6 on 2025-05-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_item_remove_sensor_hydroponic_system_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='item',
            name='depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='is_available_for_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
